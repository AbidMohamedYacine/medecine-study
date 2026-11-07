/* SEENMED_CARDIO_THEMES_DELTA34 — réglages limités aux leçons ca-*. */
;(function(){
  var b=document.body;
  if(!b || !/^ca-\d\d$/.test(b.getAttribute('data-lesson-id')||'')) return;
  if(document.getElementById('seenmed-cardio-themes-delta34')) return;
  var style=document.createElement('style');
  style.id='seenmed-cardio-themes-delta34';
  style.textContent="/* DELTA34 \u2014 fond des le\u00e7ons cardiaques seulement ; pas les composants,\n   le texte, les images, les audios ou les couleurs s\u00e9mantiques des QCM. */\n@media screen {\n  body.has-cardio-field[data-lesson-id^=\"ca-\"] {\n    background-color:#1b0710;\n  }\n  html[data-theme=\"light\"] body.has-cardio-field[data-lesson-id^=\"ca-\"] {\n    background-color:#e8f3ff;\n  }\n  html[data-theme=\"aurora\"] body.has-cardio-field[data-lesson-id^=\"ca-\"] {\n    background-color:#03110b;\n  }\n  html[data-theme=\"ocean\"] body.has-cardio-field[data-lesson-id^=\"ca-\"] {\n    background-color:#211208;\n  }\n  body.has-cardio-field[data-lesson-id^=\"ca-\"]::after {\n    background:radial-gradient(ellipse 55% 40% at 12% -5%,rgba(255,80,105,.11),transparent 65%),\n               radial-gradient(ellipse 45% 35% at 95% 8%,rgba(255,164,125,.08),transparent 60%);\n  }\n  html[data-theme=\"aurora\"] body.has-cardio-field[data-lesson-id^=\"ca-\"]::after {\n    background:radial-gradient(ellipse 55% 40% at 12% -5%,rgba(70,207,151,.12),transparent 65%),\n               radial-gradient(ellipse 45% 35% at 95% 8%,rgba(165,231,174,.07),transparent 60%);\n  }\n  html[data-theme=\"ocean\"] body.has-cardio-field[data-lesson-id^=\"ca-\"]::after {\n    background:radial-gradient(ellipse 55% 40% at 12% -5%,rgba(255,187,89,.12),transparent 65%),\n               radial-gradient(ellipse 45% 35% at 95% 8%,rgba(235,113,61,.08),transparent 60%);\n  }\n}\n";
  document.head.appendChild(style);
})();

/* ============================================================
   SEENmed — CHAMP SANGUIN (cardio-field v1)
   Même moteur que bio-field, palette SÉMIOLOGIE CARDIAQUE :
   rouge « sang artériel » + orange « sang veineux oxygéné ».
   Les couleurs ne sont PAS lues dans --blue / --teal : elles sont
   propres au module, mais suivent les 4 thèmes du site.
   ------------------------------------------------------------
   SEENmri — INTERACTIVE PROTON FIELD v3 (calm + fast)
   Fixes over v2:
   • z-index:-1 canvas — fixed UI (navbar/AI/back-to-top) never breaks
   • spatial-hash field lines: O(n·k) instead of O(n²) → no jank
   • DPR capped at 1, softer sprites, calmer alphas → comfortable
   • 120–190 protons, quieter links, full-page recycling kept
   ============================================================ */
(function () {
    'use strict';

    /* Interrupteur global : en mode « fond fixe » ce fond ne demarre pas.
       Le cacher ne suffirait pas, le calcul continuerait. */
    if (window.SEENBG && !window.SEENBG.anime) return;

    var canvas = document.getElementById('cardioFieldCanvas');
    if (!canvas) return;
    var ctx = canvas.getContext('2d');
    if (!ctx) return;
    var body = document.body;
    var page = document.querySelector('.page-field-scope') || body;

    var reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches
                  || !!(window.SEENBG && window.SEENBG.eco);   /* mode eco : meme chemin que « mouvement reduit » */

    /* ================================================================
       MODE ÉCONOME v10 — LE FOND EST UNE IMAGE, PLUS UNE ANIMATION
       ----------------------------------------------------------------
       Deux défauts de la v9, corrigés ici.

       1. LE CHAMP SE VIDAIT EN DESCENDANT. Les particules vivent dans
          l'espace du DOCUMENT et step() recycle celles qui sortent d'une
          bande autour du défilement courant. Le rodage de 240 pas, joué
          une seule fois en haut de page, rapatriait donc TOUTES les
          particules dans ce premier écran : plus bas, le fond était nu.
       2. LE DÉFILEMENT COÛTAIT ENCORE. Chaque événement de scroll
          redessinait le canvas entier, et revenir sur l'onglet relançait
          la boucle complète. « Ça bouge un peu » — et la machine travaille.

       En mode éco le champ est désormais peint dans l'espace de l'ÉCRAN :
       les particules occupent le seul écran visible, le dessin ignore le
       défilement (scrollY = 0) et plus rien ne se redessine ensuite. Le
       fond est identique du haut en bas du document et son coût, après la
       première image, est exactement nul.
       ================================================================ */
    var FIGE = reduced;

    /* ---------------- palette CARDIOLOGIE ---------------- */
    /* rouge  = sang arteriel, le debit que le coeur doit assurer
       orange = la congestion en amont, chaude et montante          */
    /* alignee sur la couleur du module dans data.js : red */
    var COL = { main: [239, 68, 68], sec: [249, 115, 22], acc: [244, 92, 45] };
    /* une teinte par theme, calee sur la palette CSS correspondante */
    var THEME_MAP = {
        '':        [[239,  68,  68], [249, 115,  22]],   /* ecarlate + orange  */
        dark:      [[239,  68,  68], [249, 115,  22]],
        light:     [[185,  28,  28], [194,  65,  12]],   /* carmin + brique    */
        aurora:    [[244, 114, 182], [251, 146,  60]],   /* rose + abricot     */
        ocean:     [[255, 138,  91], [252, 211,  77]]    /* corail + safran    */
    };
    /* DELTA34 — couleurs du fond animé de la Sémiologie Cardiaque. */
    THEME_MAP[''] = THEME_MAP.dark = [[255,100,120],[255,168,125]];
    THEME_MAP.light = [[21,91,176],[0,111,136]];
    THEME_MAP.aurora = [[70,207,151],[165,231,174]];
    THEME_MAP.ocean = [[255,187,89],[235,113,61]];

    function readTheme() {
        var theme = (document.documentElement.getAttribute('data-theme') || 'dark').toLowerCase();
        var map = THEME_MAP[theme] || THEME_MAP.dark;
        COL.main = map[0].slice();
        COL.sec  = map[1].slice();
        COL.acc  = [
            Math.round((COL.main[0] + COL.sec[0]) / 2),
            Math.round((COL.main[1] + COL.sec[1]) / 2),
            Math.round((COL.main[2] + COL.sec[2]) / 2)
        ];
        buildSprites();
    }

    /* ---------------- softer glow sprites ---------------- */
    var sprites = {};
    var SPR = 64;
    function spriteFor(rgb) {
        var key = rgb.join(',');
        if (sprites[key]) return sprites[key];
        var c = document.createElement('canvas');
        c.width = c.height = SPR;
        var g = c.getContext('2d');
        var grad = g.createRadialGradient(SPR / 2, SPR / 2, 0, SPR / 2, SPR / 2, SPR / 2);
        grad.addColorStop(0,    'rgba(' + key + ',0.55)');   /* v3: much softer peak */
        grad.addColorStop(0.35, 'rgba(' + key + ',0.22)');
        grad.addColorStop(1,    'rgba(' + key + ',0)');
        g.fillStyle = grad;
        g.fillRect(0, 0, SPR, SPR);
        sprites[key] = c;
        return c;
    }
    function buildSprites() { spriteFor(COL.main); spriteFor(COL.sec); spriteFor(COL.acc); }
    buildSprites();

    /* ---------------- state ---------------- */
    var W = 0, H = 0, DPR = 1;
    var vw = 0, vh = 0;
    var mouse = { x: -9999, y: -9999, inside: false };
    var pulses = [];
    var parts = [];
    var running = true, rafId = null;

    var LINK_D = 112, CELL = LINK_D;   /* spatial-hash cell = link distance */

    function resize() {
        vw = window.innerWidth;
        vh = window.innerHeight;
        W = Math.max(vw, page.scrollWidth);
        H = Math.max(page.scrollHeight, body.scrollHeight);
        DPR = 1;                                  /* v3: crisp-enough, half the fill cost */
        canvas.width = vw * DPR;
        canvas.height = vh * DPR;
        canvas.style.width = vw + 'px';
        canvas.style.height = vh + 'px';
        ctx.setTransform(DPR, 0, 0, DPR, 0, 0);
        seed();
    }

    function scrollYBand() {
        /* v11 — mode econome : l'espace utile redevient le DOCUMENT.
           En v10 les particules tenaient dans le seul premier ecran,
           donc le fond ne pouvait pas defiler : il n'y avait rien
           en dessous a decouvrir. */
        if (FIGE) { return Math.random() * H; }
        var top = (window.pageYOffset || 0) - vh * 0.45 - 120;
        return top + Math.random() * (vh * 1.9 + 240);
    }
    function newPart(anywhere) {
        return {
            x: Math.random() * W,
            y: (FIGE || anywhere) ? Math.random() * H : scrollYBand(),
            vx: (Math.random() - 0.5) * 0.2,
            vy: (Math.random() - 0.5) * 0.2,
            r: 1.2 + Math.random() * 1.7,          /* v3: smaller */
            ci: Math.floor(Math.random() * 3),
            phase: Math.random() * Math.PI * 2,
            spin: 0.4 + Math.random() * 0.9
        };
    }
    function seed() {
        /* v11 — en mode econome le champ couvre TOUT le document : a
           nombre constant il serait dilue d'autant. On calcule donc la
           population sur la hauteur reelle, pour garder la MEME densite
           par ecran qu'en mode anime. Cout : un tableau plus long, mais
           le dessin ne traite que la bande visible. */
        var parEcran = Math.max(120, Math.min(190, Math.round(vw * vh / 7500)));
        var n = FIGE
            ? Math.min(9000, Math.round(parEcran * Math.max(1, H / vh)))
            : parEcran;
        parts = [];
        for (var i = 0; i < n; i++) parts.push(newPart(true));
    }
    function colOf(p) { return p.ci === 0 ? COL.main : p.ci === 1 ? COL.sec : COL.acc; }

    /* ---------------- interaction ---------------- */
    window.addEventListener('mousemove', function (e) {
        if (window.SEENBG && window.SEENBG.eco) { return; }
        mouse.x = e.clientX;
        mouse.y = e.clientY + (window.pageYOffset || 0);
        mouse.inside = true;
        dismissHint();
    }, { passive: true });
    document.addEventListener('mouseleave', function () {
        mouse.inside = false; mouse.x = -9999; mouse.y = -9999;
    });
    document.addEventListener('click', function (e) {
        if (window.SEENBG && window.SEENBG.eco) { return; }
        var t = e.target;
        if (t.closest && t.closest('a, button, input, select, textarea, label, .card, .vault-card, .bento, .btn, nav, .ai-panel, canvas#mriCanvas, .quiz-opt-btn, .exam-len-btn, .cine-case-btn, .lge-btn, .ks-mode-btn, .sr-chip, .es-chip, .cat-pill, .mode-tab-btn, .adv-chip, .adv-factor, .lp-item, .cod-card, .proto-btn, .vp-btn, .tab-btn, .ws-slider, .slider, .footer, #searchOverlay, #aiPanel, #preloader')) return;
        pulses.push({ x: e.clientX, y: e.clientY + (window.pageYOffset || 0), r: 6, v: 3.2, alpha: 0.8 });
        dismissHint();
    });
    window.addEventListener('touchmove', function (e) {
        if (window.SEENBG && window.SEENBG.eco) { return; }
        if (!e.touches || !e.touches[0]) return;
        var t = e.touches[0];
        mouse.x = t.clientX; mouse.y = t.clientY + (window.pageYOffset || 0);
        mouse.inside = true;
        dismissHint();
    }, { passive: true });
    window.addEventListener('touchend', function () {
        mouse.inside = false; mouse.x = -9999; mouse.y = -9999;
    });

    var hintGone = false;
    function dismissHint() {
        if (hintGone) return;
        hintGone = true;
        var h = document.getElementById('fieldHint');
        if (h) h.classList.add('gone');
    }
    new MutationObserver(function () {
        readTheme();
        /* en mode econome plus rien ne boucle : si l'on ne repeint pas
           ici, le fond garde les couleurs de l'ancien theme. */
        if (reduced) { draw(); }
    }).observe(document.documentElement, {
        attributes: true, attributeFilter: ['data-theme']
    });
    document.addEventListener('visibilitychange', function () {
        running = !document.hidden;
        /* v10 : en mode econome, revenir sur l'onglet ne doit PAS relancer
           la boucle — c'etait la fuite d'animation la plus sournoise.
           Une seule image, et seulement si le tampon a pu etre vide. */
        if (FIGE) { if (running) { draw(); } return; }
        if (running) start(); else stop();
    });

    /* ---------------- physics ---------------- */
    var MAG_R = 185;
    function step() {
        var i, j, p;
        for (i = pulses.length - 1; i >= 0; i--) {
            var pu = pulses[i];
            pu.r += pu.v; pu.v *= 0.985; pu.alpha *= 0.955;
            if (pu.alpha < 0.03) { pulses.splice(i, 1); continue; }
            for (j = 0; j < parts.length; j++) {
                p = parts[j];
                var dx = p.x - pu.x, dy = p.y - pu.y;
                var d = Math.sqrt(dx * dx + dy * dy) || 1;
                if (Math.abs(d - pu.r) < 34) {
                    var f = pu.alpha * 1.2 * (1 - Math.abs(d - pu.r) / 34);
                    p.vx += (dx / d) * f; p.vy += (dy / d) * f;
                }
            }
        }
        /* v11 — en mode econome la bande couvre tout le document :
           le rodage ne doit JAMAIS rapatrier les particules dans le
           premier ecran, sinon le bas de page redevient nu. */
        var bandTop = FIGE ? -1e7 : (window.pageYOffset || 0) - vh * 0.45 - 120;
        var bandBot = FIGE ? 1e7 : bandTop + vh * 1.9 + 240;
        for (i = 0; i < parts.length; i++) {
            p = parts[i];
            if (mouse.inside) {
                var mdx = mouse.x - p.x, mdy = mouse.y - p.y;
                var md = Math.sqrt(mdx * mdx + mdy * mdy) || 1;
                if (md < MAG_R) {
                    var pull = (1 - md / MAG_R) * 0.05;
                    p.vx += (mdx / md) * pull + (-mdy / md) * pull * 1.8;
                    p.vy += (mdy / md) * pull + ( mdx / md) * pull * 1.8;
                }
            }
            p.vx += (Math.random() - 0.5) * 0.011;
            p.vy += (Math.random() - 0.5) * 0.011;
            p.vx *= 0.962; p.vy *= 0.962;
            p.x += p.vx; p.y += p.vy;
            p.phase += p.spin * 0.06;
            if (p.x < -20) p.x = W + 20; else if (p.x > W + 20) p.x = -20;
            if (p.y < bandTop - 30 || p.y > bandBot + 30) {
                var np = newPart(false);
                p.y = np.y; p.x = np.x; p.vx = np.vx; p.vy = np.vy; p.ci = np.ci;
            }
        }
    }

    /* ---------------- render ---------------- */
    var visList = [];
    function draw() {
        ctx.clearRect(0, 0, vw, vh);
        var scrollY = (window.pageYOffset || 0);
        var yTop = scrollY - 220, yBot = scrollY + vh + 220;

        /* visible subset */
        visList.length = 0;
        for (var v = 0; v < parts.length; v++) {
            var pv = parts[v];
            if (pv.y >= yTop && pv.y <= yBot) visList.push(pv);
        }

        /* ---- field lines via spatial hash (O(n·k)) ---- */
        var grid = {}, pl;
        for (var a = 0; a < visList.length; a++) {
            pl = visList[a];
            var kx = (pl.x / CELL) | 0, ky = (pl.y / CELL) | 0;
            var key = kx + '_' + ky;
            if (!grid[key]) grid[key] = [];
            grid[key].push(pl);
        }
        ctx.lineWidth = 1;
        var OFF = [[0, 0], [1, 0], [0, 1], [1, 1]];
        for (var b = 0; b < visList.length; b++) {
            var p1 = visList[b];
            var cx = (p1.x / CELL) | 0, cy = (p1.y / CELL) | 0;
            for (var o = 0; o < 4; o++) {
                var cellArr = grid[(cx + OFF[o][0]) + '_' + (cy + OFF[o][1])];
                if (!cellArr) continue;
                for (var c = 0; c < cellArr.length; c++) {
                    var p2 = cellArr[c];
                    if (p2 === p1) continue;
                    if (OFF[o][0] === 0 && OFF[o][1] === 0 && c <= b && cellArr[c] === p2 && visList.indexOf(p2) <= b) continue; /* same-cell dedupe */
                    var ddx = p1.x - p2.x; if (ddx > LINK_D || ddx < -LINK_D) continue;
                    var ddy = p1.y - p2.y; if (ddy > LINK_D || ddy < -LINK_D) continue;
                    var dd2 = ddx * ddx + ddy * ddy;
                    if (dd2 > LINK_D * LINK_D) continue;
                    var al = (1 - Math.sqrt(dd2) / LINK_D) * 0.09;   /* v3: quieter lines */
                    var cc = colOf(p1);
                    ctx.strokeStyle = 'rgba(' + cc[0] + ',' + cc[1] + ',' + cc[2] + ',' + al.toFixed(3) + ')';
                    ctx.beginPath();
                    ctx.moveTo(p1.x, p1.y - scrollY);
                    ctx.lineTo(p2.x, p2.y - scrollY);
                    ctx.stroke();
                }
            }
        }

        /* ---- protons ---- */
        for (var k = 0; k < visList.length; k++) {
            var p = visList[k];
            var s = (2.3 + Math.sin(p.phase) * 0.55) * p.r;
            var sz = s * 5.2;
            var c2 = colOf(p);
            if (FIGE) {
                /* v11 — AUCUN HALO EN MODE ECONOME. C'est precisement la
                   lueur dont on ne veut pas, et le disque plein suffit a
                   donner sa presence au champ : on l'elargit un peu pour
                   compenser la disparition du degrade. */
                ctx.globalAlpha = 0.34;
                ctx.fillStyle = 'rgb(' + c2[0] + ',' + c2[1] + ',' + c2[2] + ')';
                ctx.beginPath();
                ctx.arc(p.x, p.y - scrollY, Math.max(1.1, s * 0.85), 0, Math.PI * 2);
                ctx.fill();
                ctx.globalAlpha = 0.62;
                ctx.fillStyle = 'rgba(238, 250, 242, 0.85)';
                ctx.beginPath();
                ctx.arc(p.x, p.y - scrollY, Math.max(0.6, s * 0.38), 0, Math.PI * 2);
                ctx.fill();
                ctx.globalAlpha = 1;
                continue;
            }
            ctx.globalAlpha = 0.55;                                   /* v3: calmer */
            ctx.drawImage(spriteFor(c2), p.x - sz / 2, p.y - sz / 2 - scrollY, sz, sz);
            ctx.globalAlpha = 0.5;
            ctx.fillStyle = 'rgba(238, 250, 242, 0.8)';
            ctx.beginPath();
            ctx.arc(p.x, p.y - scrollY, Math.max(0.5, s * 0.36), 0, Math.PI * 2);
            ctx.fill();
            ctx.globalAlpha = 1;
        }

        /* ---- RF pulses ---- */
        for (var q = 0; q < pulses.length; q++) {
            var pu2 = pulses[q];
            var py = pu2.y - scrollY;
            if (py < -pu2.r - 40 || py > vh + pu2.r + 40) continue;
            ctx.strokeStyle = 'rgba(' + COL.sec[0] + ',' + COL.sec[1] + ',' + COL.sec[2] + ',' + pu2.alpha.toFixed(3) + ')';
            ctx.lineWidth = 1.8;
            ctx.beginPath();
            ctx.arc(pu2.x, py, pu2.r, 0, Math.PI * 2);
            ctx.stroke();
        }
    }

    /* Plafond de cadence : un ecran 180 Hz appelle requestAnimationFrame
       180 fois par seconde. Soixante suffisent largement a l'oeil, et
       c'est trois fois moins de travail pour la machine. */
    var __cad = {};
    function frame(t) {
        if (!running) return;
        rafId = requestAnimationFrame(frame);
        if (window.SEENBG && !window.SEENBG.cadence(__cad, t)) return;
        step();
        draw();
    }
    /* v3.1: repaint the instant the page scrolls — the compositor moves the
       page at display rate; waiting for the next rAF left the field 1–2
       frames behind ("late, then catches up"). Drawing on the scroll event
       keeps the field locked to the pixels. */
    window.addEventListener('scroll', function () {
        /* mode econome : le fond ne suit plus la page — il est deja peint
           pour l'ecran entier, donc descendre ne coute RIEN. */
        if (FIGE || !running) { return; }
        draw();
    }, { passive: true });
    function start() { if (!rafId) rafId = requestAnimationFrame(frame); }
    function stop() { if (rafId) { cancelAnimationFrame(rafId); rafId = null; } }

    /* ---------------- boot ---------------- */
    /* v11 — LE RODAGE A ETE SUPPRIME. Il avancait la simulation de 240
       pas en silence avant de peindre la premiere image. Deux raisons
       de s'en passer : il recyclait les particules dans la bande du
       defilement courant, donc il VIDAIT tout le bas du document (le
       defaut signale) ; et sur un champ qui peut compter des milliers
       de points il aurait coute des centaines de millisecondes a
       l'ouverture. Les particules naissent desormais deja reparties. */

    var __rt = null;
    window.addEventListener('resize', function () {
        if (!FIGE) { resize(); return; }
        /* mode econome : une seule image, apres coup, jamais pendant. */
        clearTimeout(__rt);
        /* v11 : surtout PAS de rodage ici — le champ peut compter des
           milliers de particules, 240 pas figeraient la page. */
        __rt = setTimeout(function () { resize(); draw(); }, 180);
    });
    readTheme();
    resize();
    if (reduced) {
        /* RODAGE AVANT DE FIGER.
           Les particules naissent eteintes (lit: 0) et ne s'allument que
           dans step(). Une seule image dessinee a froid donnait un champ
           quasi vide — ce n'est pas « le fond vivant, immobile », c'est un
           fond absent. On avance donc la simulation en silence, sans rien
           peindre, puis on dessine UNE fois l'etat etabli. Cout : quelques
           millisecondes, une seule fois dans la vie de la page. */
    /* ----------------------------------------------------------------
       v11 — LA PAGE GRANDIT PENDANT QU'ON LA LIT.
       Les illustrations en chargement differe (loading="lazy") ne
       prennent leur hauteur qu'au moment ou on approche d'elles : un
       document de vingt ecrans peut en gagner trois pendant la lecture.
       Mesurer la hauteur une seule fois au demarrage laissait donc le
       tout dernier ecran hors du champ seme, donc VIDE. Un
       ResizeObserver nous previent sans sondage ; il se declenche apres
       la mise en page, donc lire la hauteur dans son rappel ne coute
       aucun recalcul. On ne reseme pas tout (ce serait un clignotement),
       on complete la seule bande nouvelle.
       ---------------------------------------------------------------- */
    function etendreChamp(nouveau) {
        var base = H;
        if (nouveau <= base || !parts.length) { return false; }
        var ajout = Math.min(9000 - parts.length,
                             Math.round(parts.length * (nouveau - base) / base));
        H = nouveau;
        for (var i = 0; i < ajout; i++) {
            var p = newPart(true);
            p.y = base + Math.random() * (nouveau - base);
            parts.push(p);
        }
        return ajout > 0;
    }
    function surveillerHauteur() {
        if (!window.ResizeObserver) { return; }
        var ro = new ResizeObserver(function () {
            var h = Math.max(page.scrollHeight, body.scrollHeight);
            if (h > H + 160 && etendreChamp(h)) { draw(); }
        });
        try { ro.observe(page); ro.observe(body); } catch (e) {}
    }

        /* v11 — PLUS DE RODAGE EN MODE ECONOME. Il ne servait qu'a
           laisser les particules se placer ; or elles naissent deja
           reparties, leur eclat ne depend que de la souris (absente
           ici), et 240 pas sur un champ de plusieurs milliers de points
           auraient fige la page a l'ouverture. */
        draw();
        surveillerHauteur();
        /* v11 : le champ est immobile, mais la fenetre se deplace
           devant lui. Un seul ecouteur, une image par rafraichissement. */
        if (window.SEENBG && window.SEENBG.auDefilement) {
            window.SEENBG.auDefilement(draw);
        }
        /* Les organes sont des glyphes Font Awesome peints AU CANVAS. Au
           premier dessin la police n'est pas encore arrivee : en mode anime
           la boucle rattrape a l'image suivante, ici il n'y en a pas. Le
           champ restait donc nu, reduit a ses points. On redessine quand la
           police est prete, puis deux fois par securite — et plus jamais. */
        if (document.fonts && document.fonts.ready) {
            document.fonts.ready.then(function () { draw(); });
        }
        /* v11 — au premier dessin la page n'a pas sa hauteur definitive
           (polices, images, sections depliees). Si l'on ne remesure pas, le
           champ s'arrete au milieu du document. On refait donc le semis une
           fois la page posee : deux fois, puis plus jamais. */
        function reajuster() { resize(); draw(); }
        setTimeout(reajuster, 900);
        setTimeout(reajuster, 2500);
    }
    else { start(); setTimeout(dismissHint, 9000); }

    window.__cardioField = {
        count: function () { return parts.length; },
        pulses: function () { return pulses.length; },
        mouse: mouse,
        colors: COL,
        fire: function (x, y) { pulses.push({ x: x, y: y, r: 6, v: 3.2, alpha: 0.8 }); }
    };
})();
