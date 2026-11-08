#!/usr/bin/env python3
"""SEENmed — garde-fou images (AGENT-4).

Deux défauts d'usage signalés par l'utilisateur le 30/10 sur pn-08, dont il ne
faut plus jamais reproduire la cause :
  A. « pas assez d'images : pas une image par section »  -> couverture.
  B. des images du cours (reels) « étirées, dimensions anormales », et une
     planche générée étirée aussi -> distorsion / format.

Ce script mesure, il ne répare rien.

Usage :
  python3 verifier-images.py /chemin/medstudy                 # tout le site
  python3 verifier-images.py /chemin/medstudy lecons/pn-11-*.html
  python3 verifier-images.py --lesson pn-11 /chemin/medstudy

Sorties :
  1) COUVERTURE : sections de contenu sans aucune image  -> liste (défaut A).
  2) DISTORSION : attribut width/height de la page != dimensions réelles du
     fichier -> l'image est étirée par le navigateur (défaut B, exact).
  3) FORMAT : planche générée hors 1376x768 (tolérance 1 %) -> à déclarer ou
     à refaire ; reel hors format « normal » (ratio > 2.3 ou < 0.75) ->
     contrôle zoom obligatoire avant installation.
  4) CONSEIL de correction : jamais de width/height « jolis » ; toujours les
     dimensions réelles, ou régénérer l'image au bon format.
"""
import os
import re
import sys
from pathlib import Path

GEN_W, GEN_H = 1376, 768
TOL = 0.01          # 1 % de tolérance sur le ratio 1376x768
REEL_MIN_RATIO = 0.75
REEL_MAX_RATIO = 2.30


def real_dims(path):
    """Dimensions réelles (PIL si dispo, sinon en-têtes PNG/JPEG/WebP)."""
    try:
        from PIL import Image  # noqa
        with Image.open(path) as im:
            return im.size
    except Exception:
        pass
    try:
        with open(path, "rb") as f:
            head = f.read(32)
            if head[:8] == b"\x89PNG\r\n\x1a\n":
                return int.from_bytes(head[16:20], "big"), int.from_bytes(head[20:24], "big")
            if head[:2] == b"\xff\xd8":
                f.seek(2)
                while True:
                    marker = f.read(2)
                    if len(marker) < 2 or marker[0] != 0xFF:
                        return None
                    if marker[1] in (0xC0, 0xC1, 0xC2):
                        f.read(3)
                        h = int.from_bytes(f.read(2), "big")
                        w = int.from_bytes(f.read(2), "big")
                        return w, h
                    ln = int.from_bytes(f.read(2), "big")
                    f.seek(ln - 2, 1)
            if head[:4] == b"RIFF" and head[8:12] == b"WEBP":
                kind = head[12:16]
                if kind == b"VP8X":
                    w = int.from_bytes(head[24:27], "little") + 1
                    h = int.from_bytes(head[27:30], "little") + 1
                    return w, h
                if kind == b"VP8L":
                    b = head[21:25]
                    w = 1 + (((b[1] & 0x3F) << 8) | b[0])
                    h = 1 + (((b[3] & 0x0F) << 10) | (b[2] << 2) | ((b[1] & 0xC0) >> 6))
                    return w, h
                if kind == b"VP8 ":
                    f.seek(26)
                    b = f.read(4)
                    w = int.from_bytes(b[0:2], "little") & 0x3FFF
                    h = int.from_bytes(b[2:4], "little") & 0x3FFF
                    return w, h
    except Exception:
        return None
    return None


IMG_RE = re.compile(r"<img\b[^>]*>", re.I)
ATTR = lambda tag, name: (re.search(rf'{name}\s*=\s*"([^"]*)"', tag, re.I) or [None, None])[1]
SEC_RE = re.compile(r'<section class="lsection"[^>]*id="([^"]+)"(.*?)</section>', re.S)
IMG_IN = re.compile(r"<img\b[^>]*>", re.I)


def check_page(site: Path, page: Path):
    html = page.read_text(encoding="utf-8", errors="replace")
    pid = re.match(r"^([a-z]{2,3}-\d+)", page.name)
    lid = pid.group(1) if pid else "?"
    rows = {"dims": [], "format": [], "cover": []}

    for tag in IMG_RE.findall(html):
        src = ATTR(tag, "src") or ""
        if not src or src.startswith(("http", "data:")):
            continue
        clean = src.split("?")[0].lstrip("./")
        if clean.startswith("assets/"):
            f = site / clean
        elif clean.startswith("../assets/"):
            f = site / clean[3:]
        else:
            continue
        w, h = ATTR(tag, "width"), ATTR(tag, "height")
        if not f.is_file():
            rows["dims"].append((src, "FICHIER ABSENT", None))
            continue
        rd = real_dims(f)
        if not rd:
            rows["dims"].append((src, "image illisible ou dimensions indéterminables", None))
            continue
        rw, rh = rd
        try:
            dw, dh = int(w), int(h)
        except (TypeError, ValueError):
            dw = dh = None
        if dw and dh and (dw, dh) != (rw, rh):
            rows["dims"].append((src, f"déclaré {dw}x{dh} != réel {rw}x{rh}", round(dw / dh, 3)))
        ratio = rw / rh
        is_reel = "/reel/" in src
        if not is_reel:
            if ATTR(tag, "data-large-planche") == "true":
                if min(rw, rh) < 768 or rw * rh < 1400000 or not 0.5 <= ratio <= 2.3:
                    rows["format"].append((src, f"grande planche trop petite ou ratio extrême : {rw}x{rh}", round(ratio, 3)))
                if not dw or not dh:
                    rows["dims"].append((src, "grande planche : width/height obligatoires", None))
            else:
                gen_ratio = GEN_W / GEN_H
                if abs(ratio - gen_ratio) / gen_ratio > TOL:
                    rows["format"].append((src, f"{rw}x{rh} (attendu 1376x768)", round(ratio, 3)))
        elif ratio < REEL_MIN_RATIO or ratio > REEL_MAX_RATIO:
            rows["format"].append((src, f"reel {rw}x{rh} ratio {ratio:.2f} — zoom obligatoire", round(ratio, 3)))

    # Couverture : sections de contenu (numérotées) sans aucune image
    for sid, body in SEC_RE.findall(html):
        if sid in {"vue", "mindmap", "cine", "methode", "connexions", "annales",
                   "entrainement", "fiche", "flashcards", "resume-total"}:
            continue
        if not IMG_IN.search(body):
            rows["cover"].append(sid or "(sans id)")

    print(f"\n=== {page.name}  [{lid}] ===")
    print(f"  sections sans image : {len(rows['cover'])}"
          + ("  -> " + ", ".join(rows["cover"]) if rows["cover"] else "  ✓"))
    print(f"  images étirées (width/height != réel) : {len(rows['dims'])}"
          + ("" if not rows["dims"] else "  ⛔"))
    for src, why, _ in rows["dims"]:
        print(f"     - {src} : {why}")
    print(f"  format hors norme : {len(rows['format'])}"
          + ("" if not rows["format"] else "  ⚠"))
    for src, why, _ in rows["format"]:
        print(f"     - {src} : {why}")
    return rows


def main(argv):
    lesson = None
    if argv and argv[0] == "--lesson":
        lesson, argv = argv[1], argv[2:]
    if not argv:
        print(__doc__)
        return 2
    site = Path(argv[0]).resolve()
    pages = [Path(p).resolve() if not Path(p).is_absolute() else Path(p)
             for p in argv[1:]] or sorted((site / "lecons").glob("*.html"))
    if lesson:
        pages = [p for p in pages if Path(p).name.startswith(lesson)]
    total_bad = 0
    cover_total = 0
    for p in pages:
        p = p if p.is_file() else (site / p)
        if not p.is_file():
            print(f"!! page introuvable : {p}")
            continue
        r = check_page(site, p)
        total_bad += len(r["dims"]) + len(r["format"])
        cover_total += len(r["cover"])
    print(f"\nTOTAL : {len(pages)} page(s) · {cover_total} section(s) sans image · "
          f"{total_bad} anomalie(s) dimension/format")
    return 1 if (total_bad or cover_total) else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
