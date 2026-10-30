#!/usr/bin/env python3
"""SEENmed — AUDIT-LECON-GOLD v3 (stdlib only).

Vérifie qu'une page leçon parle le langage des moteurs réels du site
(lesson.js, cine.js, keywords.js, ar-mode.js, bg-mode.js) et atteint la
densité des références ca-02/ca-09/bi-05. Voir STANDARD-OR-v3.md.

Usage :
  python3 AUDIT-LECON-GOLD-v3.py /chemin/medstudy lecons/pn-01-dyspnee.html [autres pages…]
  python3 AUDIT-LECON-GOLD-v3.py --strict-gold /chemin/medstudy lecons/pn-01-dyspnee.html

Le premier argument non-option est la racine du site (dossier contenant
lecons/, js/, css/, assets/). Les pages peuvent être données relatives à
cette racine ou en chemin absolu (artefact builder hors site accepté :
les références ../assets/img|audio/<id>/… sont alors aussi cherchées
dans le miroir builder ../img|audio/…).

Codes de sortie : 0 = aucun bloquant ; 1 = au moins un bloquant
(en --strict-gold, les écarts QUALITÉ deviennent bloquants).
"""
import html as ihtml
import json
import os
import re
import statistics
import struct
import sys
from pathlib import Path

LETTERS = ["A", "B", "C", "D", "E"]
FRONT = {"vue", "mindmap", "cine"}
BACK = {"annales", "entrainement", "fiche", "flashcards", "resume-total", "total"}

SKINS = {
    "bi": ("has-bio-field", "bioFieldCanvas", "bio-field.js"),
    "ca": ("has-cardio-field", "cardioFieldCanvas", "cardio-field.js"),
    "pn": ("has-pneumo-field", "pneumoFieldCanvas", "pneumo-field.js"),
    # ra : la sphère orbitale crée son propre canvas au runtime.
    "ra": ("has-orbital-sphere", None, "orbital-sphere-bg.js"),
}


def attrs(tag: str) -> dict:
    out = {}
    for m in re.finditer(r'([a-zA-Z_:][-a-zA-Z0-9_:.]*)\s*=\s*(?:"([^"]*)"|\'([^\']*)\')', tag):
        out[m.group(1).lower()] = ihtml.unescape(m.group(2) if m.group(2) is not None else m.group(3))
    return out


def strip_tags(fragment: str) -> str:
    text = re.sub(r"<script\b.*?</script>", " ", fragment, flags=re.S | re.I)
    text = re.sub(r"<[^>]+>", " ", text)
    return re.sub(r"\s+", " ", ihtml.unescape(text)).strip()


def webp_size(path: Path):
    """Dimensions réelles d'un WebP, sans PIL. None si illisible/autre format."""
    try:
        data = path.read_bytes()[:64]
    except OSError:
        return None
    if len(data) < 30 or data[0:4] != b"RIFF" or data[8:12] != b"WEBP":
        return None
    kind = data[12:16]
    try:
        if kind == b"VP8X":
            w = 1 + int.from_bytes(data[24:27], "little")
            h = 1 + int.from_bytes(data[27:30], "little")
            return w, h
        if kind == b"VP8L" and data[20] == 0x2F:
            bits = int.from_bytes(data[21:25], "little")
            return (bits & 0x3FFF) + 1, ((bits >> 14) & 0x3FFF) + 1
        if kind == b"VP8 " and data[23:26] == b"\x9d\x01\x2a":
            w = struct.unpack_from("<H", data, 26)[0] & 0x3FFF
            h = struct.unpack_from("<H", data, 28)[0] & 0x3FFF
            return w, h
    except Exception:
        return None
    return None


class Report:
    def __init__(self, strict=False):
        self.strict = strict
        self.blockers = []
        self.warnings = []
        self.metrics = []

    def block(self, code, msg):
        self.blockers.append(f"[{code}] {msg}")

    def warn(self, code, msg):
        self.warnings.append(f"[{code}] {msg}")

    def quality(self, code, msg):
        (self.block if self.strict else self.warn)(code, msg)

    def metric(self, msg):
        self.metrics.append(msg)


class Page:
    def __init__(self, root: Path, path: Path, rep: Report):
        self.root = root
        self.path = path
        self.rep = rep
        self.html = path.read_text(encoding="utf-8", errors="replace")
        m = re.match(r"^([a-z]{2,3}-\d+)-", path.name)
        self.lid = m.group(1) if m else path.stem
        self.scripts = []       # (pos, src)
        for m in re.finditer(r"<script\b[^>]*\bsrc=\"([^\"]+)\"[^>]*>", self.html, re.I):
            self.scripts.append((m.start(), m.group(1).split("?")[0]))
        self.json_blocks = {}   # id -> [(pos, parsed-or-None, raw)]
        for m in re.finditer(r"<script\b([^>]*)>(.*?)</script>", self.html, re.S | re.I):
            at = attrs("<script" + m.group(1) + ">")
            sid = at.get("id")
            if sid:
                raw = m.group(2).strip()
                try:
                    parsed = json.loads(raw)
                except Exception:
                    parsed = None
                self.json_blocks.setdefault(sid, []).append((m.start(), parsed, raw))
        # sections .lsection dans l'ordre du DOM + leurs fragments
        self.section_ids = []
        self.section_html = {}
        starts = []
        for m in re.finditer(r"<section\b[^>]*>", self.html, re.I):
            at = attrs(m.group(0))
            if "lsection" in (at.get("class") or "").split() and at.get("id"):
                starts.append((m.start(), at["id"], at))
        for i, (pos, sid, at) in enumerate(starts):
            end = starts[i + 1][0] if i + 1 < len(starts) else len(self.html)
            self.section_ids.append(sid)
            self.section_html[sid] = self.html[pos:end]
            self.section_html[sid + "::attrs"] = at
        self.nav = re.findall(r"<button\b[^>]*class=\"[^\"]*\bltab\b[^\"]*\"[^>]*data-target=\"([^\"]+)\"", self.html)

    # ---------- résolution de références ----------
    def resolve(self, ref):
        if not ref or ref.startswith(("http://", "https://", "data:", "#")):
            return None
        ref = ref.split("?")[0].split("#")[0]
        candidates = [(self.path.parent / ref), (self.root / "lecons" / ref)]
        m = re.match(r"\.\./assets/(img|audio)/[^/]+/(.+)$", ref)
        if m:  # miroir builder : page/ + img|audio/ frères
            candidates.append(self.path.parent.parent / m.group(1) / m.group(2))
        for c in candidates:
            c = Path(os.path.normpath(c))
            if c.exists():
                return c
        return Path(os.path.normpath(candidates[0]))

    def script_pos(self, needle):
        for pos, src in self.scripts:
            if src.endswith(needle):
                return pos
        return None

    def json_one(self, sid, engine=None, required=True):
        rep = self.rep
        blocks = self.json_blocks.get(sid, [])
        if not blocks:
            if required:
                rep.block("JSON", f"#{sid} absent")
            return None
        if len(blocks) > 1:
            rep.block("JSON", f"#{sid} présent {len(blocks)} fois (ID dupliqué : seul le premier est lu)")
        pos, parsed, _raw = blocks[0]
        if parsed is None:
            rep.block("JSON", f"#{sid} n'est pas un JSON parseable")
            return None
        if engine:
            epos = self.script_pos(engine)
            if epos is None:
                rep.block("SCRIPTS", f"moteur {engine} absent alors que #{sid} existe")
            elif pos > epos:
                rep.block("SCRIPTS", f"#{sid} est placé APRÈS {engine} : le moteur le lit trop tôt")
        return parsed


def audit_page(root: Path, path: Path, strict=False) -> Report:
    rep = Report(strict)
    pg = Page(root, path, rep)
    h = pg.html
    lid = pg.lid
    rep.metric(f"page {path.name} · {path.stat().st_size} o · {len(pg.section_ids)} sections")

    # ---------- structure / navigation ----------
    body_m = re.search(r"<body\b[^>]*>", h, re.I)
    body_at = attrs(body_m.group(0)) if body_m else {}
    if body_at.get("data-lesson-id") != lid:
        rep.block("STRUCT", f"body[data-lesson-id]={body_at.get('data-lesson-id')!r} != {lid!r}")
    if pg.nav != pg.section_ids:
        only_nav = [x for x in pg.nav if x not in pg.section_ids]
        only_sec = [x for x in pg.section_ids if x not in pg.nav]
        if only_nav:
            rep.block("NAV", f"onglets sans section : {only_nav}")
        if only_sec:
            rep.block("NAV", f"sections sans onglet : {only_sec}")
        if not only_nav and not only_sec:
            rep.block("NAV", "ordre des onglets != ordre des sections dans le DOM")
    for must in ("vue", "mindmap", "cine", "methode", "connexions", "annales", "entrainement", "fiche", "flashcards"):
        if must not in pg.section_ids:
            rep.block("STRUCT", f"section obligatoire absente : #{must}")
    if not ({"resume-total", "total"} & set(pg.section_ids)):
        rep.block("STRUCT", "section résumé total absente")
    if "flashcards" in pg.section_ids and "resume-total" in pg.section_ids:
        if pg.section_ids.index("flashcards") > pg.section_ids.index("resume-total"):
            rep.block("STRUCT", "flashcards doit précéder resume-total (ordre des références)")

    # sections de contenu = entre le front (vue/mindmap/cine) et le back
    content_ids = [s for s in pg.section_ids if s not in FRONT | BACK and s not in ("methode", "connexions")]
    ordinal = {}
    n = 0
    for s in pg.section_ids:
        if s in FRONT:
            continue
        if s in BACK:
            break
        n += 1
        ordinal[s] = str(n)

    # ---------- classes interdites (variante bi-06) ----------
    for bad in ("qopt", "qoptions", "score-box", "flash-grid"):
        if re.search(r'class="[^"]*\b' + re.escape(bad) + r'\b', h):
            rep.block("CONTRAT", f"classe interdite .{bad} présente (aucun moteur/CSS ne la connaît)")
    if 'id="flashApp"' in h:
        rep.block("CONTRAT", "#flashApp présent : le moteur flashcards attend #fcDeck")

    # ---------- QCM ----------
    exp_lengths = {"annales": [], "entrainement": []}
    total_q = 0
    for set_id in ("annales", "entrainement"):
        frag = pg.section_html.get(set_id)
        if frag is None:
            continue
        at = pg.section_html.get(set_id + "::attrs", {})
        if at.get("data-qcm-set") != set_id:
            rep.block("QCM", f"#{set_id} sans data-qcm-set=\"{set_id}\" : le score ne sera jamais calculé")
        if 'class="qs-val"' not in frag:
            rep.block("QCM", f"#{set_id} sans .qs-val : aucun affichage de score")
        starts = [m for m in re.finditer(r'<div\b[^>]*class="[^"]*\bqblock\b[^"]*"[^>]*>', frag)]
        if not starts:
            rep.block("QCM", f"#{set_id} ne contient aucun .qblock")
        for i, m in enumerate(starts):
            end = starts[i + 1].start() if i + 1 < len(starts) else len(frag)
            q = frag[m.start():end]
            total_q += 1
            label = f"{set_id} Q{i + 1}"
            qat = attrs(m.group(0))
            raw = qat.get("data-answer", "")
            answer = None
            try:
                answer = json.loads(raw)
            except Exception:
                rep.block("QCM", f"{label} : data-answer={raw!r} non JSON (lesson.js abandonne le bloc)")
            if isinstance(answer, list):
                if not answer or any(a not in LETTERS for a in answer):
                    rep.block("QCM", f"{label} : data-answer invalide {answer!r}")
            elif answer is not None:
                rep.block("QCM", f"{label} : data-answer n'est pas un tableau")
            if "<input" in q:
                rep.block("QCM", f"{label} : choix en <input> ignorés par le moteur")
            lis = re.findall(r'<li\b[^>]*data-l="([A-E])"', q)
            if 'class="qch"' not in q or len(lis) < 4:
                rep.block("QCM", f"{label} : choix .qch li[data-l] absents ou incomplets ({lis})")
            elif lis != LETTERS[:len(lis)]:
                rep.block("QCM", f"{label} : ordre des choix incohérent {lis}")
            if 'class="qverdict"' not in q and "qverdict" not in q:
                rep.block("QCM", f"{label} : .qverdict absent")
            if "qcheck" not in q:
                rep.block("QCM", f"{label} : bouton .qcheck absent (correction irrévélable)")
            em = re.search(r'<div\b[^>]*class="[^"]*\bqexp\b[^"]*"[^>]*>(.*)', q, re.S)
            if not em:
                rep.block("QCM", f"{label} : .qexp absente")
                continue
            if re.search(r'class="[^"]*\bqexp\b[^"]*"[^>]*\bhidden\b', q):
                rep.block("QCM", f"{label} : .qexp[hidden] (le moteur révèle via .answered, pas via hidden)")
            exp = em.group(1)
            exp_lengths[set_id].append(len(strip_tags(exp)))
            items = re.findall(r'<div\b[^>]*class="[^"]*\bqexp-item\b[^"]*"[^>]*>(.*?)</div>', exp, re.S)
            if len(items) < 2:
                rep.quality("QCM-EXP", f"{label} : correction non structurée en .qexp-item ({len(items)}), les références en ont {len(lis) or 5}")
            elif lis and len(items) != len(lis):
                rep.quality("QCM-EXP", f"{label} : {len(items)} .qexp-item pour {len(lis)} propositions (gold = 1 par proposition)")
            elif lis:
                heads = []
                for it in items:
                    t = strip_tags(it)
                    heads.append(t[:1])
                if heads != LETTERS[:len(lis)]:
                    rep.quality("QCM-EXP", f"{label} : .qexp-item non ordonnés A→E ({heads})")
            if "qexp-memo" not in exp:
                rep.quality("QCM-EXP", f"{label} : pas de .qexp-memo (piège nommé + phrase à retenir)")
    rep.metric(f"QCM total : {total_q}")
    for k, vals in exp_lengths.items():
        if vals:
            med = int(statistics.median(vals))
            rep.metric(f"corrections {k} : n={len(vals)} médiane {med} caractères")
            if med < 650:
                rep.quality("QCM-EXP", f"corrections {k} trop courtes (médiane {med} < 650, cible références)")

    # ---------- Ciné ----------
    cine = pg.json_one("cineData", engine="cine.js", required=("cine" in pg.section_ids or "cine" in pg.nav))
    chapters = []
    if isinstance(cine, dict):
        if "chapters" in cine and "chapitres" not in cine:
            rep.block("CINE", "cineData utilise la clé 'chapters' : cine.js exige 'chapitres' et sort immédiatement")
        chapters = cine.get("chapitres") or []
        if not isinstance(chapters, list) or not chapters:
            rep.block("CINE", "cineData.chapitres absent ou vide")
            chapters = []
    if "cine" in pg.section_ids and 'id="cinePlayer"' not in pg.section_html.get("cine", ""):
        rep.block("CINE", "section #cine sans #cinePlayer : pas de lecteur central")
    ar_missing = 0
    for i, c in enumerate(chapters):
        if not isinstance(c, dict):
            rep.block("CINE", f"chapitre {i} non objet")
            continue
        for wrong in ("title", "audio", "audioAr", "images"):
            if wrong in c:
                rep.block("CINE", f"chapitre {i} : clé interdite '{wrong}' (contrat = t/imgs/fr/ar)")
        if not c.get("t"):
            rep.block("CINE", f"chapitre {i} sans titre 't'")
        if not c.get("fr"):
            rep.block("CINE", f"chapitre {i} sans piste 'fr'")
        if not c.get("ar"):
            ar_missing += 1
        if not c.get("imgs"):
            rep.block("CINE", f"chapitre {i} sans 'imgs'")
        for key in ("fr", "ar"):
            if c.get(key):
                p = pg.resolve(c[key])
                if p is None or not p.exists():
                    rep.block("CINE", f"chapitre {i} piste {key} introuvable : {c[key]}")
        for im in c.get("imgs") or []:
            p = pg.resolve(im)
            if p is None or not p.exists():
                rep.block("CINE", f"chapitre {i} image introuvable : {im}")
    if chapters and ar_missing:
        rep.quality("CINE-AR", f"{ar_missing}/{len(chapters)} chapitre(s) sans piste arabe (gold ca-02/ra-02 = FR+AR partout)")
    # mini-lecteurs de section
    spot_total = 0
    for sid in content_ids + (["resume-total"] if "resume-total" in pg.section_ids else []):
        frag = pg.section_html.get(sid, "")
        spots = re.findall(r'<div\b[^>]*class="[^"]*\bcine-spot\b[^"]*"[^>]*data-ch="(\d+)"', frag)
        spot_total += len(spots)
        if not spots:
            rep.quality("CINE-SPOT", f"section #{sid} sans mini-lecteur .cine-spot sous sa planche")
        for s in spots:
            if chapters and int(s) >= len(chapters):
                rep.block("CINE-SPOT", f"#{sid} : data-ch={s} hors limites ({len(chapters)} chapitres)")
    rep.metric(f"Ciné : {len(chapters)} chapitres · {spot_total} mini-lecteurs")

    # ---------- Mots-clés ----------
    kw = pg.json_one("kwData", engine="keywords.js", required=False)
    if kw is not None:
        if isinstance(kw, dict):
            rep.block("KW", "kwData est un objet {items:…} : keywords.js exige un tableau [{t,s,n,d,a}]")
        elif isinstance(kw, list):
            rep.metric(f"mots-clés : {len(kw)} termes")
            if len(kw) < 45:
                rep.quality("KW", f"seulement {len(kw)} termes (cible 45–60, ca-02 = 57)")
            seen_terms = set()
            for i, w in enumerate(kw):
                if not isinstance(w, dict) or not all(isinstance(w.get(k), str) and w.get(k) for k in ("t", "s", "n", "d", "a")):
                    rep.block("KW", f"entrée {i} incomplète (t/s/n/d/a chaînes requises) : {str(w)[:90]}")
                    continue
                if isinstance(w.get("a"), dict):
                    rep.block("KW", f"entrée {i} ({w.get('t')}) : 'a' objet au lieu de chaîne")
                if w["s"] not in pg.section_ids:
                    rep.block("KW", f"terme « {w['t']} » pointe une section inexistante #{w['s']}")
                elif w["s"] in ordinal and w["n"] != ordinal[w["s"]]:
                    rep.quality("KW", f"terme « {w['t']} » : n={w['n']} mais #{w['s']} est la section {ordinal[w['s']]}")
                if w["t"] in seen_terms:
                    rep.quality("KW", f"terme dupliqué : {w['t']}")
                seen_terms.add(w["t"])

    # ---------- Flashcards ----------
    fc_frag = pg.section_html.get("flashcards", "")
    for need in ("fcDeck", "fcStage", "fcCard", "fcFront", "fcBack", "fcCount", "fcAgain", "fcHard", "fcGood", "fcEasy", "fcDone"):
        cnt = len(re.findall(r'id="' + need + r'"', h))
        if cnt != 1:
            rep.block("FC", f"#{need} ×{cnt} (le deck du moteur en exige exactement 1)")
    fc = pg.json_one("fcData", engine="lesson.js", required=True)
    if isinstance(fc, list):
        rep.metric(f"flashcards : {len(fc)} cartes")
        if not (20 <= len(fc) <= 35):
            rep.quality("FC", f"{len(fc)} cartes (cible 25–30)")
        ids = []
        for i, c in enumerate(fc):
            if not isinstance(c, dict) or not c.get("q") or not c.get("a"):
                rep.block("FC", f"carte {i} sans q/a")
                continue
            if not c.get("id"):
                rep.block("FC", f"carte {i} sans id stable (la répétition espacée écrase les clés undefined)")
            ids.append(c.get("id"))
        dup = [x for x in set(ids) if x and ids.count(x) > 1]
        if dup:
            rep.block("FC", f"ids de cartes dupliqués : {dup}")

    # ---------- Arabe ----------
    tr_keys = re.findall(r'data-tr="([^"]+)"', h)
    ar = pg.json_one("arData", engine="ar-mode.js", required=bool(tr_keys))
    if isinstance(ar, dict):
        orphans = sorted(set(tr_keys) - set(ar))
        unused = sorted(set(ar) - set(tr_keys))
        rep.metric(f"arabe : {len(set(tr_keys))} blocs data-tr · {len(ar)} clés arData")
        if orphans:
            rep.block("AR", f"data-tr sans traduction : {orphans[:8]}{'…' if len(orphans) > 8 else ''}")
        if unused:
            rep.block("AR", f"clés arData inutilisées : {unused[:8]}{'…' if len(unused) > 8 else ''}")
        if len(tr_keys) != len(set(tr_keys)):
            rep.block("AR", "clés data-tr dupliquées dans la page")

    # ---------- Fiche flash ----------
    fiche = pg.section_html.get("fiche", "")
    if fiche:
        if 'class="flashsheet' not in fiche:
            rep.block("FICHE", "pas de .flashsheet (le composant des références)")
        if "ff-2x2" not in fiche:
            rep.quality("FICHE", "pas de grille .ff-2x2 (4 macro-cellules ca-02/ca-09)")
        cells = re.findall(r'<div\b[^>]*class="[^"]*\bflash-cell\b[^"]*"[^>]*>(.*?)(?=<div\b[^>]*class="[^"]*\bflash-cell\b|</section)', fiche, re.S)
        rep.metric(f"fiche flash : {len(cells)} cellules · {len(strip_tags(fiche))} caractères de texte")
        if len(cells) != 4:
            rep.quality("FICHE", f"{len(cells)} cellules (gold = 4 macro-cellules)")
        if len(strip_tags(fiche)) < 2400:
            rep.quality("FICHE", "texte de fiche < 2 400 caractères (ca-02 = 2 499, ca-09 = 3 777)")
        for i, cell in enumerate(cells):
            if "<h4" not in cell:
                rep.quality("FICHE", f"cellule {i + 1} sans titre <h4>")
            if 'class="flash-img"' not in cell:
                rep.block("FICHE", f"cellule {i + 1} sans img.flash-img (lightbox/style non appliqués)")
            nli = len(re.findall(r"<li\b", cell))
            if nli < 4:
                rep.quality("FICHE", f"cellule {i + 1} : {nli} puces de faits (gold = 4–7)")

    # ---------- Peau de module ----------
    prefix = lid.split("-")[0]
    skin = SKINS.get(prefix)
    if skin:
        cls, canvas_id, jsfile = skin
        body_classes = (body_at.get("class") or "").split()
        if cls not in body_classes:
            rep.block("PEAU", f"body sans classe {cls} : le module n'a pas sa peau")
        if canvas_id and f'id="{canvas_id}"' not in h:
            rep.block("PEAU", f"canvas #{canvas_id} absent : le script de champ sort en silence (fond vide)")
        if pg.script_pos(jsfile) is None:
            rep.block("PEAU", f"script de peau {jsfile} absent")
        if prefix == "pn":
            js_path = root / "js" / "pneumo-field.js"
            if not js_path.exists():
                rep.block("PEAU", "js/pneumo-field.js absent du site")
            css = (root / "css" / "style.css").read_text(encoding="utf-8", errors="ignore") if (root / "css" / "style.css").exists() else ""
            for theme in ("light", "aurora", "ocean"):
                if f'html[data-theme="{theme}"] body.has-pneumo-field' not in css:
                    rep.block("PEAU", f"style.css sans identité pneumologie pour le thème {theme}")
            if "#pneumoFieldCanvas" not in css:
                rep.block("PEAU", "style.css ne connaît pas #pneumoFieldCanvas (modes fixe/photo)")
            main_js = (root / "js" / "main.js").read_text(encoding="utf-8", errors="ignore") if (root / "js" / "main.js").exists() else ""
            if "pneumo-root" not in main_js:
                rep.block("PEAU", "main.js n'ajoute pas la racine pneumo-root (scrollbar du module)")
    else:
        rep.warn("PEAU", f"préfixe {prefix} sans peau connue dans l'audit")

    # ---------- Images ----------
    seen_src = {}
    gen_dims = []
    for m in re.finditer(r"<img\b[^>]*>", h, re.I):
        at = attrs(m.group(0))
        src = at.get("src", "")
        if not src:
            continue
        seen_src[src] = seen_src.get(src, 0) + 1
        p = pg.resolve(src)
        if p is None or not p.exists():
            rep.block("IMG", f"image introuvable : {src}")
            continue
        alt = at.get("alt") or ""
        if len(alt) < 40:
            rep.quality("IMG-ALT", f"alt trop court ({len(alt)} car.) pour {src}")
        if "sans texte suivi" in alt.lower():
            rep.quality("IMG-CONTRAT", f"alt/consigne « sans texte suivi » interdite par v3 : {src}")
        real = webp_size(p)
        if real:
            try:
                declared = (int(at.get("width", "0")), int(at.get("height", "0")))
            except ValueError:
                declared = (0, 0)
            if declared != real:
                rep.quality("IMG-DIMS", f"{src} : width/height déclarés {declared} != réels {real}")
            if "/reel/" not in src and not src.endswith("hero.webp"):
                gen_dims.append((src, real))
    for src, n in seen_src.items():
        if n > 1:
            rep.quality("IMG-DUP", f"même image utilisée {n} fois dans la page : {src}")
    odd = [(s, d) for s, d in gen_dims if d != (1376, 768)]
    if odd:
        rep.quality("IMG-DIMS", f"{len(odd)} planche(s) générée(s) hors 1376×768 : " + ", ".join(f"{Path(s).name} {d[0]}×{d[1]}" for s, d in odd[:6]))
    rep.metric(f"images page : {sum(seen_src.values())} ({len(seen_src)} fichiers distincts)")

    return rep


def audit_engines(root: Path, rep: Report):
    """Le standard suit les moteurs : si leurs contrats changent, on le voit."""
    checks = [
        ("js/lesson.js", [".qch li", "data-answer", "qverdict", "fcDeck", "fcData", "data-qcm-set"]),
        ("js/cine.js", ["chapitres", "cinePlayer", "cine-spot"]),
        ("js/keywords.js", ["kwData", "Array.isArray"]),
        ("js/ar-mode.js", ["arData", "data-tr"]),
        ("js/bg-mode.js", ["pneumo", "planche", "photo"]),
    ]
    for rel, needles in checks:
        p = root / rel
        if not p.exists():
            rep.block("MOTEURS", f"{rel} absent du site")
            continue
        txt = p.read_text(encoding="utf-8", errors="ignore")
        for n in needles:
            if n not in txt:
                rep.block("MOTEURS", f"{rel} ne contient plus « {n} » : contrat moteur modifié, réviser STANDARD-OR-v3 avant de patcher les pages")


def main(argv):
    strict = "--strict-gold" in argv
    args = [a for a in argv if not a.startswith("--")]
    if len(args) < 2:
        print(__doc__)
        return 2
    root = Path(args[0]).resolve()
    pages = []
    for a in args[1:]:
        p = Path(a)
        if not p.is_absolute() and not p.exists():
            p = root / a
        pages.append(p.resolve())

    eng = Report(strict)
    audit_engines(root, eng)
    total_block = len(eng.blockers)
    for b in eng.blockers:
        print("BLOQUANT", b)

    for p in pages:
        rep = audit_page(root, p, strict)
        print(f"\n=== {p.name} ===")
        for mt in rep.metrics:
            print("  ·", mt)
        for b in rep.blockers:
            print("  BLOQUANT", b)
        for w in rep.warnings:
            print("  ⚠", w)
        print(f"  → {len(rep.blockers)} bloquant(s), {len(rep.warnings)} avertissement(s)")
        total_block += len(rep.blockers)
    print(f"\nTOTAL : {total_block} bloquant(s){' (strict-gold)' if strict else ''}")
    return 1 if total_block else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
