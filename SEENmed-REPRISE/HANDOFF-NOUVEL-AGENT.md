# SEENmed — HANDOFF COMPLET POUR LE NOUVEL AGENT (2026-10-29)

> **Tu reprends ce projet à froid.** Ce fichier contient tout : le produit, l'état exact, les sources, les recettes, les pièges vécus et la façon dont l'utilisateur veut travailler. Lis-le **en entier** avant d'agir, puis exécute l'**Étape 0** (§1.5). Langue du projet : **français** (le site est FR + arabe). L'utilisateur te parlera souvent en anglais simple — réponds **court**.
>
> Documents qui font foi (dans cet ordre) : **ce fichier** → `SEENmed-REPRISE/03-DETAILS-LOCK.md` → `04-PROTOCOLE-SOURCES-ET-VERSIONS.md` → `02-PLAN-26-NOVEMBRE-2026.md` → `DECISIONS-UTILISATEUR-2026-10-28.md`. Le dossier `handoff-ancien-agent/` (dont `START-HERE-FOR-NEW-AGENT.md`) est l'œuvre d'un agent précédent : **ne le suis jamais aveuglément** (consigne explicite de l'utilisateur : « if followed him we will fall in problems »). Vérifie tout ce qu'il affirme.

---

> **MISE À JOUR 4 AGENTS (2026-10-29)** : coordination multi-agents, verrous anti-doublons, discipline de quotas et **qualité image v2** = lire **`coordination/PROTOCOLE-4-AGENTS-v1.md`** (aussi sur Drive, dossier `01_COORDINATION-4-AGENTS_2026-10-29` ID `1P_NzJcrBQIbUc9r0JjXzmb0Lk-C8XTsA`). Il prime sur ce HANDOFF pour ces sujets. pn-01/pn-04 sont livrées (AGENT-2), pn-07 lui est réservée.
>

## ⚠ ADDENDUM (2026-10-29) — MODE SANS GITHUB : LIS-MOI EN PREMIER

Ton chat n'a **pas accès à GitHub** : le repo ne te sert à rien et tu ne peux ni le lire ni y écrire. **Tout se fait sur Google Drive** (connecté). Adaptations obligatoires du reste de ce document :

1. **Point de départ** : le dossier Drive **`00_KIT-NOUVEL-AGENT_2026-10-29`** (ID `1bHMhdFd94LIgR_GD9vIkv2zMRK-KjFYI`) contient ce fichier + **`KIT-NOUVEL-AGENT_SEENmed_2026-10-29.zip`** = l'intégralité de `SEENmed-REPRISE/` (docs 00→05, DETAILS-LOCK, protocole des sources, chartes, `tools/audit_seenmed.py`, builders et artefacts complets de bi-05/bi-06). Télécharge le ZIP (`google_drive__download_file`), il atterrit dans `google_drive/` de ton workspace : dézippe-le et travaille dans le `SEENmed-REPRISE/` obtenu — tous les chemins « repo » de ce document désignent ce dossier dézippé.
2. **Reconstruction de la base** : inchangée (§1.5, étapes 2→3e — elle était déjà 100 % Drive), **plus** l'application du delta **`03_DELTA-bi-06-final_2026-10-29`** (ID `1E_2B9t-Ezsntq1jFF-XSzxOFy7g8JE82`) après le 02. Ignore §1.1-2 (Git), §1.3 et §1.4 : pas de `.gitignore` chez toi, mais garde son esprit (ne stocke durablement dans ton workspace ni le site complet ni les archives — tout finit sur Drive).
3. **En remplacement des commits** : pour chaque leçon terminée, dans le même dossier Drive de livraison que le ZIP utilisateur (§9), uploade en plus un **`ARTEFACTS-<id-leçon>.zip`** contenant `PLAN-SOURCE.md` + `build_<id>.py` + `audio-scripts.md` + la page HTML + le `data.js` final + les WebP finaux. **Aucun artefact ne doit exister uniquement dans ton workspace à la fin d'un tour** (les workspaces d'agents sont éphémères — même maladie que `/tmp`, §1.1).
4. **Le §10.0 (micro-tâches bi-06) est DÉJÀ FAIT** le 29/10 par l'agent précédent : les 2 planches dédiées (`ff-seuils`, `total`) ont été régénérées et livrées par le delta 03. bi-06 est à 100 %. Ta première construction = **pn-01** (§10.1).
5. Si GitHub redevient accessible un jour : le repo `AbidMohamedYacine/medecine-study` contient le même contenu que ce kit (branche `arena/6cbc9050-medecine-study`, PR #1) — archive froide, pas un prérequis.

---

## 0. LA MISSION

- **Utilisateur** : étudiant en 3ᵉ année de médecine (Algérie, Oran). **Examen le 26/11/2026** (pneumologie incluse ; immunologie + anatomo-pathologie = fin janvier 2027). **Gel des constructions à J-7 (≈ 19/11/2026)** : après, révision seulement.
- **Produit** : **SEENmed**, un site statique hors-ligne de révision (HTML/CSS/JS vanilla, aucune étape de build). Chaque leçon = 1 page HTML riche (résumé FR intégralement traduit en arabe, planches illustrées, documents originaux du cours, QCM d'annales authentiques + entraînement, fiche flash, mots-clés, flashcards, « Ciné-révision » audio raconté).
- **État au 29/10/2026** : **61 leçons ouvrables** (59 base + bi-05 + bi-06 livrées). **21 leçons manquantes** pour novembre (liste et ordre §10). Dernier audit complet (28/10) : 61 pages, 0 inaccessible, **11 refs cassées = les 11 images d'an-06 jamais livrées** (perdues partout, **ne pas les rechercher** ; à régénérer en janvier si l'utilisateur le demande).
- **Ta mission** : construire les leçons manquantes **dans l'ordre du plan (§10)**, au même standard que bi-05/bi-06, en enchaînant leçon après leçon sans attendre d'autre feu vert que les « GO » qui débloquent tes quotas d'images/audio.

---

## 1. OÙ VIT CHAQUE CHOSE (STOCKAGE — CRITIQUE)

### 1.1 Les trois lieux
1. **Google Drive de l'utilisateur** = la sauvegarde du SITE COMPLET et des livraisons. **Le site complet ne doit JAMAIS vivre durablement dans le workspace Git** (repo déjà à ~132 Mo, consigne stricte de l'utilisateur).
2. **Repo GitHub `AbidMohamedYacine/medecine-study`** = docs de méthode, builders Python, pages des nouvelles leçons, planches WebP finales, scripts audio, plans-sources. **Jamais** : ZIP, MP3, PNG bruts (voir `.gitignore` §1.4).
3. **`/tmp/seenmed-clean/medstudy/`** = copie de travail du site complet (pour construire + auditer). ⚠️ **`/tmp` EST ÉPHÉMÈRE** : le 29/10 au matin, un reset nocturne a effacé la base de travail et 9 MP3 générés la veille (régénérés depuis les scripts Git). **Règle d'or n°1 : tout artefact produit un jour donné doit finir le MÊME JOUR soit committé (Git), soit livré (Drive).** Ne laisse jamais un résultat important uniquement dans `/tmp`.

### 1.2 Drive — IDs exacts (vérifiés)
| Élément | ID Drive | Notes |
|---|---|---|
| `00_BASE-OFFICIELLE_2026-10-28` (dossier) | `1O5QMhvttWd402VUjfyQwAaDeJRfRIvnK` | **Seule base officielle.** Ne jamais utiliser d'autres archives du Drive. |
| LISEZ-MOI de la base | `1J3JpqFaUgNvwCWsn_hEOEbG0RINok2T5` | Contient la procédure d'assemblage + MD5 : **relis-le avant de reconstruire**. |
| Base, partie 1 | `12ECuJ6UrNK5AoTi8uBCGwmtfXPtCEl7A` | Archive splittée (4 parties) → `medstudy/` 59 leçons |
| Base, partie 2 | `10EfosbTSIWDoyMaOIVeF2NRRZey4yG88` | MD5 vérifiés le 28/10 |
| Base, partie 3 | `1WxOEFavFs5wJDDfoTlLWHTwu-MD78MeG` | |
| Base, partie 4 | `1PZQD4pEnSlmqYfGhGxc3yijOp3_ZRXzX` | |
| `01_LIVRAISON-bi-05_2026-10-28` (dossier) | `17NO7hGnfkpPEvdWPMYMozVHqooqBZCfj` | ZIP `1fQBk18KnKVHXvSqm4EZZ4TxmGXxuac6n` (10 066 456 o, MD5 `9a9c50c8f018bb1026b500d7abcab7ee`) + LISEZ-MOI `1t68NgloBQFOsDpfzOocxEGrAfTf_tn0m`. ⚠️ **La page bi-05 de ce ZIP est OBSOLÈTE** (pré-correction « peau ») : la bonne est dans la livraison 02 et dans le repo. |
| `02_LIVRAISON-bi-06_2026-10-29` (dossier) | `1VDAoeTxUWiM4o6J8Bq503x-B1CzsE1OK` | ZIP `1oZixx-zRQDwsRiewm9QEQLWEbCzpJ94f` (9 681 368 o, MD5 `5d3e62d5d9a437af37a8ec5f9b115e3c`) + LISEZ-MOI `1zYRioIZx_idpSyBdirVZ8vMDmCRio5-M`. bi-06 complète + page bi-05 corrigée + data.js à jour. |
| Cours N-1 « MedHaven » (dossier sources) | `1-1qmHESAhjsYMXaiVULwb1LCYCNLRfyr` | Cours de l'année précédente = sources de construction (§2) |
| Cours N « UE 1: Cardio » (dossier sources) | `12lKQj0teZe40WzK6nz3EmpixJYBqRfhH` | Cours de cette année, quand ils existent → patch différentiel (§2) |

**Règles Drive absolues** : toute livraison = **nouveau dossier daté** `NN_LIVRAISON-<leçon>_AAAA-MM-JJ` + ZIP delta + `LISEZ-MOI` (installation en 30 s + contenu + MD5). **Jamais écraser, jamais supprimer** les archives/dossiers existants de l'utilisateur.

### 1.3 Repo — branche et règle de fusion
- Tout le travail récent (ce dossier `SEENmed-REPRISE/`, bi-05, bi-06) est sur la branche **`arena/6cbc9050-medecine-study`** (poussée sur GitHub, dernier état : bi-06 terminée). `main` (19cd208) ne contient QUE les PDF d'origine.
- ⚠️ **Si ton chat démarre depuis `main`, tu ne verras pas `SEENmed-REPRISE/`** tant que l'utilisateur n'a pas fusionné la PR ouverte depuis `arena/6cbc9050-medecine-study`. Première vérification : `ls SEENmed-REPRISE/` ; si absent → dis-le à l'utilisateur en 1 ligne (il doit merger la PR, ou te faire travailler sur cette branche). Ne reconstruis jamais ce qui existe déjà dans la branche.
- La racine du repo contient ~60 PDF de cours d'origine (ne pas supprimer/déplacer en masse ; le nettoyage de repo validé est limité au périmètre des leçons produites — voir `05-NETTOYAGE-REPO.md`) dont **`ELITE CARDIO 3EME.pdf`** = recueil d'annales + corrigés officiels (ta matière QCM, §3).

### 1.4 `.gitignore` (déjà en place — respecte-le)
`google_drive/` (zone d'atterrissage des téléchargements Drive : tout fichier téléchargé doit être **déplacé immédiatement vers `/tmp`**), `*.zip/7z/rar`, PNG/JPG bruts sous `travail/*/img/`, `*.mp3`. En Git : docs `.md`, builders `.py`, pages HTML des nouvelles leçons, **WebP finaux uniquement**, copies de `data.js`.

### 1.5 ÉTAPE 0 — ta première session, dans l'ordre
1. Vérifie la présence de `SEENmed-REPRISE/` (sinon cf. §1.3). Lis ce fichier + `03-DETAILS-LOCK.md` + `04-PROTOCOLE-SOURCES-ET-VERSIONS.md`.
2. Environnement Python : `pip install --target /tmp/pylibs pillow pymupdf` (l'installation système est bloquée PEP 668) ; toujours `PYTHONPATH=/tmp/pylibs`.
3. **Reconstruis la base de travail** (elle n'existera pas dans ton `/tmp`) :
   a. Charge le connecteur : `list_connector_tools("google_drive")` (**à chaque tour**, voir §11), outils = `google_drive__download_file`, etc.
   b. Lis le LISEZ-MOI de la base (`google_drive__read_file_text`, ID `1J3JpqFa...`) pour la procédure exacte et les MD5 attendus.
   c. `download_file` × 4 parties → elles atterrissent dans `google_drive/` du workspace → déplace-les vers `/tmp/`, assemble/dézippe selon le LISEZ-MOI → `/tmp/seenmed-clean/medstudy/` (59 leçons).
   d. Applique les deltas : livraison **01** (images+audio bi-05 ; **pas sa page**, obsolète) puis livraison **02** (bi-06 complète + page bi-05 corrigée + `js/data.js` final). Équivalent rapide pour les pages/data : repo `travail/bi-05-lipides/page/` et `travail/bi-06-biomarqueurs/page/` (le `data-apres-bi06.js` est le data.js cumulatif final) ; images des deux leçons aussi dans le repo (`travail/*/img/`) ; **les MP3 ne sont que dans les ZIP Drive 01/02**.
   e. Audit : `PYTHONPATH=/tmp/pylibs python3 SEENmed-REPRISE/tools/audit_seenmed.py /tmp/seenmed-clean/medstudy` → attendu : **pages 61, unreachable NONE, TOTAL broken refs 11 (an-06 uniquement)**. Tout écart = delta mal appliqué, corrige avant de construire.
4. Dis à l'utilisateur, en **5 lignes max** : base reconstruite + audit conforme + micro-tâche bi-06 (§10.0) + prochaine leçon = **pn-01**. Puis attends son « GO » (ou enchaîne directement s'il l'a déjà donné dans son message d'ouverture).

---

## 2. LES SOURCES DES COURS (jamais inventer)

- **Règle d'or n°2 : source lue EN ENTIER avant d'écrire une ligne** (texte + images extraites + pages rendues si besoin). Jamais inventer un contenu, un chiffre, un corrigé, une étape.
- **Cartographie complète** (quelle source pour quelle leçon, IDs Drive, drapeaux) = **`SEENmed-REPRISE/04-PROTOCOLE-SOURCES-ET-VERSIONS.md`** — ne re-cartographie pas, utilise-la. État : **21/22 leçons sourcées** sur les cours N-1 (MedHaven). **Seule ra-05 est sans source** (séances 09.10 KLOUCHA / 13.10 BELMESSABIH, aucun fichier nulle part) → **bloquée** tant que l'utilisateur n'obtient pas le PDF ; ne la construis pas, signale-la brièvement quand tu passes devant dans le plan.
- **Protocole N-1 → N** (dans le fichier 04) : on construit **maintenant** sur la source N-1, avec **empreinte de source obligatoire** dans le `PLAN-SOURCE.md` de la leçon (fichier, ID Drive, taille, MD5, pages/diapos, enseignant, année). Quand le PDF de l'année N arrive : **patch différentiel ciblé** (seules les infos nouvelles/différentes ; texte, puis images/voix si nécessaire) — **jamais de reconstruction**.
- Drapeaux connus (détail dans 04) : **pn-05** source de 157 Ko à vérifier à l'ouverture ; **pn-11** en `.docx` ; **psy-06** = PDF 6,6 Mo (**jamais** le pptx de 1,23 Go qui traîne à côté) ; notions parfois testées en annales mais absentes des diapos → les enseigner **au niveau exact des annales** et les signaler « à confirmer sur le cours » (ex. bi-06 : ASAT/LDH, copeptine/h-FABP, VPN/VPP).
- **Téléchargement** : `google_drive__download_file` (ID depuis le fichier 04) → fichier dans `google_drive/` → `mv` immédiat vers `/tmp/sources/<id-leçon>/`. Extraction : PyMuPDF (texte par page → JSON/TXT **lu en entier**, images natives). Pour PPTX : python-pptx (aussi dans /tmp/pylibs si tu l'installes).
- **Images du cours (« reels »)** : les PDF de diapos convertis ont souvent des fonds à canal alpha qui sortent **noirs** à l'extraction RGB — n'insiste pas ; garde uniquement les vrais schémas/photos lisibles (bi-06 : 3/21 seulement). Convertis les reels en **WebP qualité 90**, stockés `assets/img/<id>/reel/` (site) + `travail/<leçon>/img/reel/` (repo), affichés en `.reel-strip` avec mention « Document original du cours » + source (enseignant, page).

---

## 3. LES ANNALES (élément différenciant — authenticité totale)

- Recueil : **`ELITE CARDIO 3EME.pdf`** à la racine du repo (annales + corrigés officiels, par module et par chapitre, PROMO 2018→2022). Extrais les pages du chapitre de ta leçon (PyMuPDF), **relis-les sur le texte extrait** (le fichier 04/d'autres documents donnent parfois les numéros de pages — vérifie toujours dans le PDF).
- **Verbatim strict** : énoncés et propositions **dans l'ordre et le texte d'origine** (nettoyage typographique minimal des sauts de ligne d'extraction), réponses = **corrigés officiels du recueil** (champ `data-answer`). Aucune question inventée ou « réparée ».
- **Corrigés anciens parfois imparfaits** (vécu bi-06 : Q4-D « pro-BNP molécule de choix » validée alors qu'on dose BNP/NT-proBNP ; Q6-D « myoglobine peu sensible » alors que le cours dit « non spécifique ») : **garde le verdict officiel** et ajoute dans ta correction une **nuance honnête explicite** (« retiens-le pour cette annale ; en clinique/nouvelle question, c'est X »). C'est un trait de qualité signature du projet.
- **Leçon apprise à ne jamais refaire** : ne reconstruis JAMAIS les annales de mémoire ou depuis un résumé — toujours depuis l'extraction du PDF sous les yeux (le 28/10, un bloc annales reconstruit de mémoire a dû être jeté et réécrit après re-vérification).
- **Calibration de l'entraînement** : compte la distribution du nombre de bonnes réponses des vraies annales du chapitre (bi-06 : 1 rép.×2, 2×1, 3×6, 4×1) et calque tes 20 QCM d'entraînement dessus (bi-06 : 4×1, 2×2, 12×3, 2×4). Annonce la calibration dans la section Méthode.

---

## 4. ARCHITECTURE D'UNE PAGE LEÇON (le standard « gold »)

### 4.1 Le site
- `medstudy/index.html` (tableau de bord + modules), `progression.html`, `js/data.js` = **registre des 92 leçons**, `lecons/<id>-<slug>.html`, `assets/img/<id>/…`, `assets/audio/<id>/…`, `js/` (moteurs : navigation leçon, QCM, Ciné, flashcards, mots-clés, langue FR/AR, fonds par module).
- Page gold de référence structurelle (à cloner comme squelette) : **`lecons/ra-02-ultrasons-echographie-thoracique.html`**. Nouvelles pages modèles complètes : `bi-05-lipides-lipoproteines.html`, `bi-06-biomarqueurs-cardiaques.html` (aussi dans le repo `travail/*/page/`). ⚠️ an-01 n'est PAS un modèle (markup QCM seulement).

### 4.2 `data.js` — schéma exact (vérifié)
Guillemets **simples**, champs `id`, `nom`, `qcm`, `entr`, `recu`, `url`. Une leçon manquante a une ligne courte :
```js
{ id: 'bi-06', nom: 'Les biomarqueurs cardiaques', qcm: 10, recu: false },
```
Une fois construite, remplace-la par le format complet (même indentation que les voisines) :
```js
{ id: 'bi-06', nom: 'Les biomarqueurs cardiaques', qcm: 10, entr: 20, recu: true,
  url: 'lecons/bi-06-biomarqueurs-cardiaques.html' },
```
`qcm` = nombre d'annales réelles du chapitre, `entr` = 20 (standard entraînement). Ne touche à rien d'autre dans le fichier.

### 4.3 Squelette d'une leçon (onglets, dans l'ordre)
`vue` (Vue d'ensemble : essence en 10 puces + feuille de route + boîte Transparence-source) · `mindmap` · `cine` (Ciné-révision, `<div id="cinePlayer">`) · **sections numérotées** (12–14, chacune : numéro coloré, titre, sous-titre `.lsub` traduit, planche, `cine-spot`, boîtes `.lbox`/`.mini-card`/`.ltable`, éventuel `.reel-strip`, et encadré final `.qcm-focus` « Ce que l'examinateur peut fabriquer avec cette seule section ») · `methode` (la méthode de l'examinateur déduite des vraies annales + calibration) · `connexions` (liens inter-modules) · `annales` (QCM authentiques) · `entrainement` (20 QCM) · `fiche` (Fiche flash : 6 cellules visuelles sans texte suivi + « à dire à voix haute en 20 s ») · `flashcards` (`<div id="flashApp">`) · `resume-total` (grande planche poster + spot résumé).

### 4.4 Markup à respecter (le JS du site s'y branche)
- Sections : `<section class="lsection" id="…">`, tête `.lsection-head` > `.lsection-num` (+ `.n<num>` ou `.icon-only`), sous-titre `<div class="lsub" data-tr="clé">FR</div>`.
- Boîtes : `.lbox.reveal[data-tr]` (`.lbox-title` + `<ul>`), `.mini-card.acc-<couleur>.reveal[data-tr]` (`<h4>` + `<ul>`) en `.lgrid2` ou `.mini-grid cols-3`, tableaux `.ltable-wrap` > `table.ltable[data-tr]` (la version AR contient le tableau entier `thead+tbody`).
- Images : `<figure class="section-visual reveal"><img src="../assets/img/<id>/x.webp" alt="description FR complète" loading="lazy" width height><figcaption>💡 …</figcaption></figure>` ; hero en `loading="eager"` ; poster en `.total-poster` ; fiche en `.flash-grid>.flash-cell`.
- Ciné inline par section : `<div class="cine-spot reveal" data-ch="N"></div>` (**0-based** : chapitre 1 = `data-ch="0"`).
- QCM : `.qblock` (annales : +`.ann-block` et badge « Annale réelle » + `.qsource` « PROMO AAAA ») avec `data-answer="A,C"`, `.qhead` (`.qnum`), `.qtext`, `.qoptions` > 5 × `<label class="qopt"><input type="checkbox" value="A"><span class="qletter">A</span><span>…</span></label>`, bouton `.qcheck`, correction `<div class="qexp" data-tr="…" hidden>` commençant par `.qexp-ans`. Scores : `<div class="score-box" id="annalesScore">` / `id="entrScore"`.
- Données JSON en fin de page (ordre gold ci-dessous) : `#cineData` `{chapters:[{title, audio, audioAr?, images:[]}]}` · `#kwData` `{items:[{t,d,a:{t,d}}]}` (mots-clés FR + AR) · `#fcData` `[{q,a}]` (flashcards FR) · `#arData` `{clé: HTML arabe}`.
- **Fin de page gold (ordre exact, ne le casse jamais)** : [dernière section] → `<script … id="cineData">` + `id="kwData"` **dans `<main>`** → `</div>` conteneur → `</main>` → `<footer class="footer">` (3 boutons : « Retour au tableau de bord » → `../index.html` ; « Autre leçon : X » → **un fichier qui existe** ; « Revoir la leçon » → `#vue` ; ligne `© SEENmed — Leçon « Titre » · Module · Prof`) → `<div id="scrollProgress"></div>` → `<button id="backToTop">` (coin bas — **l'utilisateur y tient** : « include the back to the beginning button in the bottom like the other pages ») → `id="fcData"` + `id="arData"` → scripts du site (dont le **script de fond du module**, §4.5).
  - ⚠️ N'invente **aucun lien** : `a-propos.html` et `contact.html` n'existent pas dans la base (vécu : un footer maison a créé 2 refs cassées). La racine ne contient que `index.html` + `progression.html`.

### 4.5 LA « PEAU » — le fond propre à chaque module (erreur vécue à ne jamais refaire)
Chaque module a **sa classe `<body>` et son script de fond**. Cloner le squelette d'un autre module sans re-peau = page au mauvais fond (vécu bi-05 v1, corrigée ensuite). **Vérifie toujours sur une page gold DU module** avant de construire ; valeurs vérifiées :

| Module | `<body class>` | Script de fond |
|---|---|---|
| Biochimie (bi-) | `has-bio-field` | `../js/bio-field.js?v=11` |
| Cardiologie (ca-) | `has-cardio-field` | `../js/cardio-field.js?v=4` |
| Radiologie (ra-) | `has-orbital-sphere` | `../js/lib/three.min.js` + `../js/orbital-sphere-bg.js?v=6` |
| Physiologie (ph-) | `has-hero-field` | `../js/hero-field.js?v=10` |
| Anatomo-pathologie (an-) | `has-hero-field` | `../js/organ-field.js?v=16` |
| Immunologie (im-) | `has-fluid-field` | `../js/fluid-field.js?v=10` |
| Sémiologie (sg-) | (vérifier) | `../js/cloud-field.js` |
| **Pneumologie (pn-), Psychiatrie/Psychologie (psy-)** | **NON vérifié** | **→ ouvrir une page gold du module et relever classe + script. Ne devine jamais.** |

Contrôle systématique avant de dire « fini » : `grep` sur ta page = 1× la bonne classe body, 1× le bon script de fond, 0× le fond du squelette d'origine (ex. `orbital`/`three.min` hors radiologie), 1× `scrollProgress`, 1× `backToTop`, 1× footer de leçon.

---

## 5. ÉCRIRE LE CONTENU (quantité + qualité cibles, mesurées sur bi-05/bi-06)

- **Par leçon** : 12–14 sections de contenu · **21–23 planches générées** (hero + mindmap + 1/section + 6 fiche-flash + 1 poster total) + reels du cours quand ils existent · **10 MP3** (8 chapitres FR + résumé FR + résumé AR) · annales = le nombre réel du chapitre (bi-05 : 15, bi-06 : 10) · **20 QCM d'entraînement** · ~36 mots-clés · 25 flashcards · **arabe complet** (~76–91 clés `data-tr`).
- **Sections** : sous-titre qui annonce l'enjeu (pas un résumé sec), planche en premier, 1 boîte principale dense (faits du cours, chiffres en gras), 1 élément de structuration (tableau ou paire de mini-cartes), encadré « pièges d'examinateur » ancré dans les vraies annales. Les 9 fabriques de pièges utilisées : ① adjectif dévoyé ② famille croisée ③ cause noyée ④ ordre de grandeur ⑤ inversion cause/effet ou stimulus ⑥ négation/absolu plaqué (« toujours », « uniquement », « jamais ») ⑦ extrapolation ⑧ permutation (valeurs/heures/rôles entre deux entités sœurs) ⑨ conclusion sans contexte.
- **Corrections QCM** : verdict + « Pourquoi » (le fait de cours) + « Pièges » (chaque distracteur jugé). Annales : référence PROMO + nuance si corrigé officiel imparfait (§3).
- **Ton** : professeur clair, connecteurs logiques, phrases complètes — **jamais télégraphique**, dans le texte comme dans l'audio.

### Traduction arabe (règles verrouillées)
- **Seuls les éléments `data-tr` sont traduits** (leurs HTML FR et AR doivent avoir la même structure : titres, listes, tableaux entiers). **Énoncés et propositions des QCM : toujours en français** (comme le jour de l'examen) ; seules les corrections (`.qexp`) sont traduites.
- **Arabe contextuel du sens**, pas mot-à-mot ; **les termes techniques français restent en français** dans la phrase arabe, balisés `<bdi class="fr-term">terme</bdi>` (mots) ou `<bdi class="fr-plain">CK-MB</bdi>` (sigles/chiffres). Arabe neutre, jamais d'accent khaliji dans l'audio.
- Invariant technique : ensemble des `data-tr` du HTML == ensemble des clés `#arData` (assert dans le builder).

---

## 6. LES IMAGES (méthode + limites dures)

- ⛔ **CAP PLATEFORME : 10 générations d'images PAR MESSAGE (tour).** Au 11ᵉ appel, tout le bloc échoue (« Image generation limit of 10 reached ») — et les tentatives comptent (un 429 fournisseur consomme aussi un slot, vécu sur le poster bi-06). **Planifie 10 planches maximum par tour, un seul bloc parallèle, prompts relus AVANT l'envoi.** Une leçon = 2 tours d'images (10 + ~11), le second tour pouvant enchaîner sur la leçon suivante.
- **Prompts** (ce qui marche) : en français, décrire scène + style (« illustration médicale moderne, fond clair, format paysage ») + **titres et chiffres français exacts entre guillemets** + « Aucun autre texte ». Planches fiche-flash : « sans aucun texte » (que des formes/chiffres/symboles). Aligne toujours prompt ↔ `alt` de la page.
  - Ex. qui a marché : « Graphique scientifique médical propre, fond clair… Titre en haut en français impeccable : « Cinétique des marqueurs après infarctus ». … courbe orange « Myoglobine : dès 2 h, pic 4–12 h, normale à 24 h »… Aucun autre texte. »
- **Après génération** : PNG → **WebP qualité 83** (planches ; reels 90) vers le site ET le repo, supprime les PNG (jamais en Git). **Relecture obligatoire** : planche-contact (vignettes 470 px, 2 colonnes) lue en entier + zooms pleine taille sur les planches chiffrées (les générateurs inventent parfois une valeur décorative, ex. « 152 ng/L » — acceptable comme décor, jamais comme seuil enseigné ; tout chiffre inexact ou texte garbled visible = régénérer au tour suivant, le signaler dans le PLAN-SOURCE).
- **Dimensions** : le générateur varie (1536×1024, 1693×929, 1774×887…). Les attributs `width/height` du HTML doivent être les **dimensions réelles** de chaque fichier (patch auto via PIL après conversion — le builder bi-06 doit être complété ainsi si régénération).

---

## 7. L'AUDIO « CINÉ-RÉVISION » (méthode + limites dures)

- ⛔ **CAPS : 10 clips par tour (les tentatives échouées COMPtent), 1500 caractères MAX par clip** (compte les caractères **avant** chaque appel ; vise ≤ 1400 pour les résumés). Vécu : un résumé FR de ~1600-1900 car. a brûlé 3 slots.
- **Structure** : 9 chapitres `cineData` = 8 chapitres FR regroupant les sections (images = planches des sections couvertes) + 1 « Résumé total » avec `audio` FR (`resume.mp3`, images: poster total + mindmap) et `audioAr` (`resume-ar.mp3`). Chemins : `../assets/audio/<id>/ch1..8.mp3`, `resume.mp3`, `resume-ar.mp3`.
- **Voix** : les IDs de voix sont **propres à la session/chat** (dans l'ancien chat : voice-00 FR, voice-01 AR — ils ne fonctionneront probablement pas chez toi). Procédure : `add_voice` (le tour se met en pause, **l'utilisateur écoute et choisit** — c'est la seule pause "autorisée", une fois par langue) puis `generate_speech`. Textes d'audition proposés : FR « Bienvenue dans cette leçon de biochimie. Aujourd'hui, nous explorons les marqueurs qui racontent l'état du cœur : de la troponine aux peptides natriurétiques, chaque molécule a son heure et son message. » ; AR « مرحباً بك في درس الكيمياء الحيوية. اليوم نستكشف الواسمات التي تروي حالة القلب: من التروبونين إلى الببتيدات الناتريورية، لكل جزيء وقته ورسالته. »
- **Scripts** : narration fluide type professeur qui relie les idées (jamais de liste télégraphique), FR prononcé à la française, chiffres écrits en lettres dans le texte parlé quand ça aide (« une à deux heures »). **Toujours committer `travail/<leçon>/audio-scripts.md` AVANT de générer** (c'est ce qui a permis de régénérer 9 MP3 perdus à l'identique en 1 tour).
- MP3 hors Git (`*.mp3`) → ils ne sont en sécurité que dans le ZIP de livraison Drive : **livre le même jour que la génération** (§9).

---

## 8. LE BUILDER (comment les pages sont fabriquées)

- **Modèle vivant : `SEENmed-REPRISE/travail/bi-06-biomarqueurs/build_bi06.py`** (et `bi-05-lipides/build_bi05.py`). Principe : un script Python lit la page gold **ra-02** de la base reconstruite, en extrait `top` (head/hero — avec remplacements : `<title>`, `data-lesson-id`, **classe body du module**, fil d'Ariane, `<h1>`, chips, boutons, image hero), `nav` (tabs régénérés) et `bottom` (footer gold patché : lien « Autre leçon » + ligne copyright ; scripts d'origine remplacés par le **script de fond du module**), puis génère tout le corps via des helpers (`sub`, `lbox`, `mini`, `grid2`, `fig`, `spot`, `focus`, `reels`, `table`, `section`) qui accumulent le dictionnaire arabe `AR` en parallèle.
- Écrit en **parties concaténées** (q1 squelette+vue, q2 sections 1-6, q3 sections 7-12+méthode, q4 annales+entraînement, q5 fiche/kw/fc/ciné/assemblage+data.js) — pratique pour écrire gros sans dépasser les limites par appel d'écriture ; le fichier committé est la concaténation.
- **Validations intégrées au builder (garde-les toutes)** : parse JSON des 4 blocs ; `arData == data-tr` ; nombre de `.qcheck` == annales+20 ; aucun `.png` ; peau (classe+script+backToTop ==1) ; liste des images référencées manquantes (les `?v=` et `#ancres` signalés sont des **faux positifs** — seul `tools/audit_seenmed.py` fait foi pour le site entier).
- **Pièges vécus** : chemin three = `js/lib/three.min.js` (pas `vendor/`) ; les JSON cine/kw vont **dans `<main>`** avant sa fermeture ; apostrophes françaises dans les chaînes Python simples → échapper ou guillemets doubles ; greps shell complexes chaînés → `shell_error`, préfère des commandes simples ou Python ; patch `data.js` doit être idempotent (relancer le builder ne doit pas casser).

---

## 9. FINIR UNE LEÇON (checklist de clôture, dans l'ordre)

1. Page construite, validations builder vertes ; contrôle peau (§4.5) ; contrôle refs de la leçon = 0 manquante.
2. `data.js` patché (§4.2) ; **audit officiel** : seul écart toléré = 11 refs an-06.
3. Copie les artefacts dans le repo : `travail/<leçon>/` = `PLAN-SOURCE.md` (à jour, cases cochées), `build_<id>.py`, `audio-scripts.md`, `page/<page>.html`, `page/data-apres-<id>.js`, `img/*.webp` (+ `reel/`).
4. **Commit + push** sur ta branche de session (message clair : « <id>: leçon terminée + livraison »). Étapes : édite d'abord, vérifie `git status`, puis `git add` (évite add en parallèle d'une édition — staging raté vécu).
5. **Livraison Drive** : arbre delta `medstudy/{lecons/<page>.html, js/data.js, assets/img/<id>/**, assets/audio/<id>/**}` (+ toute page corrigée en attente) → ZIP dans le workspace (ex. `SEENmed_DELTA-<id>_AAAA-MM-JJ.zip`, gitignoré) → `md5sum` → `LISEZ-MOI-<id>.txt` (installation : « dézippe PAR-DESSUS ton dossier medstudy actuel », contenu chiffré, notes honnêtes) → `google_drive__create_file {name:"NN_LIVRAISON-…", mime_type:"application/vnd.google-apps.folder"}` → `google_drive__upload_file {file_path, name, parents:[idDossier]}` ×2 (≤100 Mo, depuis le workspace) → vérifie les **tailles** retournées == locales.
6. Mets à jour le `PLAN-SOURCE.md` (IDs de livraison + MD5) et committe.
7. **Enchaîne sur la leçon suivante du plan sans attendre** (si le tour a encore du quota images/audio, utilise-le pour elle).

---

## 10. CE QUI RESTE À FAIRE (ordre = `02-PLAN-26-NOVEMBRE-2026.md`)

### 10.0 Micro-tâches immédiates (avant pn-01, dans ton premier tour)
- **Régénérer en planches DÉDIÉES** les 2 composites provisoires de bi-06 : `ff-seuils.webp` (aide-mémoire sans texte suivi : échelle hs-CRP 1/3 mg/L + horloges 1–2 h / 3–6 h / 10 j) et `total.webp` (poster « Les biomarqueurs cardiaques », 3 colonnes NÉCROSE/FONCTION/INFLAMMATION + bandeau STEMI/NSTEMI — prompt complet dans le PLAN-SOURCE bi-06 / historique : réécris-le proprement). Remplace site+repo, recolle les dims réelles dans la page (repo + site), inclus les 2 fichiers dans ta prochaine livraison delta (ou micro-delta nommé `02b`). **Préviens l'utilisateur en 1 ligne.**

### 10.1 Les 21 leçons manquantes (priorités mesurées aux annales ELITE)
- **Tier S** : ~~ra-05 (17 QCM)~~ **BLOQUÉE** (pas de source, §2) · ~~bi-05 ✔~~ · ~~bi-06 ✔~~ · **pn-01 (6)** · **pn-04 (8)** · **sg-05 (8)**
- **Tier A** : pn-07 · pn-05 · pn-03 · pn-08 · pn-11 · sg-04 · bi-04
- **Tier B** : pn-02 · pn-06 · pn-09 · pn-12 · pn-10 · ph-09 · psy-09 · psy-08 · psy-06
- Hors novembre (janvier) : immuno/anapath restantes + régénération des 11 images an-06. **AN-11+** : hors base de travail (décision utilisateur — les originaux Drive intacts, n'y touche pas).
- Pour chaque leçon : source + ID + nombre d'annales exacts = fichier **04** (et le PDF ELITE). Pour pn-*/psy-* : **relever d'abord la peau du module** sur une page gold (§4.5).

---

## 11. LIMITES PLATEFORME & OUTILS (tout ce qui a mordu, pour ne pas te faire mordre)

| Limite | Détail vécu | Parade |
|---|---|---|
| Images **10/tour** | 11ᵉ appel = tout le bloc refusé ; les échecs (429 inclus) consomment des slots | Compter avant d'envoyer ; 1 seul bloc ≤10 ; prompts relus |
| Audio **10 clips/tour**, **1500 car./clip** | Tentatives échouées comptées ; résumé >1500 = slots brûlés | Compter les caractères avant ; résumés ≤1400 car. |
| Voix TTS | IDs valables pour **ce chat seulement** | Refaire `add_voice` (pause choix utilisateur, 1×/langue) |
| **Quota journalier** du compte | Avertissement « close to your usage limit for today » après une journée très lourde | Zéro appel gaspillé ; réponses courtes ; artefacts sauvés au fil de l'eau (si le quota coupe, tout est déjà en Git/Drive) |
| Connecteurs (Drive…) | Outils à **recharger à chaque tour** : `list_connector_tools` puis `google_drive__<outil>` | Le faire en tout début de tour qui touche Drive |
| Drive par curl | Inutilisable | Uniquement les outils connecteur |
| `upload_file` Drive | Fichier du **workspace**, ≤100 Mo | ZIP delta par leçon (~10 Mo) : largement OK |
| Internet sandbox | Hôtes autorisés seulement : github, npm, pypi… | Pas de téléchargement web direct hors liste |
| Python système | PEP 668 | `pip install --target /tmp/pylibs …` + `PYTHONPATH=/tmp/pylibs` |
| `/tmp` | **Reset nocturne possible** (vécu 29/10) | Règle d'or n°1 (§1.1) ; reconstruire la base à chaque nouvelle session |
| Shell | Greps complexes → `shell_error` | Commandes simples ; l'outil d'audit fait foi |
| Git | `edit_file` + `git add` en parallèle = staging parfois raté | Éditer, `git status`, puis add/commit |

---

## 12. COMMENT TRAVAILLER AVEC CET UTILISATEUR (ses consignes, textuellement)

- **« GO » = sature le tour** : utilise tout le quota utile (jusqu'à 10 images + 10 audios) pour finir une leçon en **2–3 messages**, contrôles qualité inclus dans le tour, **zéro pause pour une broutille**. Rythme convenu : GO 1 = source + images lot 1 + page complète + intégration + audit ; GO 2 = images lot 2 + audio + livraison (+ début de la suivante s'il reste du quota).
- **Ne t'arrête pas** : leçon finie et confirmée → enchaîne la suivante du plan sans attendre un nouveau GO. Arrêts légitimes, et eux seulement : source absente (ra-05), contradiction réelle source/annales, choix de voix à auditionner, cap plateforme atteint (dis-le en **1 ligne** avec l'état exact).
- **Réponses COURTES et brèves** entre les tours (il l'a redemandé : « short brief responses ») : ce qui est fait / ce qui reste / prochain pas — en listes serrées, pas d'essais. La qualité se met dans les fichiers, pas dans le blabla.
- **Jamais dire « fini » pour du partiel.** Si 2 planches sont provisoires, dis-le (cf. bi-06 §10.0). Transparence totale sur les sources (boîte Transparence dans chaque leçon) et sur tes erreurs (corrigées + tracées dans le PLAN-SOURCE).
- **Jamais inventer** : contenu de cours, annales, corrigés, chiffres, liens, fichiers. En cas de doute réel et bloquant seulement : une question courte à l'utilisateur (il veut être « on the same page », mais déteste les interruptions pour des détails gérables).
- **Sois « a little smart »** : adapte chaque leçon à SON module et SON contenu (peau, exemples, connexions) au lieu de cloner aveuglément — c'est sa correction après l'erreur de fond de bi-05.
- Il ne veut **pas** trier/dézipper des choses lui-même au-delà de l'installation en 30 s : tu gères Drive, les ZIP, l'organisation. Ne lui demande jamais de token/mot de passe ; Git/GitHub/Drive sont déjà connectés côté Arena.
- **Stockage** : obsession légitime de l'utilisateur — le site complet vit sur **Drive** (base officielle + livraisons datées), le repo reste léger (méthode + artefacts par leçon). Aucune suppression sur son Drive, jamais d'écrasement.

---

## 13. FICHIERS DU REPO À CONNAÎTRE

- `SEENmed-REPRISE/` : `00-AUDIT-NEUTRE-2026-10-28.md` (état des lieux initial) · `01-DIAGNOSTIC-ET-REPARATION-2026-10-28.md` · **`02-PLAN-26-NOVEMBRE-2026.md`** (priorités) · **`03-DETAILS-LOCK.md`** (règles de méthode verrouillées + addendum peaux/fin de page — **à lire**) · **`04-PROTOCOLE-SOURCES-ET-VERSIONS.md`** (correspondances sources + IDs — **ta carte**) · `05-NETTOYAGE-REPO.md` · `DECISIONS-UTILISATEUR-2026-10-28.md` · `chartes-recuperees/` (CHARTE-IMAGES, CHARTE-IMMUNO…) · `tools/audit_seenmed.py` (**l'audit officiel**) · `travail/bi-05-lipides/` et `travail/bi-06-biomarqueurs/` (**modèles complets à imiter** : PLAN-SOURCE, builder, scripts audio, page, data.js, images) · `handoff-ancien-agent/` (⚠️ non autoritaire, §0).
- Racine : `ELITE CARDIO 3EME.pdf` (annales) + ~60 PDF de cours d'origine (matière brute de l'utilisateur — les sources de construction restent celles du fichier 04 sur Drive N-1).
- Par leçon, le `PLAN-SOURCE.md` est le journal de bord : empreinte source, plan de sections, cartographie annales, état d'avancement coché, incidents. **Tiens-le à jour en permanence** — c'est lui qui permet de reprendre après n'importe quelle coupure (quota, reset, changement d'agent).

---

*Bonne route. Le standard est bi-06 ; la source de vérité est lue, jamais devinée ; chaque tour compte. Premier message attendu de ta part : l'étape 0 (§1.5) exécutée et annoncée en 5 lignes.*
