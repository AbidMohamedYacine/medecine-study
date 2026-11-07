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
 'systole.webp':'v2/02-systole.png',
 'posture.webp':'v3/03-posture.png',
 'deux-bras.webp':'v3/08-mesure-deux-bras.png',
 'comparaison.webp':'v2/07-deux-bras.png',
 'automesure.webp':'v3/06-automesure.png',
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
   if (['mapa.webp','choix-brassard.webp','profils.webp'].includes(out)) {
     await sharp(file).extract({left:16,top:0,width:1376,height:768}).webp({quality:94}).toFile(path.join(dest,out));
     continue;
   }
   const bg=await sharp(file).resize(1376,768,{fit:'cover'}).blur(35).modulate({brightness:.65}).toBuffer();
   const fg=await sharp(file).resize(1376,768,{fit:'contain',background:{r:0,g:0,b:0,alpha:0}}).png().toBuffer();
   await sharp(bg).composite([{input:fg}]).webp({quality:90}).toFile(path.join(dest,out));
 }
 for(const n of [16,20,44,45]) fs.copyFileSync(`/tmp/ca04-pages/${n}.png`,path.join(dest,`reel/diapo-${n}.png`));
 const aud=path.join(root,'assets/audio/ca-04-delta36'); fs.mkdirSync(aud,{recursive:true});
 for (let i=1;i<=10;i++){let n=String(i).padStart(2,'0');fs.copyFileSync(path.join(src,`audio-v3/${n}-fr.mp3`),path.join(aud,`${n}-fr.mp3`));}
 for (const lang of ['fr','ar'])fs.copyFileSync(path.join(src,`audio-v2/resume-${lang}.mp3`),path.join(aud,`resume-${lang}.mp3`));
 console.log('Médias provisoires préparés dans', dest);
}
main().catch(e=>{console.error(e);process.exit(1)});
