#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""PATCH-AUDIOS-AR-v3 — applique la règle audio du site à #cineData.

DÉCISION UTILISATEUR (30/10/2026, STANDARD-OR-v3 §4) : les chapitres du
Ciné sont en FRANÇAIS uniquement ; l'arabe n'existe que sur le chapitre
résumé (le dernier), en FR + AR. Ce script :
  - retire `ar` de tous les chapitres sauf le dernier,
  - câble le dernier sur `<fr>-ar.mp3` si le fichier existe (sinon garde
    la piste déjà déclarée, ex. resume-ar.mp3),
  - recalcule le sous-titre de la section #cine.
Usage : python3 PATCH-AUDIOS-AR-v3.py <page.html> [...]
Ensuite : AUDIT-LECON-GOLD-v3.py + RUNTIME-DOM-v3.test.cjs.
"""
import json, re, sys
from pathlib import Path

def lsub(chs):
    n = len(chs)
    if chs and chs[-1].get('ar'):
        return (f'Les planches défilent, la voix explique en reliant les idées : <b>{n-1} chapitres en français</b>, '
                'plus le <b>résumé total en français et en arabe (ع)</b>, vitesse réglable. Rien ne se lance sans ton clic.')
    return (f'Les planches défilent, la voix explique en reliant les idées : <b>{n-1} chapitres + le résumé, en français</b>, '
            'vitesse réglable. Rien ne se lance sans ton clic.')

for path in sys.argv[1:]:
    p = Path(path)
    s = p.read_text(encoding='utf-8')
    m = re.search(r'(<script type="application/json" id="cineData">)(.*?)(</script>)', s, re.S)
    assert m, f'cineData introuvable dans {path}'
    cine = json.loads(m.group(2))
    chs = cine['chapitres']
    unwired = 0
    for c in chs[:-1]:
        if c.get('ar'):
            c['ar'] = None; unwired += 1
    last = chs[-1]
    if not last.get('ar') and last.get('fr'):
        ar = re.sub(r'\.mp3(\?.*)?$', r'-ar.mp3\1', last['fr'])
        if (p.parent / ar.split('?')[0]).resolve().exists():
            last['ar'] = ar
    s = s[:m.start(2)] + json.dumps(cine, ensure_ascii=False, separators=(',', ':')) + s[m.end(2):]
    sec = re.search(r'(<section class="lsection" id="cine">.*?<div class="lsub">)(.*?)(</div>)', s, re.S)
    if sec:
        s = s[:sec.start(2)] + lsub(chs) + s[sec.end(2):]
    p.write_text(s, encoding='utf-8')
    print(f'{p.name} : {unwired} piste(s) AR de chapitre retirée(s) — résumé AR = {last.get("ar")}')
