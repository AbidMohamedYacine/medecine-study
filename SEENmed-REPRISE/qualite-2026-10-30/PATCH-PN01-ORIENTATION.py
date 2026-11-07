#!/usr/bin/env python3
"""
PATCH-PN01-ORIENTATION.py — pn-01 (dyspnée) : chapitre Ciné dédié à la section
« orientation » (elle n'avait aucun spot ; sa planche était rangée dans le
chapitre Gravité). Phase 2 du patch qualité v3, 2026-10-30.

Effets sur la page :
  1. Insertion d'un chapitre FR à l'index 6 de cineData :
     "Chapitre 7 — Les signes d'orientation : chercher la cause"
     (imgs = orientation.webp ; fr = ../assets/audio/pn-01/orientation.mp3 ; ar = null,
      règle audio : chapitres FR uniquement).
  2. Renumérotation des titres suivants (Gravité 7->8, Examens 8->9) et retrait
     d'orientation.webp des images du chapitre Gravité.
  3. Décalage +1 des spots data-ch >= 6 ; ajout du spot data-ch="6" dans la
     section orientation, juste après sa planche.
  4. Sous-titre Ciné : « 8 chapitres » -> « 9 chapitres ».
Le script d'orientation est archivé dans audio-scripts-RESUMES-LONGS_phase2.md.
Usage : python3 PATCH-PN01-ORIENTATION.py <page pn-01>
"""
import re
import sys
import json

p = sys.argv[1]
h = open(p, encoding='utf-8').read()

# --- 1+2. cineData ---
m = re.search(r'(<script type="application/json" id="cineData">)(.*?)(</script>)', h, re.S)
cj = json.loads(m.group(2))
chs = cj['chapitres']
assert len(chs) == 9 and 'Gravité' in chs[6]['t'] and 'Examens' in chs[7]['t'], 'structure inattendue'
new_ch = {
    "t": "Chapitre 7 — Les signes d'orientation : chercher la cause",
    "imgs": ["../assets/img/pn-01/orientation.webp"],
    "fr": "../assets/audio/pn-01/orientation.mp3",
    "ar": None,
}
chs[6]['imgs'] = [i for i in chs[6]['imgs'] if 'orientation.webp' not in i]
chs[6]['t'] = chs[6]['t'].replace('Chapitre 7', 'Chapitre 8')
chs[7]['t'] = chs[7]['t'].replace('Chapitre 8', 'Chapitre 9')
chs.insert(6, new_ch)
assert all(c.get('ar') is None for c in chs[:-1]) and chs[-1].get('ar'), 'règle audio violée'
h = h[:m.start(2)] + json.dumps(cj, ensure_ascii=False) + h[m.end(2):]

# --- 3. spots : décalage (ordre décroissant via placeholders) ---
for old, new in [(8, 9), (7, 8), (6, 7)]:
    h = h.replace(f'cine-spot reveal" data-ch="{old}"', f'cine-spot reveal" data-ch="§{new}"')
h = h.replace('data-ch="§', 'data-ch="')
i = h.find('id="orientation"')
j = h.find('</figure>', i)
assert i > 0 and j > i
h = h[:j + len('</figure>')] + '<div class="cine-spot reveal" data-ch="6"></div>' + h[j + len('</figure>'):]

# --- 4. sous-titre Ciné ---
assert '<b>8 chapitres en' in h
h = h.replace('<b>8 chapitres en', '<b>9 chapitres en')

open(p, 'w', encoding='utf-8').write(h)

# --- vérifications ---
cj2 = json.loads(re.search(r'id="cineData">(.*?)</script>', h, re.S).group(1))
print('chapitres:', len(cj2['chapitres']))
for k, c in enumerate(cj2['chapitres']):
    print(' ', k, c['t'], '| ar:', c.get('ar'))
for s in re.split(r'<section class="lsection" id="', h)[1:]:
    sid = s.split('"', 1)[0]
    sp = re.findall(r'cine-spot[^>]*data-ch="(\d+)"', s.split('</section>')[0])
    if sp:
        print(f'  spot {sid} -> {sp}')
print('OK')
