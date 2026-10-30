# STANDARD-OR v3 — SEENmed

Version : 2026-10-30 · Autorité : moteurs réels du site (`lesson.js`, `cine.js`, `keywords.js`, `ar-mode.js`, `bg-mode.js`) + pages aimées **ca-02/ca-09**, squelette **ra-02**, modèle récent **bi-05**.

Ce document remplace les contrats interactifs faux du HANDOFF hérités du builder bi-06. En cas de conflit : **le code des moteurs gagne**, puis ce standard, puis les anciens builders. Une page n'est jamais `LIVREE` sur comptages de chaînes : elle doit passer l'audit v3, le test runtime et le contrôle visuel zoomé.

---

## 0. Règles qui ne changent pas

- Source lue en entier ; rien d'inventé (annales, corrigés, chiffres, diagnostics, étapes). N-1 → construction immédiate ; PDF N → patch différentiel seulement, avec empreinte de version.
- Un seul propriétaire par leçon (LOCK Drive). Registre/JOURNAL avant et après. `data.js` toujours depuis le dernier `data_COURANT`, une seule ligne touchée, jamais de renumérotation.
- Caps génération **par message utilisateur** : 10 images + 10 audios, tentatives et échecs compris. Un seul bloc compté/listé/vérifié. Après 10 succès d'un type, **jamais de second bloc dans le même message** ; aucun retry 429/cap dans le même tour.
- Livraison = nouveau dossier daté Drive + LISEZ-MOI + MD5. Jamais d'écrasement/suppression d'origine. Jamais « fini » pour du partiel.

## 1. Anatomie obligatoire d'une leçon

Ordre des sections = ordre des onglets, sans orphelin :

`vue → mindmap → cine → sections de contenu numérotées → methode → connexions → annales → entrainement → fiche → flashcards → resume-total`

Chaque section de contenu suit le rituel des références :

1. `.lsection-head` : numéro coloré `.lsection-num.nN`, titre, `.lsub` traduite (`data-tr`).
2. Planche principale `.section-visual` (voir §7), puis `.reel-strip` si le cours fournit un document réel utile.
3. **Mini-lecteur Ciné immédiatement sous la planche** (ou sous le strip réel qui la suit directement).
4. Une boîte principale `.lbox` qui enseigne le mécanisme, pas une paraphrase de la diapo.
5. En règle générale **deux `.mini-card`** dans `.lgrid2` (chiffres, mécanisme, cas, piège) ; un `.ltable` peut remplacer une carte quand la source est tabulaire.
6. `.qcm-focus` final : « Ce que l'examinateur peut fabriquer avec cette seule section ».

Densité de référence : ca-02 fait ~300–430 mots par section de contenu, avec 1 planche + souvent 1 strip réel + 2 mini-cartes. Une section faite uniquement de boîtes de texte empilées est un écart, pas une variante.

Fin de page : footer gold du squelette (3 boutons valides, ligne de leçon correcte), `#scrollProgress`, `#backToTop` uniques. Le bas cloné doit être **nettoyé** : ancien `#fcData`, ancienne peau/canvas/scripts, ancien lien « autre leçon » et ancien copyright sont des pièges connus.

## 2. Ordre des données et des scripts (bloquant)

Les moteurs lisent leurs JSON **à l'exécution du script**. Tous les blocs de données doivent donc précéder tous les moteurs :

```html
<script type="application/json" id="cineData">…</script>
<script type="application/json" id="kwData">…</script>
<script type="application/json" id="fcData">…</script>   <!-- UN SEUL -->
<script type="application/json" id="arData">…</script>
<script src="../js/bg-mode.js?v=14"></script>
<script src="../js/progress.js?v=6"></script>
<script src="../js/main.js?v=6"></script>
<script src="../js/<peau-du-module>.js"></script>
<script src="../js/lesson.js?v=12"></script>
<script src="../js/ar-mode.js?v=1"></script>
<script src="../js/keywords.js?v=2"></script>
<script src="../js/cine.js?v=3"></script>
```

Un ID dupliqué (`fcData` ×2) est bloquant : le navigateur ne lira que le premier.

## 3. QCM — contrat exact du moteur

Chaque section QCM porte `data-qcm-set` et un en-tête de score :

```html
<section class="lsection" id="annales" data-qcm-set="annales">
  …
  <div class="qcm-section-head reveal">
    <span class="chip chip-qcm"><i class="fa-solid fa-trophy"></i>
      Score de la session : <span class="qs-val">0 / 0</span></span>
    <span class="chip"><i class="fa-solid fa-circle-info"></i>
      Plusieurs réponses possibles — coche tout ce qui est juste</span>
  </div>
```

Chaque question :

```html
<div class="qblock reveal" data-answer='["B", "C"]'>
  <div class="qhead">
    <div class="qtext">1. Énoncé exact…</div>
    <span class="qsrc src-annale"><i class="fa-solid fa-landmark"></i> PROMO 2022</span>
  </div>
  <ul class="qch">
    <li data-l="A"><span class="ql">A</span><span class="qtxt">Proposition…</span><span class="xe"></span></li>
    <!-- … B C D E … -->
  </ul>
  <div class="qverdict"></div>
  <div class="qexp" data-tr="q01-exp">
    <div class="qexp-title"><i class="fa-solid fa-circle-check"></i> Correction, proposition par proposition</div>
    <div class="qexp-item f"><b>A — À NE PAS COCHER.</b> Pourquoi cette proposition précise est fausse…</div>
    <div class="qexp-item t"><b>B — À COCHER.</b> Pourquoi cette proposition précise est juste…</div>
    <!-- une ligne par proposition, dans l'ordre A→E -->
    <div class="qexp-memo"><i class="fa-solid fa-lightbulb"></i> Réponse BC. Le piège nommé, la phrase à retenir.</div>
  </div>
  <div class="qcheck-row"><button class="qcheck btn btn-primary btn-sm" type="button"><i class="fa-solid fa-check-double"></i> Corriger</button></div>
</div>
```

Interdits (variante bi-06) : `data-answer="A,C"`, `label.qopt/input[type=checkbox]`, `.qoptions`, `.qexp[hidden]`, `.score-box`, `#annalesScore`.

Qualité de contenu gold :

- Annales : verbatim + corrigé officiel ; toute divergence cours/corrigé est signalée dans la correction, jamais « réparée » en silence.
- Correction = **une raison par proposition** + mémo qui nomme le piège (caractère volé, absolu, côté/chiffre inversé, négation…). Cible mesurée sur ca-02/ca-09 : médiane ≥ 650 caractères par correction.
- La traduction arabe de `qexp` (via `data-tr`) garde la même structure `.qexp-item t/f` + mémo.
- Entraînement : calibration écrite avant génération (nombre de réponses justes, types de pièges) calquée sur les vraies annales du chapitre.

## 4. Ciné-révision — contrat exact du moteur

Section centrale obligatoire, juste après `mindmap` :

```html
<section class="lsection" id="cine">
  <div class="lsection-head">
    <div class="lsection-num icon-only"><i class="fa-solid fa-clapperboard"></i></div>
    <div>
      <h2>Ciné-révision — la leçon racontée</h2>
      <div class="lsub">… nombre de chapitres et langues réellement livrées …</div>
    </div>
  </div>
  <div id="cinePlayer" class="reveal"></div>
</section>
```

JSON lu par `cine.js` — et rien d'autre :

```json
{ "chapitres": [
  { "t": "Titre du chapitre", "imgs": ["../assets/img/<id>/planche.webp"],
    "fr": "../assets/audio/<id>/01-chapitre.mp3", "ar": null },
  { "t": "Résumé total", "imgs": ["../assets/img/<id>/total.webp"],
    "fr": "../assets/audio/<id>/resume.mp3", "ar": "../assets/audio/<id>/resume-ar.mp3" }
] }
```

Interdits : `chapters`, `title`, `audio`, `audioAr`, `images`.

- **Chaque section de contenu** reçoit `<div class="cine-spot" data-ch="N"></div>` sous sa planche, où N est le chapitre qui raconte réellement cette section. Un chapitre peut couvrir 1–2 sections adjacentes ; l'indexation est vérifiée section par section (le titre affiché par le mini-lecteur doit correspondre à la section).
- `resume-total` reçoit le spot du dernier chapitre (résumé).
- **Langues des pistes (décision utilisateur, 30/10/2026 — à ne jamais « améliorer »)** : les **chapitres sont en FRANÇAIS uniquement** (`"ar": null`) ; **seul le chapitre résumé (le dernier) existe en FR + AR**. C'est le modèle bi-05/bi-06/pn-01 (8 chapitres FR + résumé FR + résumé AR = 10 MP3). Les anciennes ca-02/ra-02 (AR partout) ne sont **pas** le modèle à reproduire pour les audios. Scripts gelés avant génération, narration professeur fluide, ≤ ~1 400 caractères par piste, chiffres en toutes lettres quand la prononciation l'exige. Site silencieux : rien ne démarre sans clic (`preload=none` géré par le moteur).

## 5. Mots-clés — contrat exact du moteur

`#kwData` est un **tableau**, dans l'ordre des sections :

```json
[ { "t": "Terme", "s": "id-section", "n": "3",
    "d": "Définition française courte, <b>mot-clé en gras</b>, avec le chiffre/piège utile.",
    "a": "التعريف بالعربية مع إبقاء <bdi class=\"fr-term\">terme</bdi> بالفرنسية عند الحاجة." } ]
```

- `s` = ID réel de la section où le terme est enseigné ; `n` = son numéro de section de contenu.
- Interdit : objet `{items:[…]}`, `a` en objet `{t,d}`.
- Couverture gold : viser la densité ca-02 (≈ 45–60 termes pour une leçon de 10–14 sections) : tous les termes techniques, sigles, seuils nommés et pièges lexicaux du cours. Une entrée qui n'est pas un terme (« Conclusion du cours ») n'a pas sa place dans le dictionnaire.

## 6. Flashcards — contrat exact du moteur

La section contient le deck complet (copié de ca-02/bi-05, jamais réinventé) :

```html
<div class="sr-panel reveal" id="fcDeck">
  <div class="sr-head">
    <div class="sr-count" id="fcCount"></div>
    <span class="chip chip-qcm"><i class="fa-solid fa-clock-rotate-left"></i> SM-2 : J+1 → J+3 → J+7 → J+16 → J+35</span>
  </div>
  <div class="fc-stage" id="fcStage">
    <div class="fc-card" id="fcCard">
      <div class="fc-face fc-front" id="fcFront"></div>
      <div class="fc-face fc-back" id="fcBack"></div>
    </div>
  </div>
  <div class="sr-controls">
    <button class="sr-btn again" id="fcAgain">…</button>
    <button class="sr-btn hard" id="fcHard">…</button>
    <button class="sr-btn good" id="fcGood">…</button>
    <button class="sr-btn easy" id="fcEasy">…</button>
  </div>
  <div class="sr-done" id="fcDone" style="display:none;"></div>
</div>
```

Données : un seul `#fcData`, avant les moteurs, chaque carte avec un `id` stable et unique :

```json
[ { "id": "c01", "q": "Question fermée ?", "a": "Réponse complète avec <b>les mots qui tombent</b>." } ]
```

Interdits : `#flashApp`, cartes sans `id`, second `fcData` hérité du squelette. Cible : 25–30 cartes couvrant toutes les sections, réponses relisables en 10 secondes.

## 7. Fiche flash — le composant des références

Format ca-02/ca-09 : **quatre macro-cellules** en 2×2.

```html
<div class="flashsheet ff-2x2 reveal">
  <div class="flash-cell fc-red">
    <h4><i class="fa-solid fa-…"></i> THÈME — angle d'examen</h4>
    <img class="flash-img" src="../assets/img/<id>/ff-theme.webp" alt="Contrat de contenu complet…" loading="lazy" width="1376" height="768">
    <ul>
      <li>★★ <b>Fait 1</b> : la phrase qui tombe, avec son chiffre.</li>
      <!-- 4 à 7 puces denses : faits, seuils, pièges, réflexes -->
    </ul>
  </div>
  <!-- fc-blue, fc-teal, fc-amber / fc-purple -->
</div>
```

Interdits : `.flash-grid`, `figure` + légende d'une ligne, image « sans texte suivi ». La fiche se relit la veille : l'image **et** la liste portent chacune l'essentiel. Cible texte ≥ 2 400 caractères sur la section (ca-02 : 2 499 ; ca-09 : 3 777). La boîte « à dire à voix haute en 20 secondes » peut suivre, elle ne remplace pas les listes.

## 8. Images — qualité v3 (remplace et durcit v2)

### 8.1 Contrat par planche, écrit AVANT génération

Pour chaque image générée, le builder/PLAN-SOURCE fige : section couverte, titre français exact affiché, 3–5 zones, libellés exacts en toutes lettres, chiffres/seuils, scène/anatomie, mécanisme/flèches, piège d'annales. Le `alt` de la page reprend ce contrat en français complet — jamais « illustration de… » générique.

### 8.2 À quoi ressemble la référence (ca-02/ca-09)

- Paysage **1376×768** pour toute planche générée (hero, mindmap, sections, ff-*, total). Les documents réels du cours gardent leurs dimensions d'origine.
- Fond contextuel **rempli** (scène d'urgence, paillasse, carnet, salle d'examen…) — jamais de blanc vide, jamais d'icônes flottant dans le vide.
- Composition en panneaux numérotés ou colonnes comparatives ; on voit **où c'est, à quoi ça ressemble, comment ça marche**, les connexions et les effets.
- Texte français lisible intégré : titres, étiquettes anatomiques, seuils, horloges, pièges. Les nombres sensibles sont écrits en toutes lettres dans le prompt si le générateur les déforme en chiffres.
- Une planche = une révision autonome en ~30 secondes. **Plusieurs images par section sont autorisées — et attendues — dès que le contenu l'exige** (décision utilisateur) : deux mécanismes distincts = deux planches (ca-09 le fait) ; anatomie, mécanisme, comparaison et piège peuvent chacun recevoir leur propre image. Il n'y a **aucun plafond d'une image par section** : seul le cap plateforme (10 images par message) règle le rythme, jamais le total d'une leçon. Chaque image ajoutée suit le même contrat §8.1, se place **sous le sous-bloc qu'elle illustre** (jamais en tas en fin de section) et doit correspondre **exactement** à ce passage — mêmes faits, mêmes chiffres, même vocabulaire que le texte voisin. Une image décorative ou « à peu près » est rejetée au même titre qu'une image fausse.
- Fiches flash : infographies denses bleu nuit/or (ou carnet) avec 6–10 lignes exactes par case. La consigne « sans texte suivi » est interdite pour planches et fiches ; seul un hero purement d'ambiance peut s'en passer.

### 8.3 Contrôle et rejet

Chaque image retenue est **relue en zoom 100 %** : orthographe de chaque mot, chaque chiffre, côté gauche/droit, flèches, aucune étiquette tronquée, aucun texte gibberish. Une planche pauvre, fausse ou à moitié vide est **rejetée**, pas livrée « en attendant ». Le journal d'images de la leçon classe chaque fichier : `GARDER / CORRIGER / REFAIRE`, avec la raison.

## 9. Peaux de module — et la peau PNEUMOLOGIE (nouvelle)

Chaque module a **sa** peau : classe body, canvas, script de champ, identité CSS dans les 4 thèmes, racine de scrollbar. Ne jamais garder la peau du squelette cloné. Les quatre modes de fond existants doivent tous fonctionner : `anime` (champ vivant), `eco` (champ figé peint une fois), `photo` (capture du champ), `planche` (planche à l'encre du module via `bg-mode.js`).

### 9.1 « Air alvéolaire » — Sémiologie pneumologique (`pn-*`)

Métaphore : l'air oxygéné (cyan glacier) qui rencontre le tissu alvéolaire (rose) ; le champ de particules reliées évoque molécules d'air et grappes d'alvéoles. Moteur = clone du champ biochimie (`bio-field.js` v11, mêmes logique éco/photo/cadence), renommé `pneumo-field.js`, canvas `#pneumoFieldCanvas`, classe `has-pneumo-field`, racine `pneumo-root`, API `window.__pneumoField`.

| Thème | Nom | Primaire `--blue` | Secondaire `--teal` | Fond `--bg` | Champ (RGB) |
|---|---|---|---|---|---|
| Sombre | Air nocturne | `#35d0ff` cyan glacier | `#ff7aa8` rose alvéole | `#05141f` | `[53,208,255]` / `[255,122,168]` |
| Clair | Air clair | `#087ea4` bleu respiratoire | `#be3455` rose profond | `#eef8fb` | `[8,126,164]` / `[190,52,85]` |
| Aurora | Brume alvéolaire | `#a78bfa` violet brume | `#f9a8d4` rose aurore | `#140b24` | `[167,139,250]` / `[249,168,212]` |
| Ocean | Oxygène dissous | `#2dd4bf` turquoise dissous | `#7dd3fc` bulles d'air | `#03202b` | `[45,212,191]` / `[125,211,252]` |

Chaque thème redéclare sur `body.has-pneumo-field` : `--blue/-dark/-bright/-soft/-rgb/-glow`, `--teal/-dark/-soft/-rgb`, `--bg/-card/-hover/-input`, `--text/-dim/-muted`, `--border/-soft`, `--accent-rgb`, `--green` (le « vrai » des QCM reste un vert lisible, distinct des deux accents), `--grad-brand/-deep`, ombres, halo `::after`, variante navbar claire et scrollbar `html.pneumo-root`. Le canvas est ajouté aux sélecteurs d'extinction `body.fond-fixe` / `body.fond-photo-pris`, et `#pneumoFieldCanvas` est fixé plein écran dans `lesson.css` comme les autres champs.

Page pn conforme :

```html
<body class="has-pneumo-field" data-lesson-id="pn-01">
    <canvas id="pneumoFieldCanvas" aria-hidden="true"></canvas>
    …
    <script src="../js/pneumo-field.js?v=1"></script>  <!-- après main.js, avant lesson.js -->
```

`bg-mode.js` mappe déjà `pn → pneumo` et `assets/img/fonds/planches/pneumo.webp` existe : le mode planche est acquis dès que la page est une `pn-*`. Toute page de module sans canvas assorti à son script de champ est bloquante (le moteur sort en silence) — y compris les anciennes pages bi-*.

## 10. Arabe et accessibilité

- Chaque bloc traduisible porte `data-tr="clé-unique"` ; `#arData` ↔ `data-tr` : égalité stricte des ensembles, zéro orphelin dans les deux sens.
- Arabe du sens, neutre non-khaliji ; termes techniques gardés en français dans `<bdi class="fr-term">` / chiffres et sigles dans `<bdi class="fr-plain">`.
- Images : `alt` français complet, `width/height` = dimensions réelles du fichier, `loading="lazy"` sauf hero (`eager`). Aucun `.png` de contenu, aucun `object-position` de recadrage sauvage.

## 11. Portes de livraison (toutes obligatoires)

1. `AUDIT-LECON-GOLD-v3.py <site> <page>` : **0 bloquant**. En `--strict-gold` : 0 avertissement qualité (corrections proposition par proposition, couverture mots-clés, AR Ciné complet, fiche dense, dimensions/alt).
2. **Test runtime** (navigateur ou jsdom) : cliquer un QCM annales + un entraînement (verdict + correction + score), monter le lecteur Ciné + un mini-lecteur par zone, ouvrir/fermer/rechercher les mots-clés, retourner et noter une flashcard, basculer AR/FR, dérouler les 4 thèmes × 4 modes de fond sur une page du module.
3. Audit officiel chaîne complète : seules les références cassées **préexistantes connues** sont tolérées, listées dans le LISEZ-MOI.
4. Contrôle visuel : planche-contact de la leçon + zoom de chaque image générée ; journal `GARDER/CORRIGER/REFAIRE` joint aux artefacts.
5. `data.js` : ligne de la leçon `recu:true` + `url`, toutes les autres `LIVREE` intactes ; registre et JOURNAL mis à jour ; delta Drive daté + LISEZ-MOI + MD5 ; artefacts builder/scripts uploadés le même jour.

Toute dérogation (ex. AR Ciné partiel faute de quota) se déclare dans le statut et le LISEZ-MOI avec l'étape restante — la leçon reste alors `EN_COURS`/`A_PATCHER`, jamais `LIVREE`.
