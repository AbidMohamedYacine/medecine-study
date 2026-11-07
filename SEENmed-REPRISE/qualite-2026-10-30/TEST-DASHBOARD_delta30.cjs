/* TEST-DASHBOARD_delta30 — le tableau de bord survit à un data.js périmé.
   Usage : NODE_PATH=/tmp/seenmed-runtime/node_modules node TEST-DASHBOARD_delta30.cjs <site_dir> [infra_dir]
   infra_dir (défaut /tmp/infra) doit contenir :
     base-data.js (data.js de la base 28/10) · data_COURANT_2026-11-01_convergent-total-delta30.js
   et le dossier google_drive du repo le data fork sg04 (chemin codé ci-dessous, ajuster si besoin).
   Scénarios (swap du fichier js/data.js du bench entre chaque run) :
     A. data convergent total        → pneumo 12/12, total 76, im-11 + sg-04 présents
     B. data.js de la BASE 28/10     → MÊME résultat (secours synchrone) ← le bug utilisateur 01/11
     C. data fork sg04 (sans im-11)  → im-11 présent, pneumo 12/12, total 76
     D. contrôle : B sans data-merge → pneumo 0/12 (reproduit le bug : le test sait détecter)
     E. couche patchs : un patch de leçon (pn-01 qcm 999) fait foi sur data de base
   Restaure l'état A à la fin. */
const fs = require("fs"), path = require("path"), http = require("http");
const { JSDOM, ResourceLoader } = require("jsdom");

const SITE = process.argv[2];
const INFRA = process.argv[3] || "/tmp/infra";
const DATA = path.join(SITE, "js/data.js");
const MERGE = path.join(SITE, "js/data-merge.js");
const CONV = fs.readFileSync(path.join(INFRA, "data_COURANT_2026-11-01_convergent-total-delta30.js"));
const BASE = fs.readFileSync(path.join(INFRA, "base-data.js"));
const SG04 = fs.readFileSync("/home/user/medecine-study/google_drive/data_COURANT_2026-11-01_apres-sg04-delta25.js");

const MIME = { ".html": "text/html", ".js": "text/javascript", ".css": "text/css", ".webp": "image/webp", ".png": "image/png", ".svg": "image/svg+xml", ".woff2": "font/woff2", ".json": "application/json" };
const server = http.createServer((req, res) => {
  const p = path.join(SITE, decodeURIComponent(req.url.split("?")[0]));
  fs.readFile(p, (err, buf) => {
    if (err) { res.writeHead(404); res.end(); return; }
    res.writeHead(200, { "Content-Type": MIME[path.extname(p)] || "application/octet-stream" });
    res.end(buf);
  });
});

async function loadDom() {
  const dom = await JSDOM.fromURL(`http://127.0.0.1:${server.address().port}/index.html`, {
    resources: new ResourceLoader({ userAgent: "jsdom-test" }),
    runScripts: "dangerously", pretendToBeVisual: true,
  });
  await new Promise(r => { dom.window.addEventListener("load", () => setTimeout(r, 800)); setTimeout(r, 15000); });
  return dom;
}
async function run() {
  const dom = await loadDom();
  const links = [...dom.window.document.querySelectorAll("a.lrow-link.ready")].map(a => a.getAttribute("href"));
  const res = {
    total: links.length,
    pneumo: links.filter(h => /\/pn-\d/.test(h)).length,
    im11: links.some(h => h.includes("im-11-deficits")),
    sg04: links.some(h => h.includes("sg-04-troubles")),
  };
  dom.window.close();
  return res;
}

let failures = 0;
function check(name, r, exp) {
  const ok = r.total === exp.total && r.pneumo === exp.pneumo && r.im11 === exp.im11 && r.sg04 === exp.sg04;
  console.log(`${ok ? "✓" : "✗"} ${name} — total ${r.total}, pneumo ${r.pneumo}/12, im-11 ${r.im11}, sg-04 ${r.sg04}`);
  if (!ok) failures++;
}

(async () => {
  await new Promise(r => server.listen(0, "127.0.0.1", r));
  const FULL = { total: 76, pneumo: 12, im11: true, sg04: true };

  fs.writeFileSync(DATA, CONV);
  check("A. data convergent total", await run(), FULL);

  fs.writeFileSync(DATA, BASE);
  check("B. data BASE écrasé (le bug) → secouru", await run(), FULL);

  fs.writeFileSync(DATA, SG04);
  check("C. data fork sg04 (sans im-11) → complété", await run(), FULL);

  fs.writeFileSync(DATA, BASE);
  fs.renameSync(MERGE, MERGE + ".off");
  check("D. contrôle sans data-merge (bug visible)", await run(), { total: 60, pneumo: 0, im11: false, sg04: false });

  fs.renameSync(MERGE + ".off", MERGE);

  // E. Couche patchs (leçons futures) : un patch de leçon fait foi, même sur data de base.
  const P01 = path.join(SITE, "js/data-patches/pn-01.js");
  const p01bak = fs.readFileSync(P01);
  fs.writeFileSync(P01, "window.MED_DATA_PATCHES = window.MED_DATA_PATCHES || [];\n" +
    "window.MED_DATA_PATCHES.push({\"id\":\"pn-01\",\"url\":\"lecons/pn-01-dyspnee.html\",\"recu\":true,\"qcm\":999,\"entr\":20});\n");
  fs.writeFileSync(DATA, BASE);
  {
    const dom = await loadDom();
    const pn01 = dom.window.MED_DATA.modules.flatMap(m => m.lecons).find(l => l.id === "pn-01");
    const ok = pn01.qcm === 999 && pn01.url === "lecons/pn-01-dyspnee.html";
    console.log(`${ok ? "✓" : "✗"} E. patch de leçon prioritaire (qcm 999 appliqué, url secourue)`);
    if (!ok) failures++;
    dom.window.close();
  }
  fs.writeFileSync(P01, p01bak);
  fs.writeFileSync(DATA, CONV);
  server.close();
  console.log(failures === 0 ? "\n================ TEST DASHBOARD : TOUT PASSE (5/5)" : `\n================ ${failures} ÉCHEC(S)`);
  process.exit(failures ? 1 : 0);
})().catch(e => { console.error(e); process.exit(2); });
