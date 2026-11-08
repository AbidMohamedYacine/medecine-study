// Teste le site temporaire servi sur 8096 ; Chromium et playwright-core requis.
const {chromium}=require('playwright-core');
const C=require('@sparticuz/chromium');
(async()=>{
  const b=await chromium.launch({executablePath:await C.executablePath(),args:C.args.filter(x=>x!=='--single-process')});
  for(const w of [390,1280]){
    const ctx=await b.newContext({viewport:{width:w,height:900}}),p=await ctx.newPage();
    const errs=[];p.on('pageerror',e=>errs.push(e.message));
    await p.goto('http://127.0.0.1:8096/lecons/ca-04-pression-arterielle.html',{waitUntil:'networkidle'});
    const r=await p.evaluate(()=>({nav:[...document.querySelectorAll('.ltab')].map(e=>({target:e.dataset.target,icon:!!e.querySelector('i'),exists:!!document.getElementById(e.dataset.target)})),syntheses:document.querySelectorAll('#resume-total figure img').length,boxes:document.querySelectorAll('main .lbox').length,notes:document.querySelectorAll('[data-tr^="note-qcm-"]').length}));
    if(r.nav.length!==20||r.nav.some(x=>!x.icon||!x.exists)||r.syntheses!==2||r.notes!==5||r.boxes<40||errs.length)throw Error(JSON.stringify({w,r,errs}));
    await p.locator('#resume-total img').first().evaluate(el=>el.scrollIntoView({behavior:'instant'}));
    await p.locator('#resume-total img').first().click();
    const zoom=await p.evaluate(()=>{const lb=document.querySelector('#imgLightbox'),i=lb.querySelector('img');return {open:lb.classList.contains('open'),w:i.getBoundingClientRect().width,h:i.getBoundingClientRect().height,scrollW:lb.scrollWidth,scrollH:lb.scrollHeight}});
    if(!zoom.open||zoom.w<1000||zoom.scrollH<=900||(w===390&&zoom.scrollW<=390))throw Error(JSON.stringify({w,zoom}));
    await p.locator('#imgLightbox .lb-close').click();
    if(await p.locator('#imgLightbox').evaluate(x=>x.classList.contains('open')))throw Error('zoom reste ouvert');
    console.log(JSON.stringify({w,nav:r.nav.length,syntheses:r.syntheses,boxes:r.boxes,notes:r.notes,zoom}));
    await ctx.close();
  }
  await b.close();
})().catch(e=>{console.error(e);process.exit(1)});
