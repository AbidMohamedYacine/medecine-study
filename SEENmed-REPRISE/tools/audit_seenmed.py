#!/usr/bin/env python3
"""SEENmed chain audit — verifies data.js <-> pages <-> assets as ONE chain.

Usage: python3 audit_seenmed.py /path/to/medstudy
Checks: (1) every data.js url resolves to an existing file, (2) every page
in lecons/ is reachable from a data.js url, (3) body[data-lesson-id]
matches the file id, (4) every local ../assets|css|js reference inside
each page exists on disk, (5) lists pages without an audio folder.
Requires node (to parse data.js faithfully). Exit code 1 if any check fails.
"""
import json, os, re, subprocess, sys

MS = os.path.abspath(sys.argv[1] if len(sys.argv) > 1 else "medstudy")
js = (
    "global.window={};"
    f"eval(require('fs').readFileSync({json.dumps(os.path.join(MS, 'js/data.js'))},'utf8'));"
    "const D=window.MED_DATA;const rows=[];"
    "for(const m of D.modules)for(const l of m.lecons)rows.push({module:m.id,...l});"
    "process.stdout.write(JSON.stringify(rows));"
)
rows = json.loads(subprocess.check_output(["node", "-e", js], text=True))
byid = {r["id"]: r for r in rows}
fails = 0

pages = []
for f in sorted(os.listdir(os.path.join(MS, "lecons"))):
    if f.endswith(".html"):
        pages.append((re.match(r"^([a-z]{2,3}-\d+)-", f).group(1), f,
                      os.path.join(MS, "lecons", f)))
print(f"pages: {len(pages)} | data.js entries: {len(rows)} | with url: "
      f"{sum(1 for r in rows if r.get('url'))}")

missing = [(r["id"], r["url"]) for r in rows
           if r.get("url") and not os.path.isfile(os.path.join(MS, r["url"]))]
print("urls -> missing files:", missing or "NONE"); fails += len(missing)

unreach = [(lid, f) for lid, f, _ in pages if not byid.get(lid, {}).get("url")]
print("unreachable pages:", unreach or "NONE"); fails += len(unreach)

def refs(html):
    out = set(re.findall(r'(?:src|href)="([^"#]+)"', html))
    out |= set(re.findall(r'"(\.\./assets/[^"]+)"', html))
    out |= set(re.findall(r'"(\.\./(?:css|js)/[^"]+)"', html))
    return {r.split("?")[0] for r in out
            if not r.startswith(("http", "mailto:", "data:"))}

total_broken = 0
for lid, _f, path in pages:
    h = open(path, encoding="utf-8", errors="ignore").read()
    m = re.search(r'data-lesson-id="([^"]+)"', h)
    body = m.group(1) if m else None
    if body != lid:
        print(f"BODY-ID MISMATCH {lid}: {body}"); fails += 1
    pagedir = os.path.dirname(path)
    broken = sorted(r for r in refs(h) if r.startswith("..")
                    and not os.path.exists(os.path.normpath(os.path.join(pagedir, r))))
    if broken:
        total_broken += len(broken)
        print(f"{lid}: {len(broken)} broken refs")
        for b in broken:
            print("   ", b)
fails += total_broken
print("TOTAL broken refs:", total_broken)
no_audio = [lid for lid, _, _ in pages
            if not os.path.isdir(os.path.join(MS, "assets/audio", lid))]
print(f"pages without audio folder ({len(no_audio)}):", ", ".join(no_audio))
sys.exit(1 if fails else 0)
