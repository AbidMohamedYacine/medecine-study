# Audit forensique qualité — bi-06, pn-01, pn-04

Date : 2026-10-30 · AGENT-1 · Statut des trois pages : **A_PATCHER** (gel publié au JOURNAL, locks AGENT-1).

Références mesurées dans la base officielle reconstruite : **ca-02** (référence interactive complète), **ca-09** (référence contenu/images/fiche ; sans Ciné/mots-clés/arabe), **ra-02** (squelette), **bi-05** (modèle récent le plus sain pour les contrats).

## Verdict

L'utilisateur a raison. Les trois pages suspectes contiennent beaucoup de matière, mais plusieurs fonctions visibles sont **structurellement débranchées des moteurs réels du site**. Ce ne sont pas des impressions : les sélecteurs et clés attendus par `lesson.js`, `cine.js` et `keywords.js` ne correspondent pas au HTML livré.

La cause racine est le builder **bi-06** : il a inventé une variante de balisage au lieu de copier bi-05/ca-02/ra-02. Le HANDOFF a ensuite codifié cette variante aux lignes 117, 122, 124 et 125. Les builders pn-01 et pn-04 l'ont recopiée presque telle quelle, puis ont ajouté leurs propres pertes : section Ciné centrale absente, mini-lecteurs incomplets ou décalés, peau pneumologie absente.

## 1. QCM — présents à l'écran, inertes au clic

Moteur réel (`lesson.js`) :

- `JSON.parse(block.getAttribute('data-answer'))` : la valeur doit donc être un JSON, par exemple `data-answer='["A","C"]'`.
- Choix lus uniquement dans `.qch li[data-l]`.
- Verdict écrit dans `.qverdict`.
- Révélation par `.qcheck`, affichage CSS de `.qexp` seulement quand `.qblock.answered`.
- Score seulement dans une section `[data-qcm-set]` contenant `.qs-val`.

Pages suspectes :

- `data-answer="A,C,D"` : `JSON.parse` échoue, le moteur abandonne silencieusement chaque bloc.
- Choix en `label.qopt > input[type=checkbox]` : aucun `.qch li`, donc aucun choix écouté.
- `.qexp[hidden]` : jamais d'état `answered`, correction jamais révélée.
- `.score-box#annalesScore/#entrScore` : aucun sélecteur du moteur ne les remplit.
- Classes `.qnum/.qsource/.qbadge/.qoptions/.qopt/.qletter` : absentes de `lesson.css`.

Conséquence : les cases peuvent se cocher visuellement comme des cases HTML ordinaires, mais il n'y a ni correction, ni verdict, ni score, ni enregistrement de progression.

Richesse des corrections (texte visible, médiane) :

| Page | Annales | Entraînement |
|---|---:|---:|
| ca-02 | 930 caractères | 833 |
| ca-09 | 1 051 | 673 |
| bi-06 | 364 | 297 |
| pn-01 | 655 | 208 |
| pn-04 | 666 | 217 |

Les références corrigent **proposition par proposition** (5 `.qexp-item` + mémo). Les suspectes ont un bloc « Pourquoi / Pièges » global, souvent utile mais pas au format ni à la densité des références, surtout en entraînement pn.

## 2. Ciné-révision et lecteurs de section — données présentes, moteur muet

Moteur réel (`cine.js`) : il exige `{ "chapitres": [{ "t", "imgs", "fr", "ar" }] }`. Sans tableau `chapitres`, il sort immédiatement : ni lecteur central, ni mini-lecteurs.

Pages suspectes : `{ "chapters": [{ "title", "audio", "audioAr", "images" }] }`.

- **bi-06** : la section `#cine` et `#cinePlayer` existent, et les spots de section sont globalement bien placés, mais le JSON incompatible empêche tout montage.
- **pn-01 / pn-04** : l'onglet `cine` existe dans la navigation, mais **aucune section `#cine`**, aucun `#cinePlayer`. Même avec un JSON corrigé, il n'y aurait pas de lecteur central.
- **pn-01** : spots seulement sur une partie des sections, avec dérive d'index après les sections sans spot : par exemple `frequence` pointe le chapitre « phase », `gravite` pointe « fréquence/rythme », `auscultation` et `pointscles` pointent le résumé. Plusieurs sections n'ont aucun lecteur.
- **pn-04** : seulement deux spots (`vue` chapitre 0 et `resume-total` chapitre 9). Les 14 sections de contenu n'ont aucun lecteur.

Couverture audio :

- ca-02 et ra-02 : FR + AR sur **tous** les chapitres.
- bi-05, bi-06, pn-01 : FR sur les chapitres, AR seulement sur le résumé.
- pn-04 : 10 pistes FR, **aucune piste AR**, pas même le résumé.

Les fichiers audio existent donc, mais l'expérience « vocal sous chaque planche de section » des références n'est pas livrée.

## 3. Mots-clés — panneau impossible à ouvrir

Moteur réel (`keywords.js`) : `#kwData` doit être un **tableau** `[{t,s,n,d,a}]`, dans l'ordre des sections ; `s` fait défiler vers la section et `n` affiche son numéro.

Pages suspectes : objet `{items:[{t,d,a:{t,d}}]}`. Le test `Array.isArray(WORDS)` échoue, le script sort : ni poignée « MOTS-CLÉS », ni panneau, ni recherche, ni saut de section.

Densité : ca-02 = 57 termes ; bi-05 = 36 ; bi-06 = 36 ; pn-01 = 37 ; pn-04 = 38. Au-delà du format, pn-04 contient des entrées qui ne sont pas des termes de dictionnaire (« 100 mL par jour », « Conclusion du cours »). Le standard v3 fixe donc aussi une cible de couverture, pas seulement un format.

## 4. Flashcards — mauvais conteneur, double jeu de données, IDs absents

Moteur réel : il ne démarre que si `#fcDeck` existe ; il lit `#fcData`, puis utilise `fcStage/fcCard/fcFront/fcBack/fcCount/fcAgain/fcHard/fcGood/fcEasy/fcDone` et un `id` stable par carte pour la répétition espacée.

Pages suspectes :

- Section réduite à `<div id="flashApp"></div>` : aucun deck, moteur inactif.
- **Deux** scripts portant le même ID `fcData` : le premier est le jeu ra-02 (ultrasons) hérité du bas de page du squelette ; le second est le jeu propre à la leçon, placé après les moteurs.
- Le jeu propre n'a aucun `id` de carte : même en réparant le conteneur, toutes les cartes partageraient la clé `undefined` dans la progression.
- L'ordre des sections est aussi inversé par rapport à la navigation : `fiche → resume-total → flashcards` dans le DOM, contre `fiche → flashcards → resume-total` dans les onglets et les références.

## 5. Arabe — traductions présentes mais moteur chargé trop tôt

`ar-mode.js` cherche `#arData` dès son exécution. Dans les pages de référence, tous les JSON précèdent les moteurs. Dans les suspectes, `#fcData` propre et `#arData` sont insérés **après** `lesson.js/ar-mode.js/keywords.js/cine.js`. Le mode arabe ne peut donc pas initialiser ses bascules, malgré 76 à 106 clés `data-tr` présentes.

## 6. Fiche flash — composant inventé, non stylé, appauvri

Références ca-02/ca-09 : `.flashsheet.ff-2x2` → 4 `.flash-cell fc-*`, chacune avec titre, `img.flash-img` dense et liste HTML de faits d'examen (2 499 caractères de texte sur ca-02 ; 3 777 sur ca-09).

Pages suspectes : `.flash-grid` (aucune règle CSS) → 6 `figure.flash-cell` avec image explicitement demandée/alt-textée « sans texte suivi » + légende d'une ligne. La cellule reprend une partie du style `.flash-cell`, mais l'organisation « image qui se suffit + faits à relire » a disparu. C'est exactement l'écart signalé par l'utilisateur.

## 7. Organisation des sections de contenu

Rituel des références récentes :

`tête de section → planche principale → documents réels éventuels → mini-lecteur Ciné → boîte principale → 2 mini-cartes (ou tableau) → .qcm-focus`.

Écarts mesurés :

- ca-02 : 5 `.lbox`, 30 `.mini-card`, 9 `.reel-strip`, spot dans chaque section de contenu principale.
- bi-06 : 13 `.lbox`, 11 `.mini-card`, 3 `.reel-strip` ; structure proche, mais interactifs cassés et planches inégales.
- pn-01 : 20 `.lbox`, 9 `.mini-card`, 9 `.reel-strip` ; matière réelle, mais lecteurs absents/décalés et hiérarchie plus monotone.
- pn-04 : 34 `.lbox`, 3 `.mini-card`, 3 `.reel-strip` ; premières sections sans planche principale au format attendu, aucun lecteur de section. L'impression « blocs de texte » est donc fondée, même si le texte source est présent.

## 8. Images — le problème n'est pas seulement le goût, c'est le contrat

Les planches-contact et les zooms confirment deux familles différentes :

- **ca-02/ca-09** : planches 1376×768, fond contextuel rempli, titre français en toutes lettres, 3 à 5 zones/panneaux, scène ou anatomie + mécanisme + chiffres/seuils + piège d'annales. Une planche permet de réviser sa section en 30 secondes. Les fiches flash sont des infographies texte dense bleu nuit/or ou carnet, pas des pictogrammes.
- **bi-06** : style 3D/illustration moderne inégal, dimensions variables (1536×1024, 1693×929, 1774×887…), plusieurs fonds blancs ou quasi vides. Exemple zoomé : `ff-cinetique` = trois courbes sans aucun libellé de marqueur.
- **pn-01/pn-04** : dimensions 1376×768 respectées, mais style sépia/vintage dilué, grandes zones vides, pictogrammes et libellés petits ; fiches flash sans mots. Exemples zoomés : pn-04 `ff-types` = cinq béchers sans un seul mot ; pn-01 `gravite` = une scène propre mais pauvre (5 étiquettes) face à la densité ca-02/ca-09.

La règle « qualité image v2 » du 30/10 est **postérieure** aux constructions pn du 29/10 : elle n'a jamais été appliquée rétroactivement. Dire que pn-01/pn-04 illustraient la qualité v2 était donc faux. En outre, les builders demandaient explicitement des flash « sans texte suivi », à l'opposé du contrat des références. Le standard v3 interdit cette consigne pour planches de section et fiches flash.

Quantités actuelles (à reclasser image par image : garder / corriger / refaire) :

- ca-02 : 37 images page, dont 19 documents réels du cours.
- ca-09 : 34 images page, 23 visuels de section.
- bi-06 : 24 images page, seulement 3 strips réels.
- pn-01 : 37 images page, 9 strips réels ; quantité suffisante, qualité/contrat insuffisants.
- pn-04 : 28 images page, seulement 3 strips réels.

## 9. Fond et thèmes — pneumologie sans peau

`bg-mode.js` connaît déjà `pn → pneumo` et la planche à l'encre `assets/img/fonds/planches/pneumo.webp` existe (arbre bronchique/alvéoles, 1376×768) : le mode **planche** peut donc fonctionner.

En revanche, pn-01/pn-04 ont `<body data-lesson-id>` sans classe de peau, sans canvas, sans script de champ. Il n'existe ni `pneumo-field.js`, ni `#pneumoFieldCanvas`, ni bloc CSS `has-pneumo-field`, ni racine de scrollbar associée. Les modes **animé/éco/photo** n'ont donc aucun fond vivant pneumologie à afficher ou photographier, et les quatre thèmes restent ceux de la plateforme.

Défaut adjacent découvert : les pages bi-05/bi-06 de nos artefacts chargent `bio-field.js` et la classe `has-bio-field`, mais ne contiennent pas `<canvas id="bioFieldCanvas">` ; l'identité CSS s'applique, pas le champ de particules. Le patch bi-06 ajoute le canvas ; bi-05 devra recevoir le même micro-patch d'une ligne.

## 10. Pourquoi les contrôles ont laissé passer

1. L'audit officiel vérifie la chaîne `data.js ↔ pages ↔ fichiers`. Il ne connaît ni les sélecteurs des moteurs, ni les clés JSON, ni le rendu, ni la qualité d'image.
2. Les assertions des builders comptaient des chaînes (`qblock`, `qcheck`, `cine-spot`) et des JSON « parseables », sans vérifier les clés/classes réellement lues par les moteurs.
3. Aucun test navigateur n'a cliqué un QCM, ouvert les mots-clés, retourné une flashcard ou monté un lecteur.
4. Le HANDOFF décrivait la variante bi-06 comme « gold » et désignait bi-06 comme modèle complet à imiter.
5. Les images ont été comptées et regardées en miniature, sans grille de rejet zoomée comparable à ca-02/ca-09.

## Réparation prescrite

1. **Gel** : fait (JOURNAL + locks patch/qualité AGENT-1 ; registre à passer en `A_PATCHER`).
2. **Standard-or v3 + audit bloquant** fondés sur les moteurs réels et un test runtime navigateur/jsdom.
3. **Patch fonctionnel** bi-06/pn-01/pn-04 : QCM gold + scores, Ciné central et spots à chaque section de contenu, mots-clés tableau mappé, deck flashcards unique avec IDs, ordre des JSON avant moteurs, fiche flash `.flashsheet` dense, ordre flashcards avant résumé.
4. **Peau pneumologie complète** : champ de particules « air/alvéoles » dérivé du moteur biochimie, quatre identités chromatiques nouvelles (sombre/clair/aurora/ocean), compatibilité animé/éco/photo/planche, application à toutes les pages pn futures et aux deux pn livrées.
5. **Contenu** : corrections QCM réécrites proposition par proposition FR/AR ; mots-clés enrichis vers la couverture ca-02 ; audios AR manquants par lots comptés.
6. **Images** : classement zoomé garder/corriger/refaire, puis régénération par lots de 10 maximum par message utilisateur, au contrat ca-02/ca-09. Aucune page ne redevient `LIVREE` avant ces étapes et un test navigateur complet.
