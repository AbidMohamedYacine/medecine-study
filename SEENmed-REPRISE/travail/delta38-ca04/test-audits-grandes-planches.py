#!/usr/bin/env python3
"""Tests négatifs des contrôles adaptés. Usage : python test-audits-grandes-planches.py /tmp/.../medstudy.
Le site et les fichiers temporaires sont supprimés individuellement après le test.
"""
import subprocess, sys, tempfile
from pathlib import Path
from PIL import Image

root = Path(sys.argv[1]).resolve()
assert str(root).startswith('/tmp/')
lesson = root / 'lecons/ca-04-pression-arterielle.html'
original = lesson.read_text()
here = Path(__file__).resolve().parent
tools = [here/'AUDIT-LECON-GOLD-v3-grandes-planches.py', here/'OUTIL-verifier-images-grandes-planches.py']
img = root/'assets/img/ca-04-delta36/__test-petite-planche.webp'
Image.new('RGB',(100,100),'white').save(img,'WEBP')
corrupt = root/'assets/img/ca-04-delta36/__test-corrompue.webp'
corrupt.write_bytes(b'not an image')
needle='data-large-planche="true" src="../assets/img/ca-04-delta36/resume38-1.webp"'
assert original.count(needle)==1
small=original.replace(needle,'data-large-planche="true" src="../assets/img/ca-04-delta36/__test-petite-planche.webp"').replace('width="1024" height="1536"','width="100" height="100"',1)
cases={'normal':original,
       'non declare':original.replace(needle,needle.replace('data-large-planche="true" ','')),
       'dimensions incorrectes':original.replace('width="1024" height="1536"','width="1024" height="1000"',1),
       'insuffisante':small,
       'absente':original.replace(needle,needle.replace('resume38-1.webp','__introuvable.webp')),
       'corrompue':original.replace(needle,needle.replace('resume38-1.webp','__test-corrompue.webp'))}
try:
    for name,content in cases.items():
        with tempfile.NamedTemporaryFile('w',suffix='.html',prefix='ca-04-test-',dir=root/'lecons',encoding='utf-8',delete=False) as tmp:
            tmp.write(content); path=Path(tmp.name)
        try:
            for tool in tools:
                cmd=[sys.executable,str(tool)]
                if 'AUDIT-' in tool.name: cmd+=['--strict-gold']
                run=subprocess.run(cmd+[str(root),str(path)],capture_output=True,text=True)
                expect=0 if name=='normal' else 1
                if run.returncode!=expect:
                    raise AssertionError(f'{name} {tool.name}: attendu {expect}, reçu {run.returncode}\n{run.stdout}\n{run.stderr}')
                print(f'OK {name} / {tool.name}: code {run.returncode}')
        finally: path.unlink()
finally:
    img.unlink()
    corrupt.unlink()
