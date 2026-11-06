/* NODE_PATH=<playwright-core> node TEST-modes-pneumo.cjs <base URL> <chromium executable> */
const assert = require('assert');
const {chromium} = require('playwright-core');
const [base, executablePath] = process.argv.slice(2);
if (!base || !executablePath) throw Error('URL and Chromium executable required');
(async () => {
  const browser = await chromium.launch({executablePath,headless:true,args:['--no-sandbox','--single-process','--no-zygote']});
  const page = await browser.newPage({viewport:{width:1440,height:850}});
  await page.goto(`${base}/lecons/pn-03-semiologie-de-la-toux.html`);
  for (const mode of ['anime','eco','photo','planche']) {
    await page.evaluate(mode => localStorage.setItem('seenmed-fond',mode),mode);
    await page.reload({waitUntil:'domcontentloaded'});
    await page.waitForTimeout(mode === 'photo' ? 5000 : 1100);
    const x = await page.evaluate(() => {
      const c=document.querySelector('#pneumoFieldCanvas'), layer=document.querySelector('.static-bg');
      return {mode:SEENBG.mode,display:getComputedStyle(c).display,position:getComputedStyle(c).position,
        hero:document.querySelector('.lesson-hero').getBoundingClientRect().top,
        photo:document.body.classList.contains('fond-photo-pris'),
        planche:document.body.classList.contains('fond-fixe'),
        staticImage:layer ? getComputedStyle(layer).backgroundImage : 'none'};
    });
    assert.equal(x.mode,mode); assert.equal(x.position,'fixed'); assert(x.hero<250);
    if (mode === 'planche') { assert(x.planche); assert.equal(x.display,'none'); assert.notEqual(x.staticImage,'none'); }
    if (mode === 'photo') { assert(x.photo,'photo capture failed'); assert.equal(x.display,'none'); assert(x.staticImage.startsWith('url("data:image/')); }
    if (mode === 'anime' || mode === 'eco') assert.equal(x.display,'block');
    console.log('PASS',mode);
  }
  await browser.close();
})().catch(e=>{console.error(e);process.exit(1)});
