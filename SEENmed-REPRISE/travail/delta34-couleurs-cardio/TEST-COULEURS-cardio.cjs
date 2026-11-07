// NODE_PATH doit contenir playwright-core et @sparticuz/chromium ; site test servi en local.
const {chromium} = require('playwright-core');
const chrome = require('@sparticuz/chromium');
const fs = require('fs');
const path = require('path');
const root = process.env.SITE || '/tmp/cardio-site/medstudy';
const url = process.env.URL || 'http://127.0.0.1:8094';
const pages = fs.readdirSync(path.join(root,'lecons')).filter(x => /^ca-\d\d-.*\.html$/.test(x)).sort();
const themes = ['dark','light','aurora','ocean'];
const expected = {dark:['rgb(27, 7, 16)','255,100,120'], light:['rgb(232, 243, 255)','21,91,176'], aurora:['rgb(3, 17, 11)','70,207,151'], ocean:['rgb(33, 18, 8)','255,187,89']};
(async()=>{
 if (pages.length!==11) throw new Error(`Attendu 11 pages, trouve ${pages.length}`);
 const browser=await chromium.launch({executablePath:await chrome.executablePath(),args:chrome.args,headless:true});
 const context=await browser.newContext({viewport:{width:1440,height:900},reducedMotion:'reduce'});
 const p=await context.newPage();let errors=[];p.on('pageerror',e=>errors.push(e.message));let checks=0;
 for (const name of pages) {
  await p.goto(`${url}/lecons/${name}`,{waitUntil:'load'});
  await p.evaluate(()=>window.SEENmedSetTheme('dark'));
  for (const [i,t] of themes.entries()) {
   if (i) await p.locator('.theme-toggle').first().click();
   await p.waitForTimeout(1800);
   const data=await p.evaluate(()=>({theme:document.documentElement.getAttribute('data-theme')||'dark', bg:getComputedStyle(document.body).backgroundColor, v:getComputedStyle(document.body).getPropertyValue('--bg'), styleRules:document.getElementById('seenmed-cardio-themes-delta34')?.sheet?.cssRules?.length, colors:window.__cardioField?.colors?.main?.join(','), skin:!!document.getElementById('seenmed-cardio-themes-delta34'), title:document.querySelector('h1')?.innerText, nav:!!document.querySelector('.navbar'), tabs:document.querySelectorAll('.ltab').length}));
   if(data.theme!==t||data.bg!==expected[t][0]||data.colors!==expected[t][1]||!data.skin||!data.title||!data.nav||!data.tabs)throw new Error(`${name} ${t}: ${JSON.stringify(data)}`);
   checks++;
  }
  await p.evaluate(()=>window.scrollTo(0,document.documentElement.scrollHeight*.7)); await p.waitForTimeout(80);
  if(!await p.evaluate(()=>scrollY>0)) throw new Error(`${name} ne défile pas`);
  console.log(`OK ${name}: 4 thèmes, couleurs du champ et défilement`);
 }
 if(errors.length) throw new Error('Erreurs JS : '+JSON.stringify(errors));
 console.log(`OK ${checks}/44 thèmes ; aucune pageerror.`); await browser.close();
})().catch(e=>{console.error(e);process.exit(1)});
