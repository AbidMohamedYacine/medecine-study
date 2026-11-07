// Test exploratoire ciblé ; ne remplace pas l'audit ou une inspection complète.
const {chromium}=require('playwright-core');const C=require('@sparticuz/chromium');
(async()=>{const b=await chromium.launch({executablePath:await C.executablePath(),args:C.args.filter(x=>x!=='--single-process')});let bad=0;
for(const mode of ['anime','eco','photo','planche']) for(const theme of ['dark','light','aurora','ocean']){
 const ctx=await b.newContext({viewport:{width:1200,height:800}});await ctx.addInitScript(({mode,theme})=>{localStorage.setItem('seenmed-fond',mode);localStorage.setItem('seenmed-theme',theme)}, {mode,theme});const p=await ctx.newPage();let errors=[];p.on('pageerror',e=>errors.push(e.message));await p.goto('http://127.0.0.1:8096/lecons/ca-04-pression-arterielle.html',{waitUntil:'networkidle'});await p.evaluate(t=>window.SEENmedSetTheme(t),theme);await p.waitForTimeout(1400);
 if(mode==='photo') try{await p.waitForFunction(()=>document.body.classList.contains('fond-photo-pris'),{timeout:15000})}catch{}
 const x=await p.evaluate(()=>({mode:document.body.dataset.fond,theme:document.documentElement.dataset.theme||'dark',field:window.__cardioField?.count()||0,fixed:document.body.classList.contains('fond-fixe'),photo:document.body.classList.contains('fond-photo-pris'),bg:getComputedStyle(document.body).backgroundColor,canvas:getComputedStyle(document.getElementById('cardioFieldCanvas')).display}));
 const ok=x.mode===mode && x.theme===theme && (mode==='photo'?x.photo:mode==='planche'?x.fixed:x.field>50) && !errors.length; if(!ok)bad++;console.log(JSON.stringify({mode,theme,ok,...x,errors}));await ctx.close();}
await b.close();if(bad)process.exit(1)})().catch(e=>{console.error(e);process.exit(1)})
