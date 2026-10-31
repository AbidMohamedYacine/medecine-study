/* RUNTIME-CINE-AR — test ciblé de la bascule ع/FR du Ciné (delta 19, 31/10/2026).
   Bug d'origine : charger() réinitialisait la langue partagée quand le chapitre
   courant du lecteur central n'avait pas de piste arabe. Usage (depuis un dossier
   avec jsdom installé, ex. /tmp/seenmed-runtime) :
   nodejs RUNTIME-CINE-AR.test.cjs [site] [page] — page attendue : derniers chapitre
   = résumé avec piste AR, chapitres FR seuls. */
'use strict';
const fs=require('fs'), path=require('path'), http=require('http');
const {JSDOM}=require('jsdom');
const SITE=process.argv[2]||'/tmp/site/medstudy', PAGE=process.argv[3]||'lecons/pn-08-syndromes-mediastinaux.html';
const MIME={'.html':'text/html; charset=utf-8','.css':'text/css','.js':'text/javascript','.webp':'image/webp','.mp3':'audio/mpeg','.json':'application/json','.woff2':'font/woff2'};
const server=http.createServer((rq,rs)=>{ let p=decodeURIComponent(rq.url.split('?')[0]); const fp=path.join(SITE,p);
  if(!fs.existsSync(fp)){rs.writeHead(404);rs.end();return;} rs.writeHead(200,{'Content-Type':MIME[path.extname(fp)]||'application/octet-stream'}); fs.createReadStream(fp).pipe(rs);});
const sleep=ms=>new Promise(r=>setTimeout(r,ms));
let pass=0, fail=0; const ck=(n,ok,d)=>{ console.log((ok?'  ✓ ':'  ✗ FAIL ')+n+(d?' — '+d:'')); ok?pass++:fail++; };
(async()=>{
  await new Promise(r=>server.listen(0,'127.0.0.1',r));
  const base=`http://127.0.0.1:${server.address().port}/`;
  const audios=[];
  const html=fs.readFileSync(path.join(SITE,PAGE),'utf-8');
  const dom=new JSDOM(html,{url:base+PAGE,resources:'usable',runScripts:'dangerously',pretendToBeVisual:true,
    beforeParse(w){
      w.matchMedia=q=>({matches:false,media:q,addEventListener(){},removeEventListener(){},addListener(){},removeListener(){}});
      const grad={addColorStop(){}}; const fake=new Proxy({},{get(t,k){ if(k in t)return t[k]; if(k==='measureText')return()=>({width:0}); if(k==='createLinearGradient'||k==='createRadialGradient')return()=>grad; if(k==='getImageData')return(x,y,ww,h)=>({data:new Uint8ClampedArray(ww*h*4),width:ww,height:h}); return()=>{};},set(t,k,v){t[k]=v;return true;}});
      w.HTMLCanvasElement.prototype.getContext=function(){return fake;};
      w.Element.prototype.scrollIntoView=function(){};
      w.IntersectionObserver=class{constructor(){}observe(){}unobserve(){}disconnect(){}};
      w.HTMLMediaElement.prototype.play=function(){this.__paused=false;this.dispatchEvent(new w.Event('play'));return Promise.resolve();};
      w.HTMLMediaElement.prototype.pause=function(){this.__paused=true;this.dispatchEvent(new w.Event('pause'));};
      try{Object.defineProperty(w.HTMLMediaElement.prototype,'paused',{get(){return this.__paused!==false;}});}catch(e){}
      const Orig=w.Audio; const wrapped=function(...a){ const el=new Orig(...a); audios.push(el); return el; };
      wrapped.prototype=Orig.prototype; w.Audio=wrapped;
    }});
  const w=dom.window, d=w.document;
  await new Promise(r=>{ if(d.readyState==='complete')r(); else w.addEventListener('load',r); });
  await sleep(600);
  const spot=d.querySelector('.cine-spot[data-ch="6"]');
  ck('spot résumé monté', !!spot && !!spot.querySelector('.cspot-lang'));
  ck('bouton ع/FR visible sur le résumé', spot && !spot.querySelector('.cspot-lang').hidden);
  ck('16 audios créés (1 central + 15 spots)', audios.length===16, String(audios.length));
  // 1) bascule AR depuis le spot (cas signalé par l'utilisateur)
  spot.querySelector('.cspot-lang').click(); await sleep(100);
  ck('langue partagée = ar après bascule', w.localStorage.getItem('seenmed-cine-lang')==='ar', w.localStorage.getItem('seenmed-cine-lang'));
  ck('bouton du spot allumé', spot.querySelector('.cspot-lang').classList.contains('on'));
  // 2) lecture du résumé : la piste AR doit être chargée
  spot.querySelector('.cspot-play').click(); await sleep(100);
  const aRes=audios.find(a=>(a.src||'').includes('resume'));
  ck('piste ARABe chargée (resume-ar.mp3)', !!aRes && aRes.src.includes('resume-ar.mp3'), aRes?aRes.src:'aucun src resume*');
  // 3) navigation chapitre FR-only au lecteur central : la langue NE doit PAS retomber
  const chaps=d.querySelectorAll('.cine-chap'); chaps[0].click(); await sleep(100);
  ck('langue toujours ar après navigation ch.1', w.localStorage.getItem('seenmed-cine-lang')==='ar', w.localStorage.getItem('seenmed-cine-lang'));
  const note=d.querySelector('.cine-note');
  ck('note honnête « ع en préparation » sur ch. FR-only', note && !note.hidden, note?note.textContent:'');
  // 4) chapitre résumé au central : piste AR
  chaps[6].click(); await sleep(100);
  const aCen=audios[0];
  ck('lecteur central sur resume-ar.mp3', (aCen.src||'').includes('resume-ar.mp3'), aCen.src);
  // 5) retour FR depuis le spot
  spot.querySelector('.cspot-lang').click(); await sleep(100);
  ck('retour FR', w.localStorage.getItem('seenmed-cine-lang')==='fr' && !spot.querySelector('.cspot-lang').classList.contains('on'));
  console.log(`\n================ TEST BASCULE AR : ${pass}/${pass+fail} OK — ${fail} ÉCHEC(S)`);
  dom.window.close(); server.close(); process.exit(fail?1:0);
})().catch(e=>{console.error('ERR',e); server.close(); process.exit(2);});
