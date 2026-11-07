#!/usr/bin/env python3
"""Dump structurel de pn-01 (châssis gold pneumologie) pour builder pn-08."""
import re, json

H = open('/tmp/site/medstudy/lecons/pn-01-dyspnee.html', encoding='utf-8').read()
OUT = open('/tmp/pn08/chassis-dump.txt', 'w', encoding='utf-8')

def show(title, txt, limit=4000):
    print(f"\n######## {title} ########")
    print(txt[:limit])
    OUT.write(f"\n######## {title} ########\n{txt}\n")

def section(idv):
    m = re.search(rf'<section[^>]*id="{idv}"[^>]*>', H)
    if not m: return f"(section {idv} introuvable)"
    start = m.start()
    nxt = H.find('<section', m.end())
    return H[start:nxt if nxt > 0 else len(H)]

def script_json(idv):
    m = re.search(rf'<script[^>]*id="{idv}"[^>]*>(.*?)</script>', H, re.S)
    return m.group(1) if m else None

# HEAD + body opening + navbar
head = H[:H.find('</head>') + 7]
show('HEAD', head)
body_open = H[H.find('<body'):H.find('<section')]
show('BODY OUVERTURE -> 1re section (navbar incluse)', body_open, 6000)

# Sections modèles
show('SECTION vue', section('vue'), 5000)
show('SECTION mindmap', section('mindmap'), 2500)
show('SECTION cine (coquille)', section('cine')[:3000], 3000)
show('SECTION nyha (Contenu type)', section('nyha'), 7000)
show('SECTION methode', section('methode'), 3500)
show('SECTION connexions', section('connexions'), 3500)

ann = section('annales')
qb = re.search(r'<div class="qblock.*?(?=<div class="qblock|</section>)', ann, re.S)
show('ANNALES: en-tête section (avant 1er qblock)', ann[:ann.find('<div class="qblock')], 3000)
show('ANNALES: 1er qblock complet', qb.group(0) if qb else '(?)', 4500)

show('SECTION fiche', section('fiche'), 6000)
show('SECTION flashcards (coquille)', section('flashcards'), 4000)
show('SECTION resume-total', section('resume-total'), 4000)

# Après la dernière section : footer + JSON + moteurs
last_sec_end = H.rfind('</section>')
show('APRES DERNIERE SECTION (footer->JSON->moteurs)', H[last_sec_end:], 5000)

# JSON : formats exacts
cine = json.loads(script_json('cineData'))
show('cineData clés + chapitre 0 + dernier', json.dumps(
    {'keys': list(cine.keys()), 'ch0': cine['chapitres'][0], 'ch_last': cine['chapitres'][-1],
     'n_chapitres': len(cine['chapitres'])}, ensure_ascii=False, indent=1), 3000)
kw = json.loads(script_json('kwData'))
show('kwData [0..2] + type', json.dumps({'type': type(kw).__name__, 'n': len(kw), 'items': kw[:3]}, ensure_ascii=False, indent=1), 2500)
fc = json.loads(script_json('fcData'))
fcl = fc if isinstance(fc, list) else fc.get('cartes') or fc.get('cards') or []
show('fcData structure + [0..1]', json.dumps({'type': type(fc).__name__, 'keys': (list(fc.keys()) if isinstance(fc, dict) else '-'),
     'n': len(fcl), 'items': fcl[:2]}, ensure_ascii=False, indent=1), 2500)
ar = json.loads(script_json('arData'))
keys = list(ar.keys())
show('arData: nb clés + échantillons', json.dumps({'n': len(keys), 'first_keys': keys[:12],
     'sample': {k: ar[k] for k in keys[:3]}}, ensure_ascii=False, indent=1), 3500)
qexp_keys = [k for k in keys if 'exp' in k]
if qexp_keys:
    k = qexp_keys[0]
    show(f'arData exemple qexp ({k})', str(ar[k])[:2500], 2500)

# data-tr patterns
trs = re.findall(r'data-tr="([^"]+)"', H)
show('data-tr: total + 25 premiers', f"total={len(trs)} uniques={len(set(trs))}\n" + "\n".join(trs[:25]), 2000)

# cine-spot pattern
spots = re.findall(r'<[^>]*cine-spot[^>]*>', H)
show('cine-spot (2 exemples)', "\n".join(spots[:2]) + f"\n... total {len(spots)}", 1500)

# figures/images pattern dans une section Contenu
imgs = re.findall(r'<img[^>]+>', section('nyha'))
show('img tags section nyha', "\n".join(imgs[:4]), 2000)
figs = re.findall(r'<figure.*?</figure>', section('examens'), re.S)
show('figure type (section examens)', figs[0] if figs else '(aucune figure)', 2000)

OUT.close()
print("\n>>> dump complet: /tmp/pn08/chassis-dump.txt")
