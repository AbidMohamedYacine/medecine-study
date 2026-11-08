const {chromium}=require('playwright-core');const C=require('@sparticuz/chromium');
(async()=>{const browser=await chromium.launch({executablePath:await C.executablePath(),args:C.args.filter(x=>x!=='--single-process')});
for(const theme of ['dark','light','aurora','ocean']){
 const ctx=await browser.newContext({viewport:{width:1280,height:900}});const p=await ctx.newPage();await p.goto('http://127.0.0.1:8096/lecons/ca-04-pression-arterielle.html',{waitUntil:'networkidle'});
 await p.addStyleTag({content:'*,*::before,*::after{transition:none!important;animation:none!important}'});
 const r=await p.evaluate(theme=>{document.documentElement.setAttribute('data-theme',theme);const selectors=['body','.lesson-nav','.ltab.active','.essence','.roadmap','.lbox'];return Object.fromEntries(selectors.map(s=>{const el=document.querySelector(s),c=getComputedStyle(el);return [s,{bg:c.backgroundColor,color:c.color}]}));},theme);
 console.log(JSON.stringify({theme,styles:r}));const expected={dark:['rgb(27, 11, 19)','rgba(255, 119, 137, 0.22)'],light:['rgb(232, 242, 252)','rgba(21, 91, 176, 0.16)'],aurora:['rgb(7, 29, 24)','rgba(124, 226, 179, 0.22)'],ocean:['rgb(29, 17, 10)','rgba(255, 194, 124, 0.23)']}[theme];if(r.body.bg!==expected[0]||r['.ltab.active'].bg!==expected[1])throw Error('couleurs incorrectes '+theme);await ctx.close();}
await browser.close()})().catch(e=>{console.error(e);process.exit(1)});
