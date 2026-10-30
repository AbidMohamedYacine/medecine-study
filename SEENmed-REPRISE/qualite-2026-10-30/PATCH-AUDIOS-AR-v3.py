#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""PATCH-AUDIOS-AR-v3 — câble les pistes arabes du Ciné déjà générées.

Pour chaque chapitre de #cineData sans `ar`, dérive le nom `<fr>-ar.mp3` ;
si le fichier existe sur le disque (relativement à la page), il est câblé.
Recalcule ensuite le sous-titre de la section #cine (FR seul / résumé AR /
FR+AR partout). Usage : python3 PATCH-AUDIOS-AR-v3.py <page.html> [...]
Ensuite : AUDIT-LECON-GOLD-v3.py + RUNTIME-DOM-v3.test.cjs.
"""
import json, re, sys
from pathlib import Path

def lsub(chs):
    n = len(chs); n_ar = sum(1 for c in chs if c.get('ar'))
    if n_ar == n:
        return (f'Les planches défilent, la voix explique en reliant les idées : <b>{n-1} chapitres + le résumé</b>, '
                'piste <b>française ou arabe (ع)</b>, vitesse réglable. Rien ne se lance sans ton clic.')
    if n_ar:
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
    wired = 0
    for c in cine['chapitres']:
        if c.get('ar') or not c.get('fr'):
            continue
        ar = re.sub(r'\.mp3(\?.*)?$', r'-ar.mp3\1', c['fr'])
        if (p.parent / ar.split('?')[0]).resolve().exists():
            c['ar'] = ar; wired += 1
    s = s[:m.start(2)] + json.dumps(cine, ensure_ascii=False, separators=(',', ':')) + s[m.end(2):]
    # sous-titre de la section #cine
    sec = re.search(r'(<section class="lsection" id="cine">.*?<div class="lsub">)(.*?)(</div>)', s, re.S)
    if sec:
        s = s[:sec.start(2)] + lsub(cine['chapitres']) + s[sec.end(2):]
    p.write_text(s, encoding='utf-8')
    n_ar = sum(1 for c in cine['chapitres'] if c.get('ar'))
    print(f'{p.name} : {wired} piste(s) AR câblée(s) — {n_ar}/{len(cine["chapitres"])} chapitres avec AR')
