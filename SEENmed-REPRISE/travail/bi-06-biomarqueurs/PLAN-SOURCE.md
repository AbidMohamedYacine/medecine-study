# bi-06 — Les biomarqueurs cardiaques
## Plan source-grounded (étape 1/Construction — 28/10/2026)

**Empreinte de source (N-1)** : `7/biomarqeur cardiaque - E 2026.pdf` · Drive ID
`1qx87LvbO2yNPZFxRyX8oK0DuBqK75H3E` · 1 334 520 o · MD5 `dfd351f2a76cbe0568d08a85503562b9` ·
**32 pages** · Dr Besbes, A — 2025/2026 (page 1). PDF de diapositives, texte léger, 3 visuels
exploitables : structure troponine (p.7), ECG STEMI (p.13), **courbe cinétique (p.20)**.
**Annales** : ELITE CARDIO 3ᵉ année, Biochimie §5 « Biomarqueurs cardiaques » pp.30-32 :
**10 QCM** (PROMO 2018→2022), corrigés officiels. Statut : source N-1, patch différentiel
à l'arrivée de la source N (protocole `04`). Peau module dès la construction : **Biochimie**
(`has-bio-field` + `bio-field.js?v=11`, footer + `backToTop` + `scrollProgress` — addendum 03).

## Ce que la source contient (lu en entier, texte + images rendues)
CV = 1ʳᵉ cause de mortalité · définition (mesurable, produite par le cœur, utilisée
diag/pronostic/suivi) · **3 catégories** (nécrose, fonction, inflammation/risque) ·
nécrose = protéines libérées à la destruction cellulaire → **diag SCA + sévérité** ·
**troponine** : complexe **TnC (calcium, déclenche) / TnI (inhibe actine-myosine) /
TnT (fixe à la tropomyosine)** ; **TnI+ TnT cardiospécifiques, TnC non** (squelettique) ;
marqueur de référence SCA, **élevée 6-10 j** · **classique vs hs-cTn** (détection **3-6 h**
vs **1-2 h** ; **TnI 3-6 j, TnT ≤ 10 j**) · variations (↑ âge >60 ans, ↑ homme) ·
**autres causes ↑ cTn** (cardiaques : myocardite, cardiomyopathies, IC, troubles du
rythme sévères, contusion, HTA, CO ; extracardiaques : EP/HTAP, sepsis, IR, AVC/hémorragie
méningée, exercice intense prolongé, brûlure sévère, venin) · interprétation **toujours**
anamnèse + clinique + ECG · **STEMI** : diag clinique+ECG, reperfusion **sans attendre**
la troponine ; **NSTEMI** : douleur + ECG non spécifique + **élévation/cinétique cTn** ·
**algorithmes** : classique H0 → H6-9 ; hs H0 → H1/H2/H3 ; **2× normale = exclusion IDM
fiable** · **myoglobine** : cytoplasmique muscle strié, **↑ ~2 h, pic 4-12 h, normale ~24 h**,
diag précoce + récidive, **supplantée** (spécificité) ; autres causes (rhabdomyolyse…) ·
**CK-MB** : isoenzyme, **↑ 4-6 h, retour 2-3 j**, réinfarctus précoce, supplantée par cTn ·
**courbe cinétique p.20** · fonction myocardique = surcharge pression/volume, distension, IC ·
**BNP** : ventricules, surcharge pression/volume, issu du **clivage pro-BNP**, actions
**vasodilatatrices, filtration glomérulaire ↑ (diurétique), réabsorption Na ↓ (natriurétique),
anti-SRAA/sympathique** · **NT-proBNP** : fragment **inactif**, **plus stable, demi-vie plus
longue**, **élimination rénale** · clinique IC : diagnostic (haute précision + ETT),
**dyspnée cardiaque (↑) vs pulmonaire (normale)**, **pronostic** morbi-mortalité, suivi/
ajustement · variations NT-proBNP (**âge ↑, femme ↑, obésité ↓, effort intense ↑ transitoire**) ·
autres causes ↑ NT-proBNP (FA, cardiomyopathies, HTA sévère ; EP, HTAP, BPCO/asthme aigu ;
IR ; sepsis ; hyperthyroïdie, Cushing ; cirrhose+ascite, anémie sévère, AVC) · inflammation :
**hs-CRP** (prédit risque CV ; **<1 faible, 1-3 intermédiaire, >3 mg/L élevé**), **fibrinogène**
(inflammation vasculaire, thrombose) · conclusion : complètent, **ne remplacent ni clinique
ni imagerie**.

## Croisement annales — zones tombables ★★ (10 QCM analysés)
1. **Troponine** (quasi tout) : marqueur de choix diag + pronostic ; ↑ hors IDM (IC sévère,
   EP, choc septique — jamais « uniquement IDM ») ; **spécificité myocardique ≠ coronarienne**
   (le mot « coronarienne » est corrigé faux, 2018) ; TnC non spécifique ; indications
   (ischémie/souffrance, **diagnostic rétrospectif** car 6-10 j, myo/péricardites).
2. **Cinétiques comparées** : myoglobine précoce non spécifique (+ récidive, corrigée vraie) ;
   CK-MB plus lente que myoglobine ; hs-cTn H0 + 2 h (classer/exclure) ; VPN élevée des hs.
3. **BNP/NT-proBNP** : ventricule, diurétique + vasodilatateur, dyspnée cardiaque vs
   pulmonaire, VPN/VPP IC ; troponine n'est PAS le marqueur de l'IC.
4. **Marqueur idéal** (sensible + spécifique + précoce) et anciens déclassés (ASAT/ALAT/LDH
   ni précoces ni spécifiques ; BNP hors « marqueurs coronariens »).
⚠️ **Testé en annales mais absent des diapos** (enseigner au niveau annales, confirmer
source N) : ASAT/ALAT/LDH et leur déclassement ; copeptine et h-FABP (« toujours
recommandés » = faux) ; vocabulaire VPN/VPP ; « deux catégories H0-H1 » non retenu.
Distribution des réponses : 1 rép ×2 · 2 rép ×1 · 3 rép ×6 · 4 rép ×1 — l'entraînement
(20 Q) calque : 4×1 · 2×2 · 12×3 · 2×4.

## Sections de la leçon (12, thématiques nommées)
`enjeux` définition & 3 familles (+ marqueur idéal) · `necrose` le principe ·
`troponine` complexe & spécificité ★★ · `hs` classique vs hypersensible ★★ ·
`interpretation` ↑ sans IDM + trio d'interprétation ★★ · `sca` STEMI/NSTEMI & algorithmes ★★ ·
`myoglobine` la sprinteuse déclassée · `ckmb` l'isoenzyme du réinfarctus ·
`cinetique` la courbe comparée (+ historiques) · `peptides` BNP/NT-proBNP ★★ ·
`np-clinique` peptides au lit du malade ★★ · `inflammation` hs-CRP/fibrinogène + conclusion.

## Visuels (charte images : réalité d'abord)
Hero, mindmap, 12 planches de section (sarcomère réel avec complexe troponine,
courbes de cinétique sur graphique de labo, ECG STEMI vs NSTEMI, ventricule distendu
sécrétant BNP, dyspnée urgences cœur/poumon), ff-×6, total dédié.
**Reels retenus** (q90, jamais agrandis, source citée Dr Besbes A + page) : p.7 structure
(étiquettes EN d'origine, légende FR), p.13 ECG STEMI, p.20 courbe cinétique.
Audio : 8 chapitres FR (regroupant les 12 sections) + résumé FR + résumé AR.
Arabe complet + mots-clés (~36).

## Avancement
- [x] Source lue en entier (32 pages texte + rendus images p.1/5/12/14/18 + 3 reels vus)
- [x] Annales relevées (10 QCM + corrigés officiels ELITE pp.30-32) et croisement tombable
- [x] Plan de sections, visuels, reels, audio (ce fichier)
- [ ] Reels convertis WebP q90 → `img/reel/` ; planches (21) q83 relues
- [ ] Page complète (builder, peau Biochimie) → arabe → QCM → fiche → audio
- [ ] Intégration `data.js` (qcm 10, entr 20) → audit 0 → livraison Drive datée
- [ ] Patch différentiel à l'arrivée de la source N

## État d'avancement (2026-10-28)
- [x] Source N-1 lue en entier + annales ELITE §5 (10 QCM) croisées — voir ci-dessus.
- [~] Images : lot 1 = 10/21 générées, relues (contact + zooms), WebP q83 (`img/`) + 3 reels q90. **Lot 2 restant (cap 10 images/tour) :** `cinetique, peptides, np-clinique, inflammation, ff-troponine, ff-cinetique, ff-algo, ff-causes, ff-bnp, ff-seuils` puis `total` (11ᵉ).
- [x] Page construite : `build_bi06.py` (squelette gold ra-02 + peau `has-bio-field`/`bio-field.js?v=11`, footer gold → bi-07-gazometrie.html, `backToTop`/`scrollProgress` 1×). 12 sections FR+AR (76 clés), 10 annales verbatim, 20 entraînement (4×1·2×2·12×3·2×4), 36 mots-clés, 25 flashcards, JSON OK ×4. Copie : `page/bi-06-biomarqueurs-cardiaques.html`.
- [x] Intégration `data.js` (qcm 10, entr 20, recu true, url) — copie `page/data-apres-bi06.js`.
- [~] Audio : 9/10 MP3 générés (ch1–8 + résumé AR). **Restant : `resume.mp3` FR** (2 échecs > 1500 car. + cap 10/tour ; version courte prête dans `audio-scripts.md`).
- [ ] Audit final : actuel = pages 61, bi-06 12 refs (11 images lot 2 + resume.mp3), AN-06 11 (connu). Objectif après lot 2 : bi-06 = 0.
- [ ] Livraison Drive datée `02_LIVRAISON-bi-06_2026-10-28` (+ page bi-05 corrigée peau, absente du ZIP bi-05 pré-fix).

> ⚠ Note intégrité (2026-10-28) : une première version du bloc annales du builder, reconstruite de mémoire, a été **écartée avant build** après re-vérification sur l'extraction ELITE (`/tmp/bi06-annales.txt`). Les 10 annales de la page sont bien verbatim pp. 30–32, réponses officielles BCD·ADE·C·ACD·ACD·ABD·ABCD·DE·ABD·A. Nuances signalées en corrections : Q4-D « pro-BNP molécule de choix » (officiel ; on dose BNP/NT-proBNP), Q6-D « myoglobine peu sensible » (officiel ; le cours dit « non spécifique »), Q5-A « sécrétion » verbatim (le cours dit libération).

## Clôture bi-06 (2026-10-29)
- [x] Images 21/21 présentes : 19 planches générées relues (lots 1+2) + 2 composites propres (`ff-seuils`, `total`, assemblés depuis les planches générées — cap plateforme 10 images/tour ; **à régénérer en planches dédiées par le nouvel agent, 2 appels**).
- [x] Audio 10/10 (ch1–8 + résumé FR court + résumé AR). ⚠ Incident 29/10 : reset nocturne de `/tmp` → MP3 du 28/10 perdus, **régénérés à l'identique** depuis `audio-scripts.md` (voix de session encore valides).
- [x] Page : dims `width/height` recollées aux dimensions réelles des planches du lot 2 (1693×929/1774×887) — page repo = page livrée.
- [x] Contrôle refs bi-06 : 34/34 résolues. (Audit site complet à refaire après reconstruction de la base — voir HANDOFF §Étape 0 ; dernier audit complet 28/10 : 61 pages, 11 AN-06.)
- [x] **Livraison Drive `02_LIVRAISON-bi-06_2026-10-29`** (dossier `1VDAoeTxUWiM4o6J8Bq503x-B1CzsE1OK`) : ZIP `1oZixx-zRQDwsRiewm9QEQLWEbCzpJ94f` — 9 681 368 o, MD5 `5d3e62d5d9a437af37a8ec5f9b115e3c`, 37 fichiers (bi-06 complète + page bi-05 corrigée + data.js) ; LISEZ-MOI `1zYRioIZx_idpSyBdirVZ8vMDmCRio5-M`.
- Suite : voir `SEENmed-REPRISE/HANDOFF-NOUVEL-AGENT.md` (passation complète au nouvel agent).
