/* Usage: NODE_PATH=<playwright-core+pngjs+chromium> node TEST-fond-pneumo.cjs <base URL> <chromium executable>
   The site supplied by the caller must contain the 12 real pn pages and the new JS.
   Serve once with base CSS (no pneumo rule), once with CSS containing the rule. */
const assert = require('assert');
const { chromium } = require('playwright-core');
const { PNG } = require('pngjs');
const [base, executablePath] = process.argv.slice(2);
if (!base || !executablePath) throw Error('URL and Chromium executable required');
const names = [
'pn-01-dyspnee.html','pn-02-douleurs-thoraciques.html','pn-03-semiologie-de-la-toux.html',
'pn-04-expectoration.html','pn-05-hemoptysie.html','pn-06-dysphonie.html',
'pn-07-signes-physiques.html','pn-08-syndromes-mediastinaux.html','pn-09-syndromes-pulmonaires.html',
'pn-10-syndromes-bronchiques.html','pn-11-syndromes-pleuraux.html','pn-12-ponction-pleurale.html'];
function changed(a,b) { const x=PNG.sync.read(a), y=PNG.sync.read(b);let count=0;for(let i=0;i<x.data.length;i+=4){if(Math.max(...[0,1,2].map(j=>Math.abs(x.data[i+j]-y.data[i+j])))>8)count++;}return count; }
(async()=>{
 let browser=await chromium.launch({executablePath, headless:true,args:['--no-sandbox','--single-process','--no-zygote']});
 let page=await browser.newPage({viewport:{width:1440,height:850},reducedMotion:'reduce'});
 await page.addInitScript(()=>localStorage.setItem('seenmed-fond','eco'));
 for(const name of names){
  await page.goto(`${base}/lecons/${name}`,{waitUntil:'domcontentloaded'}); await page.waitForTimeout(350);
  const initial=await page.evaluate(()=>{const c=document.querySelector('#pneumoFieldCanvas');return {pos:getComputedStyle(c).position,hero:document.querySelector('.lesson-hero').getBoundingClientRect().top,pe:getComputedStyle(c).pointerEvents,mode:SEENBG.mode};});
  assert.equal(initial.pos,'fixed',`${name}: canvas is not fixed`);assert(initial.hero<250,`initial=${JSON.stringify(initial)} `+`${name}: canvas left a gap`);assert.equal(initial.pe,'none');
  for(const where of [.12,.55,.95]) {
   await page.evaluate(x=>window.scrollTo({top:(document.documentElement.scrollHeight-innerHeight)*x,behavior:'instant'}),where);
   await page.waitForTimeout(180);
   const v=await page.evaluate(()=>{const c=document.querySelector('#pneumoFieldCanvas');const d=c.getContext('2d').getImageData(0,0,c.width,c.height).data;let n=0;for(let i=3;i<d.length;i+=4)if(d[i])n++;return {top:c.getBoundingClientRect().top,pixels:n,height:c.getBoundingClientRect().height}});
   assert(Math.abs(v.top)<1 && v.height>=800,`${name}: canvas moved on scroll`);assert(v.pixels>100,`${name}: empty field at ${where}`);
  }
  console.log('PASS',name,'fixed, no gap, painted at 12/55/95%');
 }
 // Fresh browser avoids previous page scroll restoration and resource interference.
 await browser.close();
 browser=await chromium.launch({executablePath, headless:true,args:['--no-sandbox','--single-process','--no-zygote']});
 page=await browser.newPage({viewport:{width:1440,height:850},reducedMotion:'reduce'});
 await page.addInitScript(()=>localStorage.setItem('seenmed-fond','eco'));
 // Pixel comparison proves compositing, not merely that the canvas buffer is painted.
 await page.goto(`${base}/lecons/pn-03-semiologie-de-la-toux.html`);await page.waitForTimeout(3000);
 await page.evaluate(()=>scrollTo({top:2000,behavior:'instant'}));await page.waitForTimeout(800);
 for(const t of ['dark','light','aurora','ocean']){
  await page.evaluate(t=>document.documentElement.dataset.theme=t,t);
  await page.evaluate(()=>scrollTo({top:2000,behavior:'instant'}));await page.waitForTimeout(800);
  await page.waitForTimeout(150);
  const visible=await page.screenshot();await page.evaluate(()=>document.querySelector('#pneumoFieldCanvas').style.visibility='hidden');
  await page.waitForTimeout(150);
  const hidden=await page.screenshot();await page.evaluate(()=>document.querySelector('#pneumoFieldCanvas').style.visibility='visible');
  await page.waitForTimeout(150);
  const n=changed(visible,hidden);assert(n>100,`${t}: canvas is not visibly composited (${n} pixels)`);console.log('PASS pn-03 theme',t,'visible pixels:',n);
 }
 // Buttons remain hit-testable above the non-interactive canvas.
 const hit=await page.locator('button.bg-toggle').evaluate(el=>{const r=el.getBoundingClientRect();return document.elementFromPoint(r.left+r.width/2,r.top+r.height/2)?.closest('button')===el});assert(hit,'background blocks navbar');
 await page.locator('button.bg-toggle').click();assert.equal(await page.locator('button.bg-toggle').getAttribute('aria-expanded'),'true');console.log('PASS navbar remains clickable');
 await browser.close();
})().catch(e=>{console.error(e);process.exit(1)});
