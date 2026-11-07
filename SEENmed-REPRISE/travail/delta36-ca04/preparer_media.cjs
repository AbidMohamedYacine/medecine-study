// Reconstruction provisoire, conversion sans étirement : l'image entière reste visible.
const sharp = require('sharp');
const fs = require('fs');
const path = require('path');
const src = __dirname;
const root = process.argv[2];
if (!root) throw new Error('Indiquer le dossier medstudy temporaire');
const dest = path.join(root, 'assets/img/ca-04-delta36');
fs.mkdirSync(path.join(dest, 'reel'), { recursive:true });
const files = {
 'pression.webp':'v2/01-pression.png',
 'hero.webp':'v9/09-presentation.png',
 'fiche-comprendre.webp':'v10/01-comprendre.png',
 'fiche-cabinet.webp':'v10/02-cabinet.png',
 'systole.webp':'v2/02-systole.png',
 'posture.webp':'v10/03-posture.png',
 'deux-bras.webp':'v3/08-mesure-deux-bras.png',
 'comparaison.webp':'v10/05-comparaison.png',
 'automesure.webp':'v10/06-automesure.png',
 'mapa.webp':'v7/05-mapa-corrigee.png',
 'choix-brassard.webp':'v8/02-brassard.png',
 'profils.webp':'v8/01-profils.png',
};
async function main(){
 for (const [out, input] of Object.entries(files)) {
   const file=path.join(src,input);
   // Ces planches sont en 1408 × 768 : coupe centrée de 16 px par bord,
   // sans étirement ni fond flouté. Les contenus ont été inspectés après coupe.
   if (out === 'hero.webp') {
     await sharp(file).webp({quality:94}).toFile(path.join(dest,out));
     continue;
   }
   // Les planches v10 sont proches du 16:9 : ajustement par rognage centré,
   // sans déformation. Contrôler que les éléments importants restent visibles.
   if (input.startsWith('v10/')) {
     await sharp(file).resize(1376,768,{fit:'cover',position:'centre'}).webp({quality:94}).toFile(path.join(dest,out));
     continue;
   }
   if (['mapa.webp','choix-brassard.webp','profils.webp'].includes(out)) {
     await sharp(file).extract({left:16,top:0,width:1376,height:768}).webp({quality:94}).toFile(path.join(dest,out));
     continue;
   }
   // Les trois anciennes planches restantes sont recadrées sans étirement ni
   // bandes floutées ; la courbe privilégie le bas pour conserver ses axes.
   await sharp(file).resize(1376,768,{fit:'cover',position:out==='systole.webp'?'bottom':'centre'}).webp({quality:94}).toFile(path.join(dest,out));
 }
 for(const n of [16,20,44,45]) fs.copyFileSync(`/tmp/ca04-pages/${n}.png`,path.join(dest,`reel/diapo-${n}.png`));
 const aud=path.join(root,'assets/audio/ca-04-delta36'); fs.mkdirSync(aud,{recursive:true});
 for (let i=1;i<=10;i++){let n=String(i).padStart(2,'0');fs.copyFileSync(path.join(src,`audio-v3/${n}-fr.mp3`),path.join(aud,`${n}-fr.mp3`));}
 // Résumés longs FR/AR v4 : intégration provisoire, écoute encore requise.
 for (const lang of ['fr','ar'])fs.copyFileSync(path.join(src,`audio-v4/resume-${lang}.mp3`),path.join(aud,`resume-${lang}.mp3`));
 console.log('Médias provisoires préparés dans', dest);
}
main().catch(e=>{console.error(e);process.exit(1)});
