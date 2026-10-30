#!/usr/bin/env python3
"""Assemble le site SEENmed dans /tmp/site.
Recette complète (vérifiée 30/10) : base 4 parties -> livraisons 01..05
-> js/data.js := data_COURANT apres-pn04 -> deltas 06,08,09,10,11,12.
Normalise les racines de ZIP (medstudy/ direct, emballé, ou sans préfixe)."""
import zipfile, os, shutil

Z = '/tmp/zips'
OUT = '/tmp/site'
STAGING = '/home/user/medecine-study/google_drive'
DATA_COURANT = os.path.join(STAGING, 'data_COURANT_2026-10-29_apres-pn04.js')

def move_staged():
    for f in os.listdir(STAGING):
        if f.endswith('.zip'):
            shutil.move(os.path.join(STAGING, f), os.path.join(Z, f))
            print('staged ->', f)

KNOWN_ROOTS = ('lecons/', 'assets/', 'css/', 'js/')

def normalize(name):
    if 'medstudy/' in name:
        return name[name.find('medstudy/'):]
    parts = name.split('/')
    for i, seg in enumerate(parts[:-1]):
        if seg + '/' in KNOWN_ROOTS:
            return 'medstudy/' + '/'.join(parts[i:])
    if parts[-1] == 'index.html' and len(parts) <= 2:
        return 'medstudy/index.html'
    return None

def overlay(zipname):
    path = os.path.join(Z, zipname)
    n = skipped = 0
    with zipfile.ZipFile(path) as z:
        for info in z.infolist():
            if info.filename.endswith('/'):
                continue
            rel = normalize(info.filename)
            if rel is None:
                skipped += 1
                continue
            dest = os.path.join(OUT, rel)
            os.makedirs(os.path.dirname(dest), exist_ok=True)
            with z.open(info) as src, open(dest, 'wb') as dst:
                shutil.copyfileobj(src, dst)
            n += 1
    print(f'{zipname}: {n} appliqués, {skipped} ignorés (hors site)')

move_staged()
if os.path.exists(OUT):
    shutil.rmtree(OUT)
os.makedirs(OUT)

STEPS = [
    'SEENmed-BASE-PROPRE-2026-10-28_part1-of4.zip',
    'SEENmed-BASE-PROPRE-2026-10-28_part2-of4.zip',
    'SEENmed-BASE-PROPRE-2026-10-28_part3-of4.zip',
    'SEENmed-BASE-PROPRE-2026-10-28_part4-of4.zip',
    'bi05-livraison-2026-10-28.zip',           # 01
    'SEENmed_DELTA-bi-06_2026-10-29.zip',      # 02
    'SEENmed_DELTA-bi06-final_2026-10-29.zip', # 03
    'SEENmed_DELTA-pn-01_2026-10-29.zip',      # 04
    'SEENmed_DELTA-pn-04_2026-10-29.zip',      # 05
    '__DATA_COURANT__',
    'SEENmed_PATCH-CONTRATS-v3_phase1_2026-10-30.zip',   # 06
    'SEENmed_DELTA08_pn-04-regle-audio_2026-10-30.zip',  # 08
    'SEENmed_DELTA09_resumes-longs_2026-10-30.zip',      # 09
    'SEENmed_DELTA10_phase2-lot1_2026-10-30.zip',        # 10
    'SEENmed_DELTA11_ff-style-realiste_2026-10-30.zip',  # 11
    'SEENmed_DELTA12_pn01-ff-nyha_2026-10-30.zip',       # 12
]

for s in STEPS:
    if s == '__DATA_COURANT__':
        shutil.copyfile(DATA_COURANT, os.path.join(OUT, 'medstudy', 'js', 'data.js'))
        print('js/data.js := data_COURANT_2026-10-29_apres-pn04.js')
    else:
        overlay(s)
    if s.endswith('part4-of4.zip'):
        cnt = sum(len(f) for _, _, f in os.walk(os.path.join(OUT, 'medstudy')))
        print(f'>>> base seule : {cnt} fichiers (attendu 2104)')

cnt = sum(len(f) for _, _, f in os.walk(os.path.join(OUT, 'medstudy')))
print(f'>>> TOTAL assemblé : {cnt} fichiers')
for p in ['index.html', 'js/data.js', 'lecons/ca-02-douleurs-thoraciques.html',
          'lecons/pn-01-dyspnee.html', 'assets/audio/pn-01/ch1.mp3',
          'assets/img/pn-01/hero.webp']:
    print(('OK  ' if os.path.exists(os.path.join(OUT, 'medstudy', p)) else 'ABSENT '), p)
