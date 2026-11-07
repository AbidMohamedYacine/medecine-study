#!/usr/bin/env Node
/* ============================================================================
   RUNTIME-SMOKE-v3 — test navigateur bloquant du STANDARD-OR-v3.
   L'audit statique (AUDIT-LECON-GOLD-v3.py) prouve que le HTML parle le
   langage des moteurs ; ce test prouve que les moteurs RÉPONDENT :
   QCM coché/corrigé/scoré, Ciné central + mini-lecteurs qui jouent,
   dictionnaire FR/AR, mode arabe, flashcards qui tournent et avancent,
   peau du module (canvas + 4 thèmes + 4 modes de fond).

   Prérequis (une fois) :
     mkdir -p /tmp/seenmed-runtime && cd /tmp/seenmed-runtime
     npm init -y && npm i puppeteer-core @sparticuz/chromium
   Usage :
     Node RUNTIME-SMOKE-v3.test.cjs <dossier-site> <page-relative> [autres pages…]
         [--shots <dossier-captures>] [--modes]
   Code de sortie 0 seulement si tout passe.
   ============================================================================ */
'use strict';
const fs = require('fs');
const path = require('path');
const http = require('http');

function req(name) {
  const roots = [process.env.SMOKE_RUNTIME_DIR, '/tmp/seenmed-runtime',
    process.cwd(), __dirname].filter(Boolean);
  for (const r of roots) {
    try { return require('module').createRequire(path.join(r, 'package.json'))(name); } catch (e) {}
  }
  try { return require(name); } catch (e) {}
  throw new Error('Module introuvable : ' + name + ' (voir prérequis en tête de fichier)');
}
const puppeteer = req('puppeteer-core');
const Chromium = req('@sparticuz/chromium');

const args = process.argv.slice(2);
let shotsDir = null, testModes = false;
const positional = [];
for (let i = 0; i < args.length; i++) {
  if (args[i] === '--shots') shotsDir = args[++i];
  else if (args[i] === '--modes') testModes = true;
  else positional.push(args[i]);
}
const siteDir = positional[0];
const pages = positional.slice(1);
if (!siteDir || !pages.length) { console.error('Usage: Node RUNTIME-SMOKE-v3.test.cjs <site> <page…> [--shots dir] [--modes]'); process.exit(2); }
if (shotsDir) fs.mkdirSync(shotsDir, { recursive: true });

const MIME = { '.html': 'text/html; charset=utf-8', '.css': 'text/css', '.js': 'text/javascript',
  '.json': 'application/json', '.webp': 'image/webp', '.png': 'image/png', '.jpg': 'image/jpeg',
  '.svg': 'image/svg+xml', '.mp3': 'audio/mpeg', '.woff2': 'font/woff2', '.woff': 'font/woff',
  '.ttf': 'font/ttf', '.ico': 'image/x-icon' };
const server = http.createServer((rq, rs) => {
  try {
    let p = decodeURIComponent(rq.url.split('?')[0]);
    if (p.endsWith('/')) p += 'index.html';
    const fp = path.join(siteDir, p);
    if (!fp.startsWith(path.resolve(siteDir)) || !fs.existsSync(fp)) { rs.writeHead(404); rs.end(); return; }
    rs.writeHead(200, { 'Content-Type': MIME[path.extname(fp)] || 'application/octet-stream' });
    fs.createReadStream(fp).pipe(rs);
  } catch (e) { rs.writeHead(500); rs.end(); }
});

const results = [];
function check(page, name, ok, detail) {
  results.push({ page, name, ok: !!ok, detail: detail || '' });
  console.log((ok ? '  ✓ ' : '  ✗ FAIL ') + name + (detail ? ' — ' + detail : ''));
}
const sleep = ms => new Promise(r => setTimeout(r, ms));

async function newPage(browser, preset) {
  const ctx = await browser.createBrowserContext();
  const page = await ctx.newPage();
  await page.setViewport({ width: 1440, height: 1000 });
  if (preset) await page.evaluateOnNewDocument(obj => {
    try { for (const k in obj) localStorage.setItem(k, obj[k]); } catch (e) {}
  }, preset);
  return { ctx, page };
}

async function runPage(browser, base, rel) {
  const name = path.basename(rel);
  console.log('\n=== ' + name + ' ===');
  const { ctx, page } = await newPage(browser);
  const errors = [], failed = [];
  page.on('pageerror', e => errors.push(String(e)));
  page.on('console', m => { if (m.type() === 'error') errors.push(m.text()); });
  page.on('response', r => { if (r.status() >= 400) failed.push(r.status() + ' ' + r.url().split('/').slice(-2).join('/')); });
  await page.goto(base + '/' + rel, { waitUntil: 'networkidle2', timeout: 90000 });
  await sleep(800);

  const lid = await page.evaluate(() => document.body.getAttribute('data-lesson-id') || '');
  const isPn = lid.startsWith('pn-');

  /* ---- QCM : cocher juste, corriger, verdict + correction + score ---- */
  try {
    const answers = await page.evaluate(() => JSON.parse(document.querySelector('#annales .qblock').getAttribute('data-answer')));
    await page.evaluate(() => document.querySelector('#annales .qblock').scrollIntoView());
    for (const l of answers) await page.click('#annales .qblock li[data-l="' + l + '"]');
    await page.click('#annales .qblock .qcheck');
    await sleep(400);
    const q = await page.evaluate(() => {
      const b = document.querySelector('#annales .qblock');
      const exp = b.querySelector('.qexp');
      return { answered: b.classList.contains('answered'),
        verdict: b.querySelector('.qverdict').textContent.trim(),
        verdictGood: b.querySelector('.qverdict').classList.contains('good'),
        expVisible: exp && getComputedStyle(exp).display !== 'none' && exp.offsetHeight > 0,
        nCorrect: b.querySelectorAll('li.correct').length,
        score: document.querySelector('#annales .qs-val').textContent.trim() };
    });
    check(name, 'QCM annales corrigé (answered + verdict bon)', q.answered && q.verdictGood, q.verdict);
    check(name, 'correction affichée après clic', q.expVisible);
    check(name, 'bonnes réponses coloriées', q.nCorrect === answers.length, q.nCorrect + '/' + answers.length);
    check(name, 'score de série mis à jour', q.score === '1 / 1', 'qs-val = ' + q.score);
  } catch (e) { check(name, 'QCM', false, String(e).slice(0, 200)); }

  /* ---- Ciné central + un mini-lecteur de section ---- */
  try {
    const cine = await page.evaluate(() => {
      const d = JSON.parse(document.getElementById('cineData').textContent);
      return { chapitres: d.chapitres.length,
        boutons: document.querySelectorAll('#cinePlayer .cine-chapitres > li, #cinePlayer .cine-chapitres button').length,
        spots: document.querySelectorAll('.cine-spot .cspot-play').length };
    });
    check(name, 'Ciné central monté (chapitres = JSON)', cine.boutons >= cine.chapitres, cine.boutons + ' boutons / ' + cine.chapitres);
    check(name, 'mini-lecteurs de section montés', cine.spots > 0, cine.spots + ' spots');
    await page.evaluate(() => document.querySelector('.cine-spot').scrollIntoView({ block: 'center' }));
    await sleep(300);
    await page.click('.cine-spot .cspot-play');
    await sleep(1800);
    const playing = await page.evaluate(() => document.querySelector('.cine-spot').classList.contains('on'));
    check(name, 'mini-lecteur : lecture audio réelle', playing);
    await page.click('.cine-spot .cspot-play'); await sleep(300);
    await page.evaluate(() => document.querySelector('#cinePlayer').scrollIntoView({ block: 'center' }));
    await sleep(300);
    await page.click('#cinePlayer .cine-bigplay');
    await sleep(1800);
    const central = await page.evaluate(() => !!document.querySelector('#cinePlayer .cine-wrap.playing'));
    check(name, 'Ciné central : lecture audio réelle', central);
    await page.click('#cinePlayer .cine-play'); await sleep(200);
  } catch (e) { check(name, 'Ciné', false, String(e).slice(0, 200)); }

  /* ---- Mots-clés : panneau, comptage, bascule arabe ---- */
  try {
    const kwN = await page.evaluate(() => JSON.parse(document.getElementById('kwData').textContent).length);
    await page.click('#kwHandle'); await sleep(500);
    const kw = await page.evaluate(() => ({ open: document.getElementById('kwPanel').classList.contains('open'),
      items: document.querySelectorAll('#kwPanel .kw-list > li').length }));
    check(name, 'dictionnaire ouvert, tous les termes rendus', kw.open && kw.items === kwN, kw.items + '/' + kwN);
    await page.click('#kwPanel .kw-lang'); await sleep(300);
    const arDef = await page.evaluate(() => { const d = document.querySelector('#kwPanel .kw-def'); return d && (d.getAttribute('dir') === 'rtl' || d.classList.contains('ar')); });
    check(name, 'définitions arabes du dictionnaire', arDef);
    await page.click('#kwPanel .kw-close'); await sleep(300);
  } catch (e) { check(name, 'Mots-clés', false, String(e).slice(0, 200)); }

  /* ---- Mode arabe global ---- */
  try {
    const before = await page.evaluate(() => document.querySelector('[data-tr]').textContent.slice(0, 40));
    await page.click('.ar-toggle'); await sleep(400);
    const ar = await page.evaluate(() => { const el = document.querySelector('[data-tr]'); return { txt: el.textContent.slice(0, 40), rtl: el.getAttribute('dir') === 'rtl' }; });
    check(name, 'mode arabe : blocs traduits + RTL', ar.rtl && ar.txt !== before);
    await page.click('.ar-toggle'); await sleep(300);
  } catch (e) { check(name, 'Mode arabe', false, String(e).slice(0, 200)); }

  /* ---- Flashcards : première carte, flip, notation, avance ---- */
  try {
    await page.evaluate(() => document.getElementById('fcDeck').scrollIntoView({ block: 'center' }));
    await sleep(300);
    const fc1 = await page.evaluate(() => ({ q: document.querySelector('#fcFront .fc-q') ? document.querySelector('#fcFront .fc-q').textContent.slice(0, 40) : '',
      count: document.getElementById('fcCount').textContent.trim() }));
    check(name, 'flashcards : première carte affichée', !!fc1.q, fc1.count);
    await page.click('#fcCard'); await sleep(400);
    const flipped = await page.evaluate(() => document.getElementById('fcCard').classList.contains('flipped'));
    check(name, 'flashcards : flip au clic', flipped);
    await page.click('#fcGood'); await sleep(400);
    const fc2 = await page.evaluate(() => document.getElementById('fcCount').textContent.trim());
    check(name, 'flashcards : notation → carte suivante', /2/.test(fc2), fc2);
  } catch (e) { check(name, 'Flashcards', false, String(e).slice(0, 200)); }

  /* ---- Peau du module : canvas, particules, thèmes ---- */
  try {
    if (isPn) {
      const field = await page.evaluate(() => ({ canvas: !!document.getElementById('pneumoFieldCanvas'),
        count: window.__pneumoField ? window.__pneumoField.count() : -1,
        root: document.documentElement.classList.contains('pneumo-root') }));
      check(name, 'peau pneumo : canvas + champ de particules + racine', field.canvas && field.count > 50 && field.root, field.count + ' particules');
      const expected = { dark: '#35d0ff', light: '#087ea4', aurora: '#a78bfa', ocean: '#2dd4bf' };
      for (const t of ['dark', 'light', 'aurora', 'ocean']) {
        const got = await page.evaluate(th => { document.documentElement.setAttribute('data-theme', th);
          return new Promise(res => setTimeout(() => res({ blue: getComputedStyle(document.body).getPropertyValue('--blue').trim().toLowerCase(),
            col: window.__pneumoField ? window.__pneumoField.colors.main.join(',') : '' }), 250)); }, t);
        check(name, 'thème ' + t + ' : identité pneumo appliquée', got.blue === expected[t], '--blue=' + got.blue + ' champ=' + got.col);
      }
    } else {
      const field = await page.evaluate(() => ({ canvas: !!document.getElementById('bioFieldCanvas'),
        count: window.__heroField ? window.__heroField.count() : -1 }));
      check(name, 'peau bio : canvas présent et champ vivant', field.canvas && field.count > 50, field.count + ' particules');
    }
  } catch (e) { check(name, 'Peau/thèmes', false, String(e).slice(0, 200)); }

  check(name, 'aucune erreur JS', errors.length === 0, errors.slice(0, 3).join(' | ').slice(0, 220));
  const media404 = failed.filter(f => /\.(mp3|webp)/.test(f));
  check(name, 'aucun asset 404 (hors banc incomplet toléré si listé)', failed.length === 0, failed.slice(0, 5).join(' | ').slice(0, 220));

  if (shotsDir) {
    await page.evaluate(() => { document.documentElement.setAttribute('data-theme', 'dark'); window.scrollTo(0, 0); });
    await sleep(600);
    await page.screenshot({ path: path.join(shotsDir, name + '-1-top.png') });
    await page.evaluate(() => document.querySelector('#cinePlayer').scrollIntoView());
    await sleep(600);
    await page.screenshot({ path: path.join(shotsDir, name + '-2-cine.png') });
    await page.evaluate(() => document.querySelector('#annales .qblock').scrollIntoView());
    await sleep(600);
    await page.screenshot({ path: path.join(shotsDir, name + '-3-QCM.png') });
    await page.evaluate(() => document.querySelector('#fiche .flashsheet').scrollIntoView());
    await sleep(600);
    await page.screenshot({ path: path.join(shotsDir, name + '-4-fiche.png') });
    if (isPn) {
      for (const t of ['light', 'aurora', 'ocean']) {
        await page.evaluate(th => { document.documentElement.setAttribute('data-theme', th); window.scrollTo(0, 0); }, t);
        await sleep(600);
        await page.screenshot({ path: path.join(shotsDir, name + '-theme-' + t + '.png') });
      }
    }
  }
  await ctx.close();
}

async function runModes(browser, base, rel) {
  const name = path.basename(rel);
  console.log('\n=== MODES DE FOND — ' + name + ' ===');
  for (const mode of ['anime', 'eco', 'photo', 'planche']) {
    const { ctx, page } = await newPage(browser, { 'seenmed-fond': mode });
    const errors = [];
    page.on('pageerror', e => errors.push(String(e)));
    await page.goto(base + '/' + rel, { waitUntil: 'networkidle2', timeout: 90000 });
    await sleep(1200);
    let detail = '';
    let ok = await page.evaluate(m => document.body.getAttribute('data-fond') === m && window.SEENBG && window.SEENBG.mode === m, mode);
    if (mode === 'planche') {
      const p = await page.evaluate(() => ({ fixe: document.body.classList.contains('fond-fixe'),
        planche: getComputedStyle(document.documentElement).getPropertyValue('--planche') ||
          (document.querySelector('.bg-layer, .fond-couche') ? getComputedStyle(document.querySelector('.bg-layer, .fond-couche')).getPropertyValue('--planche') : '') }));
      ok = ok && p.fixe; detail = 'fond-fixe=' + p.fixe;
    } else if (mode === 'photo') {
      try { await page.waitForFunction(() => document.body.classList.contains('fond-photo-pris'), { timeout: 25000 }); detail = 'photo prise'; }
      catch (e) { ok = false; detail = 'photo jamais prise (25 s)'; }
    } else {
      const c = await page.evaluate(() => window.__pneumoField ? window.__pneumoField.count() : (window.__heroField ? window.__heroField.count() : -1));
      ok = ok && c > 50; detail = c + ' particules';
    }
    check(name, 'mode ' + mode, ok && errors.length === 0, detail + (errors.length ? ' | ' + errors[0].slice(0, 120) : ''));
    await ctx.close();
  }
}

(async () => {
  await new Promise(r => server.listen(0, '127.0.0.1', r));
  const base = 'http://127.0.0.1:' + server.address().port;
  const CH = Chromium.default || Chromium;
  const browser = await puppeteer.launch({
    args: [...(CH.args || []), '--autoplay-policy=no-user-gesture-required', '--mute-audio'],
    executablePath: await CH.executablePath(), headless: true });
  try {
    for (const p of pages) await runPage(browser, base, p);
    if (testModes) await runModes(browser, base, pages[0]);
  } finally { await browser.close(); server.close(); }
  const fails = results.filter(r => !r.ok);
  console.log('\n================ ' + (results.length - fails.length) + '/' + results.length + ' checks OK' +
    (fails.length ? ' — ÉCHECS : ' + fails.map(f => f.page + ':' + f.name).join(' ; ') : ' — TOUT PASSE'));
  process.exit(fails.length ? 1 : 0);
})().catch(e => { console.error(e); process.exit(2); });
