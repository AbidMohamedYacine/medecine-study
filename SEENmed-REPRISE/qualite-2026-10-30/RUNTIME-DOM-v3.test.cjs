#!/usr/bin/env Node
/* RUNTIME-DOM-v3 — preuve d'interactions en DOM émulé (jsdom), pour les
   environnements sans navigateur réel. Complément de RUNTIME-SMOKE-v3
   (Puppeteer) qui reste la porte audio-réel + captures.
   Usage : Node RUNTIME-DOM-v3.test.cjs <site> <page...>   (jsdom requis : npm i jsdom dans /tmp/seenmed-runtime) */
'use strict';
const fs = require('fs'), path = require('path'), http = require('http');
const { JSDOM } = (()=>{ const roots=[process.env.SMOKE_RUNTIME_DIR,'/tmp/seenmed-runtime',process.cwd(),__dirname].filter(Boolean);
  for(const r of roots){ try{ return require('module').createRequire(require('path').join(r,'package.json'))('jsdom'); }catch(e){} }
  return require('jsdom'); })();
const siteDir = process.argv[2], pages = process.argv.slice(3);
const MIME = { '.html':'text/html; charset=utf-8','.css':'text/css','.js':'text/javascript','.webp':'image/webp','.png':'image/png','.jpg':'image/jpeg','.svg':'image/svg+xml','.mp3':'audio/mpeg','.woff2':'font/woff2','.woff':'font/woff','.ttf':'font/ttf','.json':'application/json' };
const server = http.createServer((rq,rs)=>{ try{ let p=decodeURIComponent(rq.url.split('?')[0]); if(p.endsWith('/'))p+='index.html';
  const fp=path.join(siteDir,p); if(!fp.startsWith(path.resolve(siteDir))||!fs.existsSync(fp)){rs.writeHead(404);rs.end();return;}
  rs.writeHead(200,{'Content-Type':MIME[path.extname(fp)]||'application/octet-stream'}); fs.createReadStream(fp).pipe(rs);}catch(e){rs.writeHead(500);rs.end();} });
const results=[]; const sleep=ms=>new Promise(r=>setTimeout(r,ms));
function check(page,name,ok,detail){ results.push({ok:!!ok}); console.log((ok?'  ✓ ':'  ✗ FAIL ')+name+(detail?' — '+detail:'')); }

function fakeCtx(){
  const grad={addColorStop(){}};
  return new Proxy({}, { get(t,k){ if(k in t) return t[k];
      if(k==='measureText') return ()=>({width:0});
      if(k==='createLinearGradient'||k==='createRadialGradient') return ()=>grad;
      if(k==='getImageData') return (x,y,w,h)=>({data:new Uint8ClampedArray(w*h*4),width:w,height:h});
      if(k==='createPattern') return ()=>({});
      return ()=>{}; }, set(t,k,v){ t[k]=v; return true; } });
}
function stubs(w){
  w.matchMedia = q => ({ matches:false, media:q, addEventListener(){}, removeEventListener(){}, addListener(){}, removeListener(){} });
  w.HTMLCanvasElement.prototype.getContext = function(){ return this.__ctx || (this.__ctx=fakeCtx()); };
  w.HTMLCanvasElement.prototype.toDataURL = function(){ return 'data:image/png;base64,'+'A'.repeat(4000); };
  w.Element.prototype.scrollIntoView = function(){};
  w.HTMLElement.prototype.scrollIntoView = function(){};
  w.IntersectionObserver = class { constructor(cb){ this.cb=cb; } observe(){} unobserve(){} disconnect(){} };
  w.HTMLMediaElement.prototype.play = function(){ this.dispatchEvent(new w.Event('play')); return Promise.resolve(); };
  w.HTMLMediaElement.prototype.pause = function(){ this.dispatchEvent(new w.Event('pause')); };
  w.HTMLMediaElement.prototype.load = function(){};
  try{ Object.defineProperty(w.HTMLMediaElement.prototype,'paused',{get(){ return this.__paused!==false; }}); }catch(e){}
  w.HTMLMediaElement.prototype.__defineSetter__ && 0;
  const origPlay=w.HTMLMediaElement.prototype.play;
  w.HTMLMediaElement.prototype.play=function(){ this.__paused=false; this.dispatchEvent(new w.Event('play')); return Promise.resolve(); };
  w.HTMLMediaElement.prototype.pause=function(){ this.__paused=true; this.dispatchEvent(new w.Event('pause')); };
}

async function run(base, rel){
  const name=path.basename(rel); console.log('\n=== '+name+' ===');
  const html=fs.readFileSync(path.join(siteDir,rel),'utf-8');
  const errors=[];
  const dom=new JSDOM(html,{ url: base+'/'+rel, resources:'usable', runScripts:'dangerously', pretendToBeVisual:true,
    beforeParse:stubs, virtualConsole: (()=>{ const {VirtualConsole}=require('module').createRequire(require('path').join(process.env.SMOKE_RUNTIME_DIR||'/tmp/seenmed-runtime','package.json'))('jsdom'); const vc=new VirtualConsole(); vc.on('jsdomError',e=>{ if(!/Could not load|Could not parse CSS|Not implemented: HTMLMediaElement|Not implemented: navigation/.test(String(e.detail&&e.detail.message||e.message))) errors.push(String(e.detail&&e.detail.message||e.message)); }); vc.on('error',m=>errors.push(String(m))); return vc; })() });
  const w=dom.window, d=w.document;
  await new Promise(r=>{ if(d.readyState==='complete') r(); else w.addEventListener('load',r); setTimeout(r,12000); });
  await sleep(1500);
  const lid=d.body.getAttribute('data-lesson-id')||''; const isPn=lid.startsWith('pn-');

  try{
    const blk=d.querySelector('#annales .qblock'); const ans=JSON.parse(blk.getAttribute('data-answer'));
    ans.forEach(l=>blk.querySelector('li[data-l="'+l+'"]').click());
    blk.querySelector('.qcheck').click(); await sleep(150);
    const exp=blk.querySelector('.qexp');
    check(name,'QCM : answered + verdict bon', blk.classList.contains('answered')&&blk.querySelector('.qverdict').classList.contains('good'), blk.querySelector('.qverdict').textContent.trim());
    check(name,'QCM : correction visible', w.getComputedStyle(exp).display!=='none', 'display='+w.getComputedStyle(exp).display);
    check(name,'QCM : score de série', d.querySelector('#annales .qs-val').textContent.trim()==='1 / 1', d.querySelector('#annales .qs-val').textContent.trim());
  }catch(e){ check(name,'QCM',false,String(e).slice(0,200)); }

  try{
    const cine=JSON.parse(d.getElementById('cineData').textContent);
    const boutons=d.querySelectorAll('#cinePlayer .cine-chapitres li').length;
    check(name,'Ciné central monté', boutons>=cine.chapitres.length, boutons+'/'+cine.chapitres.length);
    const spots=d.querySelectorAll('.cine-spot .cspot-play').length;
    check(name,'mini-lecteurs montés', spots>0, spots+' spots');
    d.querySelector('.cine-spot .cspot-play').click(); await sleep(250);
    check(name,'mini-lecteur : événement play → état « on »', d.querySelector('.cine-spot').classList.contains('on'));
    d.querySelector('#cinePlayer .cine-bigplay').click(); await sleep(250);
    check(name,'Ciné central : événement play → « playing »', !!d.querySelector('#cinePlayer .cine-wrap.playing'));
  }catch(e){ check(name,'Ciné',false,String(e).slice(0,200)); }

  try{
    const kwN=JSON.parse(d.getElementById('kwData').textContent).length;
    d.getElementById('kwHandle').click(); await sleep(200);
    const items=d.querySelectorAll('#kwPanel .kw-list > li').length;
    check(name,'dictionnaire ouvert, termes rendus', d.getElementById('kwPanel').classList.contains('open')&&items===kwN, items+'/'+kwN);
    d.querySelector('#kwPanel .kw-lang').click(); await sleep(150);
    const def=d.querySelector('#kwPanel .kw-def');
    check(name,'définitions arabes du dictionnaire', !!def&&(def.getAttribute('dir')==='rtl'||def.classList.contains('ar')));
  }catch(e){ check(name,'Mots-clés',false,String(e).slice(0,200)); }

  try{
    const el=d.querySelector('[data-tr]'); const before=el.textContent.slice(0,40);
    d.querySelector('.ar-toggle').click(); await sleep(200);
    check(name,'mode arabe : traduction + RTL', el.getAttribute('dir')==='rtl'&&el.textContent.slice(0,40)!==before);
    d.querySelector('.ar-toggle').click(); await sleep(150);
  }catch(e){ check(name,'Mode arabe',false,String(e).slice(0,200)); }

  try{
    const q=d.querySelector('#fcFront .fc-q');
    check(name,'flashcards : première carte', !!q&&q.textContent.trim().length>0, d.getElementById('fcCount').textContent.trim());
    d.getElementById('fcCard').click(); await sleep(150);
    check(name,'flashcards : flip', d.getElementById('fcCard').classList.contains('flipped'));
    d.getElementById('fcGood').click(); await sleep(200);
    check(name,'flashcards : notation → suivante', /2/.test(d.getElementById('fcCount').textContent), d.getElementById('fcCount').textContent.trim());
  }catch(e){ check(name,'Flashcards',false,String(e).slice(0,200)); }

  try{
    if(isPn){
      const cnt=w.__pneumoField?w.__pneumoField.count():-1;
      check(name,'peau pneumo : canvas + particules + pneumo-root', !!d.getElementById('pneumoFieldCanvas')&&cnt>50&&d.documentElement.classList.contains('pneumo-root'), cnt+' particules');
      const exp={dark:'53,208,255',light:'8,126,164',aurora:'167,139,250',ocean:'45,212,191'};
      for(const t of ['dark','light','aurora','ocean']){
        d.documentElement.setAttribute('data-theme',t); await sleep(600);
        const col=w.__pneumoField?w.__pneumoField.colors.main.join(','):'';
        check(name,'thème '+t+' : palette du champ', col===exp[t], col);
      }
    } else {
      const cnt=w.__heroField?w.__heroField.count():-1;
      check(name,'peau bio : canvas + particules', !!d.getElementById('bioFieldCanvas')&&cnt>50, cnt+' particules');
    }
  }catch(e){ check(name,'Peau/thèmes',false,String(e).slice(0,200)); }

  check(name,'aucune erreur JS (hors limites jsdom filtrées)', errors.length===0, errors.slice(0,3).join(' | ').slice(0,240));
  w.close();
}
(async()=>{ await new Promise(r=>server.listen(0,'127.0.0.1',r));
  const base='http://127.0.0.1:'+server.address().port;
  for(const p of pages) await run(base,p);
  server.close();
  const fails=results.filter(r=>!r.ok).length;
  console.log('\n================ '+(results.length-fails)+'/'+results.length+' checks OK'+(fails?' — '+fails+' ÉCHEC(S)':' — TOUT PASSE'));
  process.exit(fails?1:0);
})().catch(e=>{console.error(e);process.exit(2);});
