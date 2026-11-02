/* TEST-DASHBOARD_delta31 — im-10 « Hypersensibilité retardée (type IV) » retrouve son bouton.
   Usage : NODE_PATH=/tmp/seenmed-runtime/node_modules node TEST-DASHBOARD_delta31.cjs <site_dir> <pkg_medstudy_dir> <infra_dir>
   Pré-état attendu du bench : site de l'utilisateur après delta 30, avec la page im-10
   (lecons/im-10-hypersensibilite-retardee.html) présente sur disque (paquet AGENT-2 extrait).
   infra_dir (défaut /tmp/infra) : base-data.js (data.js base 28/10) · data-agent2-im10.js
   (le data.js du paquet medstudy-im-10 v2, 61 url).
   Scénarios :
     A1. état actuel (convergent delta 30 + data-merge v1) → 76 boutons, im-10 ABSENT (constat utilisateur reproduit)
     A2. delta 31 appliqué (data31 + data-merge v2 + patch im-10 + index) → 77, im-10 PRÉSENT, pneumo 12/12
     B.  data.js AGENT-2 (61 url) réécrasé sur l'infra delta 31 → toujours 77 (secours + patchs)
     C.  data.js BASE (60 url) écrasé sur l'infra delta 31 → toujours 77, im-10 présent
     D.  contrôle : C sans data-merge → 60, pneumo 0/12, im-10 absent (le test sait détecter)
   Restaure l'état A2 à la fin. */
const fs = require("fs"), path = require("path"), http = require("http");
const { JSDOM, ResourceLoader } = require("jsdom");

const SITE = process.argv[2];
const PKG = process.argv[3];
const INFRA = process.argv[4] || "/tmp/infra";
const DATA = path.join(SITE, "js/data.js");
const MERGE = path.join(SITE, "js/data-merge.js");
const INDEX = path.join(SITE, "index.html");
const BASE = fs.readFileSync(path.join(INFRA, "base-data.js"));
const AG2 = fs.readFileSync(path.join(INFRA, "data-agent2-im10.js"));
const D31_DATA = fs.readFileSync(path.join(PKG, "js/data.js"));
const D31_MERGE = fs.readFileSync(path.join(PKG, "js/data-merge.js"));
const D31_INDEX = fs.readFileSync(path.join(PKG, "index.html"));

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
    im10: links.some(h => h.includes("im-10-hypersensibilite-retardee.html")),
  };
  dom.window.close();
  return res;
}

let failures = 0;
function check(name, r, exp) {
  const ok = r.total === exp.total && r.pneumo === exp.pneumo && r.im11 === exp.im11 && r.sg04 === exp.sg04 && r.im10 === exp.im10;
  console.log(`${ok ? "✓" : "✗"} ${name} — total ${r.total}, pneumo ${r.pneumo}/12, im-11 ${r.im11}, sg-04 ${r.sg04}, im-10 ${r.im10}`);
  if (!ok) failures++;
}

(async () => {
  await new Promise(r => server.listen(0, "127.0.0.1", r));
  const pageExists = fs.existsSync(path.join(SITE, "lecons/im-10-hypersensibilite-retardee.html"));
  console.log(`${pageExists ? "✓" : "✗"} page im-10 présente sur le disque du bench`);
  if (!pageExists) failures++;

  // A1 : bench tel quel (delta 30) — im-10 doit être absente
  check("A1. état utilisateur actuel (delta 30)", await run(), { total: 76, pneumo: 12, im11: true, sg04: true, im10: false });

  // appliquer le delta 31
  fs.writeFileSync(DATA, D31_DATA);
  fs.writeFileSync(MERGE, D31_MERGE);
  fs.writeFileSync(INDEX, D31_INDEX);
  fs.mkdirSync(path.join(SITE, "js/data-patches"), { recursive: true });
  fs.copyFileSync(path.join(PKG, "js/data-patches/im-10.js"), path.join(SITE, "js/data-patches/im-10.js"));

  const FULL = { total: 77, pneumo: 12, im11: true, sg04: true, im10: true };
  check("A2. delta 31 appliqué", await run(), FULL);

  fs.writeFileSync(DATA, AG2);
  check("B. data AGENT-2 (61 url) réécrasé → secouru", await run(), FULL);

  fs.writeFileSync(DATA, BASE);
  check("C. data BASE (60 url) écrasé → secouru", await run(), FULL);

  fs.renameSync(MERGE, MERGE + ".off");
  check("D. contrôle sans data-merge (bug visible)", await run(), { total: 60, pneumo: 0, im11: false, sg04: false, im10: false });
  fs.renameSync(MERGE + ".off", MERGE);

  fs.writeFileSync(DATA, D31_DATA); // restaure A2
  server.close();
  console.log(failures === 0 ? "TOUT VERT (6/6)" : `ÉCHECS : ${failures}`);
  process.exit(failures === 0 ? 0 : 1);
})();
