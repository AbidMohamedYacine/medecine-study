#!/usr/bin/env python3
"""
COLLER-MP3.py — Assemble un « résumé long » à partir de plusieurs générations vocales.

Méthode (STANDARD-OR-v3 §4.1) :
  1. Le script du résumé est écrit EN ENTIER (toutes les sections), sans peur de la limite.
  2. Il est découpé aux frontières de phrases en parties de ≤ ~1 400 caractères.
  3. Chaque partie est générée avec le MÊME voice_id (chaque partie compte dans le cap 10/message).
  4. Ce script colle les parties en UN seul MP3 propre :
     - garde l'en-tête ID3v2 de la 1re partie, retire ceux des suivantes (+ ID3v1 éventuels) ;
     - vérifie que toutes les parties partagent la même fréquence d'échantillonnage ;
     - affiche la durée estimée de chaque partie et du résultat (contrôle : somme ≈ total).
  La page ne référence QUE le fichier final (resume.mp3 / resume-ar.mp3), jamais les parties.

Usage : python3 COLLER-MP3.py partie1.mp3 partie2.mp3 [partie3.mp3 ...] -o resume.mp3
"""
import sys, os, argparse

SR = {3: [44100, 48000, 32000], 2: [22050, 24000, 16000], 0: [11025, 12000, 8000]}
BR = {1: [0, 32, 40, 48, 56, 64, 80, 96, 112, 128, 160, 192, 224, 256, 320],
      2: [0, 8, 16, 24, 32, 40, 48, 56, 64, 80, 96, 112, 128, 144, 160]}


def id3v2_len(d):
    if d[:3] != b'ID3':
        return 0
    sz = ((d[6] & 0x7f) << 21) | ((d[7] & 0x7f) << 14) | ((d[8] & 0x7f) << 7) | (d[9] & 0x7f)
    return 10 + sz + (10 if d[5] & 0x10 else 0)  # + pied éventuel


def strip_tags(d, keep_head=False):
    if not keep_head:
        d = d[id3v2_len(d):]
    if len(d) >= 128 and d[-128:-125] == b'TAG':  # ID3v1
        d = d[:-128]
    return d


def probe(d):
    """Retourne (durée estimée en s, fréquence) en marchant les trames MPEG Layer III."""
    i = id3v2_len(d)
    n = len(d)
    samples = 0
    sr = None
    while i < n - 4:
        if d[i] == 0xFF and (d[i + 1] & 0xE0) == 0xE0:
            ver = (d[i + 1] >> 3) & 3
            layer = (d[i + 1] >> 1) & 3
            bri = (d[i + 2] >> 4) & 0xF
            sri = (d[i + 2] >> 2) & 3
            pad = (d[i + 2] >> 1) & 1
            if layer == 1 and ver in SR and 1 <= bri <= 14 and sri <= 2:
                v1 = (ver == 3)
                s = SR[ver][sri]
                br = BR[1 if v1 else 2][bri] * 1000
                flen = ((144 if v1 else 72) * br // s) + pad
                if flen > 0:
                    if sr is None:
                        sr = s
                    samples += 1152 if v1 else 576
                    i += flen
                    continue
        i += 1
    return (samples / sr if sr else 0.0), sr


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('parts', nargs='+')
    ap.add_argument('-o', '--out', required=True)
    a = ap.parse_args()
    if len(a.parts) < 2:
        sys.exit('Il faut au moins 2 parties.')
    blobs = []
    sr_ref = None
    total = 0.0
    for k, p in enumerate(a.parts):
        raw = open(p, 'rb').read()
        dur, sr = probe(raw)
        if sr is None:
            sys.exit(f'❌ {p} : aucune trame MP3 lisible.')
        if sr_ref is None:
            sr_ref = sr
        elif sr != sr_ref:
            sys.exit(f'❌ Fréquences différentes ({sr_ref} vs {sr} dans {p}) : NE PAS coller, régénérer la partie.')
        total += dur
        print(f'  partie {k + 1} : {os.path.basename(p):40s} ~{dur:6.1f} s  ({sr} Hz)')
        blobs.append(strip_tags(raw, keep_head=(k == 0)))
    out = b''.join(blobs)
    with open(a.out, 'wb') as f:
        f.write(out)
    dur, sr = probe(out)
    n_id3 = out.count(b'ID3')
    print(f'✅ {a.out} : {len(out) / 1024:.0f} Ko, ~{dur:.1f} s (somme des parties ~{total:.1f} s), ID3 dans le fichier : {n_id3}')
    if abs(dur - total) > 2.0:
        print('⚠️ Écart durée > 2 s : vérifier les parties avant livraison.')
    if n_id3 != 1:
        print('⚠️ ID3 multiples : un tag a survécu au nettoyage, vérifier.')


if __name__ == '__main__':
    main()
