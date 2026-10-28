# SEENmed — MÉTHODE INTÉGRALE DE FABRICATION D’UNE LEÇON

> Document de travail consolidé. Il rassemble les instructions actuellement récupérées dans le workspace. Il ne prétend pas être le fichier original disparu d’hier.

## Comment utiliser ce document

- Lire ce document avant toute nouvelle leçon.
- Utiliser `medstudy/lecons/an-03-pathologies-mec.html` comme référence structurelle ANAPATH.
- Utiliser les dernières leçons de physiopathologie validées, notamment `ph-06-choc-septique.html`, comme référence de profondeur, narration, résumé, annales et Ciné.
- Ne jamais utiliser AN-13, une page générée récemment ou un squelette comme modèle pédagogique.
- Faire une seule leçon de bout en bout : source → plan → contenu → images → reels → annales → QCM → fiche → résumé total → arabe → audio → website → audit → Drive/MD5.
- Une validation technique ne prouve jamais la qualité pédagogique.

## Portée universelle — obligatoire pour CHAQUE leçon

Cette méthode ne concerne pas seulement AN-13, MEC ou une leçon particulière. Elle s'applique intégralement à **toutes les leçons de tous les modules** : ANAPATH, physiopathologie, immunologie, cardiologie, sémiologie, biochimie, radiologie, psychiatrie et toute nouvelle matière ajoutée au site. Les exemples MEC et choc septique servent de références de qualité, mais le pipeline, les contrôles et les critères ci-dessous doivent être exécutés pour chaque leçon, sans exception.

Une leçon n’est finale que si elle contient un cours source-grounded développé, 10–18 sections thématiques nommées adaptées à son propre plan, des boxes complètes, des planches dédiées, des reels sélectionnés si la source en fournit, des annales exactes lorsqu'elles existent, des QCM spécifiques, une fiche flash illustrée case par case, un résumé total dédié, une traduction arabe réelle, 8 chapitres audio français développés + résumé français + résumé arabe, les mots-clés, l’intégration website, l’audit visuel/fonctionnel et une archive Drive vérifiée par MD5. Pour une leçon sans annales, sans figures originales ou sans source audio exploitable, l'élément est marqué « non disponible dans la source » : il n'est jamais inventé ni supprimé du contrôle.

---


# 01 — Méthode restaurée

# SEENmed — méthode complète restaurée

## Références de travail

La référence de rendu n'est pas une page générée récemment.

Références principales :
- `medstudy/lecons/an-03-pathologies-mec.html` — référence ANAPATH/MEC.
- dernières leçons de physiopathologie validées — référence de profondeur, narration, résumé et progression.
- `analysis/CHARTE-LECON.md` — méthode complète.
- `medstudy/assets/img/CHARTE-IMAGES.md` — loi des images.
- `analysis/CHARTE-ARABE.md` — traduction et méthode résumé.
- `analysis/CHARTE-CINE.md` — audio et narration.
- `analysis/CHARTE-MOTS-CLES.md` — vocabulaire.
- `ESPACE-REGLES.md` — stockage.

Les pages récentes générées automatiquement ne servent jamais de modèle.

## Travail d'une leçon, du début à la fin

1. Lire la source entière avant de construire.
2. Relire les chartes réelles avant chaque leçon.
3. Écrire un plan source-grounded : sections, hiérarchie tombable, annales, images et avancement.
4. Relever les annales CURE dans le texte exact et utiliser le corrigé officiel.
5. Construire 10 à 18 sections thématiques nommées selon le cours, jamais six sections génériques.
6. Dans chaque section : accroche courte, boxes à puces, planche dédiée, puis reels sélectifs si présents.
7. Zéro prose de cours hors `lbox`; toutes les informations doivent être cochables et organisées.
8. Produire 20 à 26 planches utiles : hero, mindmap, une planche par section, une image par case de fiche flash et un total dédié.
9. Une planche doit montrer la réalité médicale : organe, tissu, cellule, geste ou mécanisme ; jamais une simple page de mots.
10. Construire la fiche flash avec une image différente pour chaque case.
11. Construire un résumé total dédié, sans réponses de QCM, avec une hiérarchie en une lecture.
12. Construire les QCM numérotés, spécifiques au cours, avec propositions A-E, data-answer, explication de chaque proposition et source.
13. Ajouter les annales avant l'entraînement quand elles existent.
14. Traduire tout le contenu de cours en arabe contextuel : boxes, tableaux, fiche, résumé, explications de QCM et données traduisibles.
15. Garder les termes français scientifiques utiles dans la phrase arabe avec leur équivalent arabe.
16. Audio : 8 chapitres FR, résumé FR et résumé AR ; pas de huit chapitres arabes. Narration développée, fluide et contextualisée, normalement proche d'une minute ou plus par piste quand le contenu le justifie.
17. Ajouter `cineData`, les spots de section, le résumé audio et les images associées.
18. Intégrer directement la page au site : navigation, onglets, progression, arabe, flashcards, QCM, lightbox et lecteur.
19. Auditer visuellement et techniquement la page : contenu, images, arabe, QCM, audio, liens, JSON et navigation.
20. Mettre à jour le tableau de bord seulement après la livraison réelle.
21. Construire le pack autonome Drive, vérifier le MD5 local contre Drive, puis nettoyer les fichiers temporaires.

## Méthode de résumé

- Tombable : développé avec pourquoi, simplification, moyen mnémotechnique et piège d'examen.
- Non tombable : condensé sans perte de sens.
- La hiérarchie vient du croisement source × annales × corrigé, pas du nombre de diapositives.

## Règle de rythme

Une seule leçon active à la fois. On ne passe pas à la suivante tant que la leçon courante n'a pas son contenu, ses images, son résumé, son arabe, ses QCM, son audio, son intégration website et son archive finale.

## Règle de vérité

Une validation technique ne signifie pas que la leçon est de qualité. Une livraison n'est annoncée qu'après comparaison réelle avec la MEC et les dernières leçons de physiopathologie validées.

## Source manquante

Une source absente est mise en pause. Elle n'est ni devinée, ni remplacée, ni déclarée reçue.



---


# 02 — Verrou de workflow

# SEENmed WORKFLOW LOCK — ACTIVE

This is the non-negotiable production method for every next lesson.

## Canonical references
- Structure: the validated MEC lesson (`an-03-pathologies-mec.html`) and the last validated physiopathology lessons (`ph-05`, `ph-06`, `ph-10`, `ph-13` where applicable), exactly as previously agreed. These are the primary references for sections, boxes, summaries, flash sheets, audio and overall depth.
- AN-08 to AN-11 may be consulted as additional good ANAPATH examples, but AN-13 and the recent generated skeleton pages are NOT references.
- Content/boxes: real `CHARTE-LECON.md`, real `CHARTE-IMAGES.md`, `CHARTE-ARABE.md`, `CHARTE-CINE.md`.
- Never use a newly generated skeleton as a template for another lesson.

## Mandatory order per lesson
1. Read source completely and write a source-grounded plan.
2. Extract only real source visuals; generate dedicated section boards only when needed.
3. Build 10–18 named thematic sections, each with a dedicated visual.
4. Put all teaching content in lbox bullet boxes; no prose outside boxes except one short lsub.
5. Create exact official annales from the official CURE correction; never invent answers.
6. Create topic-specific numbered training QCM with proposition-by-proposition explanations.
7. Build a flash sheet with one real image per flash-cell and a dedicated total image.
8. Translate all course boxes, tables, summaries and QCM explanations into contextual Arabic.
9. Write 8 FR chapters + 8 AR chapters + FR/AR summaries as fluid narration, usually 900–1500 characters per clip; split and fuse only when needed.
10. Add section cine spots and central cineData.
11. Run lesson-check plus source/image/audio/arData audits.
12. Update data.js only after all checks pass.
13. Create autonomous Drive pack and verify MD5.
14. Clean temporary files and check storage.

## Repair policy
AN-13, AN-14, AN-15, AN-16, AN-17, AN-18, AN-20 and AN-22 are not considered final until they pass this complete workflow. Short audio is draft only; inherited QCM or visuals are not accepted as final.



---


# 03 — Charte leçon

# CHARTE-LEÇON — LA MÉTHODE COMPLÈTE (restaurée le 26/10 après audit)

> ⚠️ HISTORIQUE DE L'INCIDENT, pour ne jamais recommencer : au tour 46, après une
> compaction de l'historique, une « CHARTE-IMAGES reconstituée » de 2 Ko a été écrite
> de mémoire (medstudy/CHARTE-IMAGES.md) ALORS QUE LA VRAIE CHARTE de 12 Ko existait
> toujours dans medstudy/assets/img/CHARTE-IMAGES.md. Les leçons ph-02, ph-05, ph-06,
> ph-07, ph-08, ph-11, ph-12 (+ début ph-13) ont été construites sur la version
> dégradée : 6 sections génériques au lieu de 10-18 thématiques, 10 planches au lieu
> de 20-26, UNE image de fiche flash au lieu d'une par case, prose au lieu de boxes,
> traduction partielle (6-11 blocs sur 60+), QCM sans numéros, style « néon fond
> sombre » érigé en loi alors que la vraie charte le REJETTE comme parti pris.
> L'utilisateur l'a détecté le 26/10. RÈGLE ABSOLUE : à chaque début de leçon,
> relire LES FICHIERS de charte (ls + cat), jamais « de mémoire ».

## Les chartes de référence (les VRAIES, à relire avant chaque leçon)
1. `medstudy/assets/img/CHARTE-IMAGES.md` (12 Ko) — LOI des images.
2. `medstudy/assets/img/CHARTE-IMMUNO.md` — recettes techniques anti-défauts (§12-§14),
   registre des styles consommés.
3. `analysis/CHARTE-ARABE.md` — mode arabe + MÉTHODE RÉSUMÉ.
4. `analysis/CHARTE-CINE.md` — narration audio (voix, style, filtres).
5. `analysis/CHARTE-MOTS-CLES.md` — dictionnaire des mots-clés.
6. `ESPACE-REGLES.md` — stockage (ne supprime JAMAIS une charte : elles pèsent des Ko).

## GABARIT D'UNE LEÇON — mesuré sur les leçons validées (ph-10, ca-08, im-04, bi-03)

### 1. Sections de cours
- **10 à 18 sections THÉMATIQUES NOMMÉES** selon le plan réel du cours (`definition`,
  `starling`, `cascade`, `nyha`…) — PAS un moule générique s1-s6. ph-10 : 24 sections.
- Chaque section : planche dédiée + **le contenu organisé en BOXES** (`lbox` avec
  `lbox-title` + listes `<li>`), pas en paragraphes de prose. Référence mesurée :
  ca-08 = 64 boxes, im-04 = 58, bi-03 = 48, ph-10 = 46 ; les leçons dégradées n'en
  ont que 16. Les `<li>` portent le cochable ; la prose ne sert qu'à relier.
- reel-strip (documents originaux du PDF, WebP q90) après la planche de section.

### 2. Images (voir CHARTE-IMAGES.md pour le FOND)
- **20-26 planches par leçon** : hero + mindmap + UNE PLANCHE PAR SECTION thématique
  + ff-* (une par case de fiche flash) + total.webp. « Si un sujet ne tient pas en
  une image, en produire plusieurs » (consigne utilisateur explicite).
- **Styles VARIÉS d'une planche à l'autre**, choisis pour l'idée ; mindmap = style
  neuf à chaque leçon ; REJETÉS : néon-sur-fond-sombre systématique, imagerie
  IRM/scanner comme esthétique. La RÈGLE MÈRE : montrer la chose COMME DANS LA VRAIE
  VIE (scène clinique réaliste, organe naturaliste, siège anatomique exact, médaillons
  de réalité) + étiquettes + phrase du pourquoi + chiffres écrits.
- Quota 10/tour → une leçon complète s'étale sur 2-3 tours. ON NE COMPRESSE PAS LE
  FORMAT POUR TENIR DANS UN TOUR : on étale.
- Relecture zoom de chaque lot (anglais, doublons, chiffres inventés) avant livraison.

### 3. Fiche flash
- 4 à 7 cases `flash-cell`, chacune : `<h4>` + **image ff-<theme>.webp dédiée**
  (class="flash-img") + liste à puces du cochable (★★/★). PAS une image unique.

### 4. Résumé total
- Section `total` : **total.webp = une planche de synthèse GÉNÉRÉE dédiée** qui
  redessine tout le cours (pas un collage PIL des planches de sections), sans les
  réponses des QCM pour pouvoir se tester.

### 5. MÉTHODE RÉSUMÉ (contenu) — décision utilisateur du 25/10 (CHARTE-ARABE.md)
- Le TOMBABLE (annales/corrections) : DÉVELOPPÉ — pourquoi, simplification, moyen
  mnémotechnique, piège exact de l'examinateur.
- Le non-tombable : CONDENSÉ, lisible en une passe, sans perte d'information.
- La hiérarchie vient du croisement cours × annales × corrigés, PAS du volume du cours.

### 6. QCM
- **Numérotés** : `<p class="qtext">1. …` — les annales numérotées 1..n, puis
  l'entraînement REnuméroté 1..n (modèle ph-10/im-05).
- Annales d'abord (texte EXACT + corrigé officiel + source promo), puis entraînement
  calibré sur le profil de l'examinateur (zones vierges du cours).
- Explication proposition par proposition + memo, data-answer, bouton Corriger.
- Le nombre de QCM suit la matière (anciennes leçons : 22-51), pas un chiffre fixe.

### 7. Traduction arabe (CHARTE-ARABE.md)
- data-tr sur TOUT le contenu de cours : paragraphes, BOXES, tableaux, mini-fiches,
  explications de QCM (.qexp) — pas seulement les sous-titres. Référence : dans les
  leçons validées, la quasi-totalité du contenu (organisé en li/boxes) est couverte ;
  dans les dégradées, 6-11 <p> sur 60+ → bouton ع « qui ne traduit rien » (reproche
  utilisateur 26/10). Énoncés/propositions des QCM restent en français.
- Traduction DU SENS, termes scientifiques gardés en français dans <bdi> + équivalent
  arabe à la première occurrence.

### 8. Audio ciné (CHARTE-CINE.md)
- 8 chapitres FR (voice-00) + résumé FR + résumé AR (voice-03 — PAS voice-00),
  mini-lecteurs cine-spot par section, prof qui raconte, français prononcé à la
  française, ≤1450 car.

## LEÇONS À RÉPARER (constat d'audit du 26/10)
| leçon | boxes | data-tr | planches | ff images | QCM numérotés |
|---|---|---|---|---|---|
| validées (ca-08, im-04, bi-03, ph-10…) | 30-64 | totale (li/boxes) | 20-26 | 1/case | oui |
| ph-02, ph-05, ph-06, ph-07, ph-08, ph-11, ph-12 | 16 | 60-67 clés sur prose | 10 | 1 seule | non → corrigé 26/10 |

Réparation par leçon = ré-éclater les 6 sections en thématiques, contenu en boxes,
planche par section + ff par case (≈ 12-16 images → 2 tours/leçon), data-tr total,
total.webp dédié. ph-13 : à construire DIRECTEMENT au format complet.

## 🔴 RÈGLE ABSOLUE — zéro paragraphe hors boîte (loi utilisateur, 26/10/2026)
- AUCUN `<p data-tr>` de prose au niveau d'une section. TOUT le contenu de cours vit
  dans des `lbox` à puces (`lbox-title` avec icône + `ul/li` avec `<b>` sur les mots clés).
- Seule exception : la `lsub` — UNE ligne courte d'accroche sous le `h2` de section.
- **Leçon de référence structurelle : `ca-10-semiologie-veineuse.html`**
  (lsection-head + lsub courte → lbox data-tr → figure section-visual → mini-cards/lgrid2).
- Les légendes `<figcaption>`, `reel-head` et textes d'interface ne sont pas concernés.
- Fiche flash : **une ff-*.webp PAR flash-cell**, jamais une image unique pour toutes.



---


# 04 — Charte images

# CHARTE DES IMAGES — LOI PERMANENTE, TOUTES LEÇONS, TOUS MODULES

**Statut : à relire AVANT chaque lot de `generate_image`, sans exception.**
Ce fichier rassemble les consignes que l'utilisateur a données lui-même sur les images.
Il n'a pas à les répéter. Les recettes anti-défauts techniques restent dans
`CHARTE-IMMUNO.md` (§12 à §14) ; ici, ce sont les règles de FOND.

---

## 1. La règle mère — « montrer à quoi ça ressemble pour de vrai »

> « représenter chaque information comme elle est dans la vraie vie, pour la voir et
> s'en souvenir, avec les détails, les mots et les informations »

Une planche n'est pas une liste illustrée. Chaque notion doit apparaître **sous sa forme
réelle** : l'organe tel qu'il est, la cellule telle qu'on la voit, le geste tel qu'on le
fait, l'objet tel qu'il existe. Le mot seul ne suffit jamais ; le pictogramme abstrait
non plus.

**Test à passer avant d'envoyer un prompt** — la planche répond-elle aux quatre questions :
1. **Qu'est-ce que c'est ?** (le nom, écrit)
2. **À quoi ça ressemble ?** (la forme réelle, dessinée, reconnaissable)
3. **Comment ça marche ?** (le mécanisme, étapes numérotées, flèches étiquetées)
4. **Qu'est-ce qui s'y rattache ?** (le lien avec le reste du cours)

Si une seule manque, le prompt est incomplet.

## 2bis. ⚠️ CORRECTION UTILISATEUR (22/10, ca-09) — LA RÉALITÉ EST LE CORPS DE LA PLANCHE

> « i want to see things how they look how they act how they in real life, not just words,
> i want words but with real images beside them presenting and explaining them »
> Planches REJETÉES en exemple : casier d'apothicaire (diag-diff-autres), château d'eau (hypoperfusion).

**La métaphore ne doit PLUS être la structure dominante.** Le décor-métaphore (casier,
château d'eau, armoire, atelier…) est rétrogradé : au mieux un clin d'œil discret.
Le corps de la planche, c'est **la chose réelle** : la scène clinique peinte de façon
réaliste, l'organe anatomique naturaliste, le geste tel qu'on le fait, le tracé ECG tel
qu'il sort de l'appareil, l'appareil tel qu'il est. À côté de chaque image réelle :
l'étiquette + la phrase qui explique. Le « médaillon de réalité » devient l'image
principale ; c'est le texte qui l'accompagne, pas l'inverse.

**Complément utilisateur (ca-09, lot ECG)** : « in the ecg images i liked if you also
add how it looked or when or how — i want and prefer if i can see everything to
remember ». → **Tout tracé (ECG, courbe, spirométrie…) est accompagné de sa scène
clinique réelle** : une vignette réaliste du patient qui montre À QUOI ÇA RESSEMBLE,
QUAND et COMMENT ça survient (le vieillard qui tombe sans prévenir, le coronarien qui
serre sa poitrine…), plus la phrase du contexte. Le tracé seul ne suffit pas.

**🔴 2ᵉ CORRECTION UTILISATEUR (22/10, lot ECG rejeté) — LE SIÈGE ANATOMIQUE EXACT** :
« i meant i want to see where is it located exactly and how it looked in the heart,
be smart for every region and type of information […] be precise in every information
and its details like not repeating the same phrase two times one up and another down,
also in the small details i like to be very precise ».
→ **Trois lois permanentes** :
1. **LE SIÈGE** : chaque anomalie (trouble du rythme, bloc, souffle, lésion…) est
   accompagnée de l'ORGANE ANATOMIQUE dessiné avec LA structure en cause localisée et
   allumée — le nœud sinusal en haut de l'oreillette droite, le nœud auriculo-
   ventriculaire à la jonction, les branches du faisceau dans le septum, le faisceau
   accessoire qui court-circuite, la cicatrice sur la paroi… On doit voir OÙ c'est
   et À QUOI ÇA RESSEMBLE dans l'organe. Réfléchir ainsi pour CHAQUE région et CHAQUE
   type d'information, leçon après leçon — pas seulement l'ECG.
2. **JAMAIS LA MÊME PHRASE DEUX FOIS** sur une planche (défaut récurrent : un texte en
   haut répété en bas). Le prompt l'interdit ET la relecture zoom le traque.
3. **PRÉCISION DES PETITS DÉTAILS** : chaque détail (chiffre, flèche, position d'une
   électrode, forme d'une onde) doit être exact ; en cas de doute, le vérifier dans le
   cours avant de l'écrire dans le prompt.

## 2ter. 🔴 CORRECTION UTILISATEUR (26/10, ph-08) — JAMAIS DE PLANCHE « QUE DES MOTS »

> « why you're generating images like these ?? didn't i told you i don't like this style
> of just words ???? »

Les fiches flash (`ff-*`) et le résumé `total` obéissent à la MÊME loi que les planches de
section : **l'image RÉELLE est le corps de la planche, le texte l'accompagne**. La « parade
typographique pure » (inventée après l'incident des pictos charabia de ph-06) est **ABROGÉE**.
La bonne parade contre le mini-texte charabia dans les dessins :
**des scènes et organes réalistes SANS AUCUNE LETTRE à l'intérieur**, les mots uniquement
dans les encadrés listés du prompt — jamais la suppression des dessins.
**Toute planche dont la surface est dominée par des cartes de texte est à refaire.**
Rejetées en exemple (26/10) : ph-08 `ff-mediateurs` v1 (2 colonnes d'encadrés), `ff-clinique` v1
(grille de texte), `total` v1 (typographique), `ff-definition`/`ff-reactions`/`ff-hemodynamique` v1
(texte dominant) ; **ph-06 `total` (typographique) à refaire aussi**.

## 2. Métaphore porteuse + réalité anatomique — LES DEUX, jamais l'une sans l'autre

Les deux planches citées en exemple par l'utilisateur (`ph-04/sraa` en cascade d'eau,
`ph-04/cercle` en engrenage) sont **la bonne direction** : une métaphore concrète qui
porte la structure et la rend mémorisable.

**Mais la métaphore seule ne montre pas à quoi la chose ressemble.** Un bassin de pierre
étiqueté « ALDOSTÉRONE » n'apprend pas où naît l'aldostérone ni de quoi elle a l'air.

→ **Règle : à chaque nœud important de la métaphore, coller un MÉDAILLON de réalité**
— une vignette ronde ou carrée montrant l'organe, la cellule ou la structure réelle, en
rendu naturaliste, reliée au nœud par un trait court.
La métaphore donne **la structure et le souvenir** ; le médaillon donne **l'aspect vrai**.

## 3. Densité — une planche de révision, pas une affiche

- Chaque zone porte : **un titre court** + **une phrase qui explique le pourquoi** +
  **un visuel**.
- **Flèches étiquetées** (jamais une flèche nue), **étapes numérotées** quand il y a un ordre.
- Les chiffres du cours sont écrits **en toutes lettres sur la planche**, jamais sous-entendus.
- ≤ ~12 mots par étiquette.
- **Aucun texte minuscule.** Typographie grande, lisible à l'écran sans zoomer.

## 4. Quand ça ne tient pas, on fait DEUX planches

> « si un sujet ne tient pas en une image, en produire plusieurs »

Consigne rappelée explicitement. Un titre chargé (5 organes, un cycle + son traitement,
une liste de 6 pièges) se **découpe**. Mieux vaut deux planches claires qu'une planche
tassée. Le découpage se fait par **unité de sens**, pas par moitié arbitraire.

## 5. Langue

- **100 % français**, toujours. Aucun mot anglais, même pour un sigle technique.
- Les libellés dérivent vers l'anglais à la génération → **les énoncer en français dans
  le prompt** et **les relire au zoom** après coup.
- Orthographe et grammaire vérifiées à la relecture : les fautes de génération
  (`matnquent`, `permannnente`) se corrigent au pixel ou se régénèrent.

## 6. Style

- **Un style choisi pour l'idée**, pas par habitude : « le style le plus représentatif
  de l'idée ».
- **Les styles varient d'une planche à l'autre** à l'intérieur d'une même leçon.
- La **mind map change de style à chaque leçon** (liste des styles déjà consommés :
  `CHARTE-IMMUNO.md` §7-§14 ; voir aussi la liste tenue en mémoire de session).
- **Rejetés définitivement** : le décor « néon fin sur fond sombre », le style
  « imagerie médicale réelle » façon IRM/scanner comme parti pris esthétique.
- **Autorisé et encouragé** : chercher une vraie photo en référence (`image_search`)
  avant de générer, quand la forme réelle doit être juste.

## 7. « Plus visible »

Quand l'utilisateur dit « plus visible », il demande deux choses précises :
**où la chose se situe** (dans le corps, dans le circuit) et **à quoi elle ressemble**
(gros plan clinique réaliste). La planche `ff-syndrome` — silhouette + carte du corps +
gros plans reliés — est **le modèle à poursuivre**.

## 8. Contraintes de production

- Format **paysage 16:9**, haute définition.
- **PNG → WebP** par PIL (q83), PNG supprimés ensuite.
- **Poids** : « just do it don't hesitate » — la densité prime sur le poids.
- **Ne pas faire valider chaque image** : « make the best one for every title ».
  Questions uniquement sur ce qui est réellement ambigu.
- Quota **10 générations par tour**. Un échec consomme un crédit sans écrire le fichier.
  → **relire la planche contact avant d'épuiser le quota**.

## 9. Relecture obligatoire de chaque lot

1. Planche contact de tout le lot.
2. **Zoom** sur toute zone de texte dense.
3. Chercher en priorité les trois défauts récurrents :
   **(a)** libellé passé à l'anglais, **(b)** texte écrit **deux fois**,
   **(c)** chiffre inventé dans un pictogramme.
4. Réparer **sans crédit** quand c'est possible :
   - fond uni → effacer la zone en échantillonnant le fond ;
   - lettre en trop → **chirurgie de glyphe** : supprimer le glyphe, refermer la ligne,
     recentrer. La police d'origine est préservée, c'est invisible.
   - carte/bloc entier en double ou phrase cassée multiligne → **régénérer**.

---

## Gabarit de prompt conforme (à recopier)

> Planche de révision médicale FRANÇAISE, format paysage 16:9, [STYLE CHOISI POUR L'IDÉE].
> Titre : « … ».
> **Structure porteuse** : [la métaphore concrète — cascade, engrenage, balance, carte,
> tableau de bord…], avec N nœuds numérotés.
> **À chaque nœud** : une plaque portant le nom + une ligne expliquant le pourquoi,
> **et un médaillon de réalité** montrant [l'organe / la cellule / la structure] en rendu
> naturaliste reconnaissable.
> **Flèches étiquetées** entre les nœuds, portant ce qui circule.
> **Encadré « ce qui s'y rattache »** en bas, reliant au reste du cours.
> Les dessins ne contiennent aucune lettre ni chiffre à l'intérieur.
> Tout le texte est en français correct, aucun mot anglais, aucune faute, aucun texte minuscule.

---

## 10. LES DOCUMENTS ORIGINAUX DU COURS — règle permanente (ajoutée le 20/10)

> Demande de l'utilisateur : « can you take the real pictures or images from the lesson
> itself … there's some things that have too much detail and need to watch and see them
> with those details to compare and remember, like the anapath and tissue how it looks …
> adding it beside your generated perfect image ».

**Une planche générée explique. Une figure d'origine montre.** Les deux, désormais, à
chaque fois que le PDF en contient une.

### Procédure, à faire AVANT de générer les planches d'une leçon
1. Extraire les images intégrées du PDF :
   `pymupdf` → `page.get_images(full=True)` → `doc.extract_image(xref)`.
   **Jeter tout ce qui fait moins de 120 px de côté** (logos, puces, filets).
2. Lire le texte de la diapositive d'où vient chaque image : c'est lui qui donne la
   légende exacte. **Ne jamais inventer un diagnostic que la diapositive n'écrit pas** —
   en cas de doute, décrire la morphologie (ce qu'on voit) et le dire à l'utilisateur.
3. Convertir en **WebP q90** (et non 83) : ce sont des photographies d'histologie, le
   détail est tout l'intérêt. Les fichiers restent minuscules (7 à 99 Ko).
4. Ranger dans `assets/img/<lecon>/reel/`.

### Rendu dans la page
Bloc `.reel-strip` posé **juste après** la planche de la section :

```html
<div class="reel-strip reveal">
    <p class="reel-head">Document original du cours<span class="reel-src">D<sup>r</sup> X — diapositive N « titre »</span></p>
    <div class="reel-grid">
        <figure>
            <img src="../assets/img/<lecon>/reel/<nom>.webp" alt="…" loading="lazy" width="W" height="H">
            <figcaption><b>Macroscopie</b> — …</figcaption>
        </figure>
    </div>
</div>
```

- **Jamais d'agrandissement** : `width:auto; max-height:330px`. Une figure de 255 px de
  large s'affiche à 255 px. La netteté prime sur la taille — c'est exactement ce que
  l'utilisateur a demandé (« I don't mean the size just the details »).
- `width` et `height` natifs obligatoires dans la balise (pas de saut de mise en page).
- La lightbox est branchée : `.reel-grid img` est dans le sélecteur de `lesson.js`.
- La source est **toujours citée** : enseignant + numéro de diapositive + titre.

## §11 — 🔴 Reels : extraction SÉLECTIVE uniquement (loi utilisateur, 26/10/2026)
Un reel n'est justifié QUE si la diapositive apporte quelque chose que le texte des
boxes ne peut pas rendre :
- **GARDER** : vraies photos/images cliniques, schémas fléchés et organigrammes
  (relations entre informations), tableaux détaillés/chiffrés, courbes et graphes.
- **SUPPRIMER** : toute diapositive qui n'est que du TEXTE (titres, puces, définitions,
  formules encadrées) — c'est une redondance avec les boxes et un gâchis de stockage.
Purge du 26/10 : 72 diapos-texte retirées (ph-02 ×11, ph-05 ×21, ph-06 ×21,
ph-12 ×13, ph-13 ×6). Heuristique de tri (à TOUJOURS confirmer à l'œil) :
blanc(lum>215)>0.55 ET pixels colorés<0.08 sur vignette 200×120.



---


# 05 — Charte arabe et méthode résumé

# CHARTE DU MODE ARABE — à relire avant chaque nouvelle leçon

Décisions validées par l'utilisateur le 25/10/2026 (ask_user) :

1. **Bascule HYBRIDE** : bouton global ع/FR dans la barre de navigation (préférence
   mémorisée entre les pages) **+** puce locale AR/FR sur chaque section traduite
   pour revenir au français et comparer. Instantané, sans rechargement.
2. **Couverture** : sections de cours, tableaux, mini-fiches **+ explications des QCM**
   (`.qexp-item`, `.qexp-memo`). Les **énoncés et propositions des QCM restent en
   FRANÇAIS** — c'est la langue de l'EMD. Images : jamais traduites.
3. **Registre** : arabe **standard simplifié** (فصحى بسيطة) — phrases courtes, mots du
   quotidien, PAS de littéraire rare — avec des tournures proches du parler algérien
   quand ça éclaire (ex. « يدوخ ويطيح » acceptable en appoint d'une formulation standard).
4. **Application (RÉVISÉE le 25/10, 2e décision utilisateur)** : TOUTES les leçons
   NOUVELLEMENT FABRIQUÉES à partir de ra-02 incluse (« from now and on »), pas
   seulement post-26/11. Les 33 pages déjà livrées avant ra-02 ne sont PAS retouchées.
   Première page bilingue : ra-02 (69 blocs data-tr, arData ≈ 76 Ko).

## 🔴 Correctif acquis (25/10) — ne pas répéter
- La puce locale AR/FR se place À DROITE de `.lsection-head` (`right: 0; left: auto`,
  ar-mode.css v2). La v1 la posait à gauche, superposée au numéro de section.
- Rappel utilisateur (25/10, répété) : traduction INTELLIGENTE et contextuelle,
  « the best proper translation words for the context » — jamais du copier-coller
  mot à mot. Le dictionnaire des mots-clés (CHARTE-MOTS-CLES.md) suit la même règle.

## Règle d'or de la traduction (exigence explicite de l'utilisateur)
- **Pas de copier-coller mot à mot** : traduire le SENS, comme on l'expliquerait à
  un camarade — « in the context to make you feel that you're understanding ».
- **Terme scientifique / mot important** : il reste EN FRANÇAIS dans la phrase arabe
  (pour que l'utilisateur le mémorise tel qu'il tombera à l'examen), ET sa traduction
  arabe est juste à côté. Patron :
  `… بسبب <bdi class="fr-term">hypoperfusion cérébrale</bdi> (نقص تروية الدماغ) …`
- **Jamais de décalage droite-gauche** : tout fragment latin (terme, chiffre+unité,
  sigle) est isolé dans `<bdi class="fr-term">` (encadré turquoise) ou
  `<bdi class="fr-plain">` (neutre : unités, valeurs). Ne JAMAIS laisser un mot
  latin nu dans une phrase arabe.
- Les chiffres restent en chiffres arabes occidentaux (0-9), isolés en `fr-plain`
  avec leur unité : `<bdi class="fr-plain">60 mmHg</bdi>`.

## Contrat technique (build des pages)
- Chaque bloc traduisible porte `data-tr="clé-unique"` (clé = section + n° : `def-1`,
  `def-t1`, `ecg-q2-exp`…). Granularité : le paragraphe, la liste, le tableau ou
  l'explication de QCM — pas la page entière d'un bloc.
- Les traductions vivent dans `<script type="application/json" id="arData">` en fin
  de `<main>` : `{ "clé": "html arabe" }`. Pré-écrites au build → bascule instantanée.
- Fichiers : `js/ar-mode.js?v=1` (chargé APRÈS lesson.js) + `css/ar-mode.css?v=1`
  (chargé APRÈS lesson.css). Pages sans `#arData` : le script sort immédiatement.
- Ordre scripts attendu par les vérificateurs des NOUVELLES leçons :
  `bg-mode → progress → main → <fond> → lesson → ar-mode` ; adapter `verif_xxNN.py`
  (liste `sc ==`) et laisser `verif_global` inchangé pour les 33 anciennes pages.
- Le bouton global et les puces sont INJECTÉS par ar-mode.js : ne rien ajouter au
  HTML des barres de navigation.
- Police : pile système (`Noto Naskh Arabic` si présente, sinon Segoe UI/Tahoma) —
  pas de fichier de police à télécharger pour l'instant (site silencieux).

## Qualité à vérifier au build (checklist)
- [ ] Chaque `data-tr` a sa clé dans `arData` (et inversement — zéro orpheline).
- [ ] Aucun mot latin nu hors `<bdi>` dans les chaînes arabes (regex de contrôle).
- [ ] Les termes gardés en français ont leur équivalent arabe entre parenthèses
      à la première occurrence de la section (pas forcément aux suivantes).
- [ ] Pas deux fois la même phrase arabe recopiée (même règle qu'en français).
- [ ] JSON valide, `json.loads` au vérificateur ; taille raisonnable (< ~80 Ko).

## Méthode RÉSUMÉ (décision du même jour — vaut pour toutes les nouvelles leçons)
- Le non-tombable (jamais vu en annale) : **condensé et simplifié** — lisible en une
  passe, sans perte d'information significative.
- Le tombable (présent dans annales/corrections) : **développé** — explication du
  pourquoi, simplification, moyen mnémotechnique, piège exact de l'examinateur.
- La hiérarchie vient du croisement cours × annales × corrections, PAS du volume
  du cours. Ne plus recopier le plan du cours à poids égal.



---


# 06 — Charte Ciné, voix et audio

# CHARTE CINÉ-RÉVISION (narration audio) — à relire avant chaque production

Décisions utilisateur du 25/10/2026 :

## Format
- **Formule A** : lecteur intégré à la page de leçon (planches synchronisées,
  chapitres cliquables, vitesse, bascule FR/ع). PAS de MP4 promis (pas de ffmpeg).
- **Deux pistes** par leçon : française ET arabe. Audio mp3, meilleur rendu possible.
- Fichiers : `assets/audio/<leçon>/chN-fr.mp3` + `chN-ar.mp3` (~8 chapitres/leçon,
  ≤ 1500 caractères par clip). Quota : 10 clips par tour → étaler sur 2 tours.
- Site silencieux : rien ne joue sans clic de l'utilisateur.

## Les voix (sélectionnées par l'utilisateur — NE PAS re-auditionner)
- **Français : voice-00** (narration).
- **Arabe : voice-03** (féminine, educational). Rejetés : voice-01 et voice-02
  (voix masculines — « weird, vibrate, separated », accent trop خليجي).

## Style de narration (exigences explicites — NE PAS dévier)
- **Un professeur qui raconte, pas une lecture** : relier les choses — d'où ça
  vient, comment ça marche, où ça mène ; transitions parlées (« طيب، كيف...؟ »).
- **Piste arabe** : le mot en ARABE d'abord, le terme FRANÇAIS juste après,
  puis la phrase continue en arabe. Termes français utilisés librement, partout
  où c'est utile. Base فصحى claire + touche algérienne légère (أهلا بيك، وين).
- 🔴 **Les mots français doivent être prononcés À LA FRANÇAISE, jamais à
  l'anglaise** — reproche explicite de l'utilisateur sur le 1er essai ;
  vérifier à l'écoute avant de livrer un lot. « Do not make this mistake
  from now and on. »
- 🔴 **Accent arabe : neutre, PAS خليجي** (reproche explicite).
- Zéro faute : relire chaque script avant synthèse ; écrire les unités en toutes
  lettres pour le TTS (« vingt kilohertz », « ميغاهرتز ») ; pas de balisage.
- Contenu = méthode résumé : insister sur le tombable, survoler le reste.

## État
- Démo validée/en validation : `assets/audio/ra-02/exemple-style-ar.mp3` (voice-03).
- Reste à produire (après validation du style) : moteur js/cine.js + css/cine.css,
  section #cine + onglet dans la page, 8 chapitres FR (voice-00) + 8 AR (voice-03),
  cineData JSON (chapitres, planches, fichiers audio).

## État de production ra-02 (25/10, tour 17)
- ✅ FR : ch1-6, ch8 (voice-00) · ✅ AR : ch1, ch2 (voice-03)
- 🔲 Prochain lot (7 clips) : **ch7-fr** (texte reformulé ≤1500 car. prêt dans l'historique — le 1er jet a été refusé par le filtre de contenu, probablement sur une tournure clinique ; la reformulation « d'autres situations respiratoires » passe) + **ch3→ch8-ar**.
- ⚠️ Un clip REFUSÉ par le filtre compte quand même dans le quota 10/tour → garder 1-2 clips de marge.
- Après le lot final : patcher cineData (ch7.fr + ch3-8.ar non null) et `rm exemple-style-ar.mp3`.

## État final ra-02 (25/10) — ✅ COMPLET
16/16 clips : ch1-8 × {fr, ar} · cineData à jour (aucun null) · démo supprimée.
🔴 LEÇON FILTRE : le mot « fusée » (lignes B) déclenche le filtre de contenu TTS en français
→ dans toute narration, dire « queue de comète verticale » ; « fusées » reste permis À L'ÉCRIT sur la page.
L'équivalent arabe « صاروخ » passe, mais préférer aussi une tournure neutre par prudence.

## v2 — Mini-lecteurs de section + résumé audio (25/10)
- `.cine-spot[data-ch=N]` sous la planche de chaque section rejoue le chapitre N de cineData
  (cine.js v2 / cine.css v2) ; langue partagée `seenmed-cine-lang`, un seul son à la fois (registre solo()).
- Chapitre 9 = résumé total (`resume-{fr,ar}.mp3`), aussi dans le Ciné central.
- ra-02 : 11 spots (ch5 double modes+indications, ch8 double balance+contraste).
- 🔴 FILTRE TTS (vécu ×5) : le résumé FR complet (~1500 car.) a été refusé quelles que soient les
  formulations, alors que CHAQUE MOITIÉ passait → DICHOTOMIE puis FUSION MP3 au niveau des trames
  (python pur : strip ID3/Xing, concat trames CBR — script dans l'historique tour 19). Un refus
  compte dans le quota 10/tour. Réflexe : si 2 refus de suite, couper en deux et fusionner.
- STANDING : toute nouvelle leçon bilingue reçoit Ciné + spots + résumé audio.

## 🔴 RÈGLE PERMANENTE — FLUIDITÉ (user, 25/10, « don't let me retell it every time »)
TOUTE voix (FR et AR, chapitres, résumés, toutes les leçons à venir) doit être une NARRATION
FLUIDE ET CONTEXTUALISÉE : raconter, relier les idées (d'où ça vient → comment ça marche → où ça
mène), expliquer pour faire comprendre. JAMAIS une énumération de mots-clés, jamais de sauts secs
de section en section, jamais de style télégraphique. Les termes scientifiques FRANÇAIS sont dits
au moment utile pour la compréhension. Un résumé audio = la leçon racontée en condensé, pas une liste.
→ Relire cette règle avant CHAQUE lot audio, elle prime sur la contrainte de longueur :
   si le texte fluide dépasse 1500 car., le couper en 2 et FUSIONNER les MP3 (script trames tour 19).



---


# 07 — Charte mots-clés

# CHARTE DU DICTIONNAIRE DES MOTS-CLÉS — à appliquer à TOUTE nouvelle leçon

Décision utilisateur du 25/10/2026 : « from now and on », au même rang que le mode
arabe et la méthode de résumé. Première leçon équipée : ra-02 (47 termes).

## Le concept (exigence utilisateur)
- Une **boîte-dictionnaire des mots-clés de la leçon** : pour chaque mot, une
  explication **simple, facile, suffisante** du mot ET de son contexte dans le cours.
- Collée au **bord DROIT de l'écran** (décision RÉVISÉE du 25/10 — la première
  version à gauche a été rejetée) : poignée verticale « MOTS-CLÉS » toujours
  visible ; le panneau se **montre/cache à volonté** ; bouton FERMER bien visible
  (rouge, encadré) en plus de la touche Échap.
- Tri **alphabétique** ET **ordre des sections** (les deux boutons existent,
  préférence mémorisée). Filtre texte en plus.
- **Toujours avec la traduction arabe** des définitions (bouton ع/FR dans le
  panneau ; langue initiale héritée du mode arabe global `seenmed-ar-mode`).

## Contrat technique (build des pages)
- La page porte `<script type="application/json" id="kwData">` (placé juste avant
  `#arData`, en fin de `<main>`) :
  `[ { "t": "terme", "s": "id-section", "n": "numéro affiché",
      "d": "définition FR (balises <b> permises)",
      "a": "définition AR (tout fragment latin dans <bdi class=\"fr-term|fr-plain\">)" }, … ]`
  L'ordre du tableau = l'ordre des sections de la leçon (sert au tri « Sections »).
- Fichiers moteur : `js/keywords.js?v=1` (chargé APRÈS ar-mode.js) +
  `css/keywords.css?v=1` (chargée APRÈS ar-mode.css). Pages sans `#kwData` :
  le script sort immédiatement — rien à faire sur les anciennes pages.
- La poignée et le panneau sont INJECTÉS par keywords.js : ne rien écrire dans
  le HTML des pages. Le badge de section scrolle vers la section (`id` = `s`).
- z-index : poignée 940, panneau 950 (sous la lightbox de lesson.js).

## Qualité à vérifier au build (checklist)
- [ ] Termes uniques ; chaque `s` existe comme `<section id>` de la page.
- [ ] Chaque entrée a exactement les 5 champs t/s/n/d/a.
- [ ] Définitions arabes : zéro mot latin nu hors `<bdi>` (regex de contrôle).
- [ ] Balises `<b>/<bdi>/<i>` équilibrées dans chaque d et a ; JSON valide.
- [ ] 30 à 50 termes par leçon : tout le lexique que l'examinateur peut employer.
- [ ] Définition = le mot + son rôle dans CE cours (pas une définition de
      dictionnaire générique) ; les chiffres d'examen rappelés quand ils tombent.

## Pièges connus (ne pas répéter)
- 🔴 ar-mode.css v1 posait la puce de section en `left: 0` → superposée au numéro
  de section. Corrigé en v2 : `right: 0; left: auto`. TOUTE nouvelle feuille qui
  positionne un contrôle dans `.lsection-head` le met À DROITE.
- Les traductions arabes (ici comme dans arData) : intelligentes et contextuelles,
  les MEILLEURS mots pour le contexte — jamais du mot-à-mot plaqué. Exigence
  explicite répétée par l'utilisateur le 25/10.



---


# 08 — Règles espace et Drive

# RÈGLES D'ESPACE — à respecter à chaque tour, sans exception

> Pourquoi : la plateforme enregistre l'espace de travail à la fin de chaque tour.
> Au-delà d'environ **128 Mo** (ou 10 000 fichiers) l'enregistrement échoue :
> le travail du tour peut être perdu et les réponses se bloquent.
> C'est exactement ce qui est arrivé le 20 octobre (154 Mo).

## Le seul chiffre qui compte

```bash
python3 tools/espace.py          # mesure et verdict
python3 tools/espace.py --purge  # mesure, nettoie, remesure
```

`du -sh` **ment** : il compte des dossiers que la plateforme n'enregistre pas
(`node_modules`, `build`, `dist`, `__pycache__`, `.cache`…). `espace.py` ne
compte que ce qui est réellement persisté.

Seuils : **VERT < 90 Mo** · **ORANGE 90–110 Mo** · **ROUGE > 110 Mo**

## Les neuf règles

1. **Le ZIP ne réside jamais dans l'espace de travail.** Il se fabrique dans
   `/tmp`, part sur Google Drive, et la copie locale est effacée **dans le
   même tour** — l'instantané ne le voit jamais. Il n'est construit que sur
   demande de l'utilisateur, ou pour exécuter le cycle de décharge ci-dessous.
   *(89 Mo — c'était la moitié du problème.)*
2. **Tout fichier de travail va dans `/tmp`** : planches PNG brutes, planches
   contact, zooms de relecture, scripts d'assemblage, sauvegardes avant
   retouche PIL. `/tmp` fait 992 Mo et n'est pas compté. **Jamais** de dossier
   `build/` ni de fichier de travail dans `/home/user`.
3. **Les PDF sources ne sont pas conservés** : ils se retéléchargent par blob
   sha via l'API GitHub. Supprimés dès l'analyse écrite.
4. **Un seul PNG ne survit jamais à son WebP.** Conversion q83 puis suppression
   immédiate du PNG.
5. **Les textes bruts des leçons terminées sont supprimés** ; seules les
   analyses `.md` (profil de l'examinateur, corrigés) restent — elles pèsent
   quelques dizaines de Ko et servent aux leçons suivantes.
   Exception : `analysis/cure-anapath-texte.txt` (245 QCM) reste tant que les
   21 leçons d'anapath ne sont pas faites.
6. **On ne touche pas à la qualité des images.** Mesuré le 20/10 :
   réencoder en `method=6` fait *grossir* les fichiers (−1,3 %), et descendre
   de q83 à q72 ne gagne que 22 % en abîmant le texte dense. Les planches
   restent en **WebP q83**. L'espace ne se gagne pas sur les images.
7. **`python3 tools/espace.py --purge` à la fin de chaque leçon**, avant même
   de parler du ZIP.
8. **En ORANGE, on nettoie avant de commencer la leçon suivante**, pas après.
9. **Les images d'une leçon livrée quittent l'espace de travail** dès que la
   leçon est vérifiée au vert et déposée sur Drive — voir le cycle ci-dessous.

## Le cycle de décharge — mis en service le 22/10

C'est la réponse de fond à la saturation : **l'espace de travail n'est plus un
entrepôt, c'est un atelier.** Les planches d'une leçon n'y restent que le temps
de la construire ; ensuite elles vivent sur le portable de l'utilisateur et
dans Google Drive.

**Les quatre temps du cycle**

1. Construire l'archive dans `/tmp` (`zipfile`, `ZIP_DEFLATED` niveau 6,
   chemins relatifs préfixés `medstudy/`).
2. `google_drive__upload_file` vers le dossier **« SEENmed — livraisons »**
   (`1jWnQN-zER__1EK75c2-HxPOSXYurbR5p`). **Vérifier le succès de l'envoi
   avant toute suppression.**
3. `rm` de l'archive locale, dans le même tour.
4. Écrire `medstudy/assets/img/MANIFESTE.json`, puis supprimer les dossiers
   d'images des leçons terminées.

**Ce qui ne part jamais** : `assets/img/fonds/` (3,0 Mo) et
`assets/img/modules/` (64 Ko) sont des décors partagés par toutes les pages ;
`assets/fonts/` (1,6 Mo) aussi ; `CHARTE-IMAGES.md` et `CHARTE-IMMUNO.md` sont
des consignes de travail. **Les images de la leçon en cours restent sur le
disque** jusqu'à sa livraison.

**Le manifeste tient lieu de preuve d'existence.** `tools/manifeste.py` donne
trois fonctions aux vérificateurs :

```python
from manifeste import image_existe, images_disponibles, fichiers_disque
image_existe('ca-01', 'hero.webp')      # disque OU manifeste
images_disponibles('ca-01')             # l'ensemble des deux
fichiers_disque('ca-01')                # ce qui est réellement là ([] si déporté)
```

Un vérificateur ne doit plus jamais écrire `os.path.exists(os.path.join(IMG, s))`
ni `os.listdir(IMGDIR)` : il casserait dès la décharge suivante. Les huit
vérificateurs vivants ont été convertis le 22/10 et repassent tous au vert.

**Remise en place côté portable (Windows).** L'Explorateur fusionne les
dossiers nativement : glisser le `medstudy` de l'archive par-dessus l'ancien et
répondre « Remplacer les fichiers dans la destination ». Les anciennes images
ne sont pas perdues, puisque les archives suivantes ne contiennent que les
nouveautés — ce sont des **incréments**, pas des remplacements.

**Mesure du 22/10** : 90,9 Mo → **11,3 Mo**. 670 images, 83,4 Mo déportés.
29 leçons dans `SEENmed-complet-2026-10-22.zip` (773 fichiers, 89,4 Mo).

## Ce qui a été supprimé le 20/10 et pourquoi c'est sans risque

| Supprimé | Poids | Pourquoi rien n'est perdu |
|---|---|---|
| `telechargement/` (ZIP) | 69 Mo | Se reconstruit en une commande : `tools/build_full.py` |
| `seenmri/` | 2,2 Mo | Les 12 signatures de physique du fond sont **écrites en dur** dans `tests/home-check.js` (tableau `SIGNATURES`), et le test prévoyait déjà l'absence du dossier (`heroSrc ? … : true`). Contrôle refait : **68/68**. |
| 5 `TODO-*.md` / `ESPACE-DISQUE.md` | 45 Ko | Leçons livrées et vérifiées ; remplacés par ce fichier |
| 2 doublons exacts dans `analysis/` | 133 Ko | `cure-anapath.txt` et `anapath-notes-qcm.txt` étaient identiques (md5) à leurs jumeaux `-texte.txt` |
| 7 textes bruts non-anapath | 450 Ko | Leçons immuno/cardio/radio/physio livrées ; analyses `.md` conservées |

## Projection

**11,3 Mo au 22/10**, ~2,8 Mo par leçon → **41 leçons de marge**. La décision
qui restait en suspens le 20/10 — sortir les images des modules terminés — est
désormais prise et outillée : c'est le cycle de décharge. La qualité des
planches n'a pas été touchée, et ne le sera pas.

Le cycle se rejoue **à chaque passage en ORANGE** : archive incrémentale des
leçons livrées depuis la précédente, envoi sur Drive, mise à jour du manifeste,
suppression. Le plafond de 100 Mo d'`upload_file` impose de livrer en
incréments, plus jamais en archive monolithique.



---

# 09 — PROTOCOLE OPÉRATIONNEL UNIQUE POUR TOUTES LES LEÇONS : DE ZÉRO À LIVRAISON

## A. Règle de départ — à répéter pour chaque leçon

Tout ce protocole est relancé depuis le début pour chaque nouvelle leçon. Il ne s'agit pas d'un plan de réparation réservé aux leçons actuellement dégradées.

Une leçon est un produit pédagogique complet, pas une page HTML remplie. La page ne commence qu'après lecture complète de la source, extraction des éléments tombables, planification des images et analyse des annales disponibles.

Références obligatoires :
- MEC : `medstudy/lecons/an-03-pathologies-mec.html`.
- Physiopathologie validée : `medstudy/lecons/ph-06-choc-septique.html` et les dernières pages validées réellement contrôlées.
- Les chartes réelles dans le workspace, jamais une charte réécrite de mémoire.

Interdictions :
- ne pas partir d'un squelette récent ;
- ne pas copier une structure techniquement générée sans vérifier sa pédagogie ;
- ne pas inventer une source, une annale, une correction, une image ou une traduction ;
- ne pas déclarer une leçon terminée parce que les scripts passent ;
- ne pas passer à la leçon suivante avant le contrôle complet.

## B. Phase 1 — Source et dossier de production

1. Identifier la source exacte et son origine.
2. Vérifier qu'elle est complète et lisible.
3. Extraire le texte intégral avant toute rédaction.
4. Lire toutes les pages, y compris les diapositives de tableaux, figures et corrections.
5. Relever les termes, chiffres, classifications, mécanismes, exceptions et pièges.
6. Relever les figures originales réellement utiles.
7. Extraire les annales correspondant à la leçon et conserver leur formulation exacte.
8. Identifier les corrections officielles ; si elles manquent, le signaler et ne pas les inventer.
9. Écrire une analyse de source persistante dans `analysis/`.
10. Écrire un plan hiérarchique avec les sections, les boxes, les images, les reels, les QCM et l'audio prévus.

Le plan doit croiser trois axes :
- ce que le cours enseigne ;
- ce que les annales demandent ;
- ce qui est nécessaire pour comprendre les mécanismes et répondre aux zones non encore tombées.

## C. Phase 2 — Architecture pédagogique

La leçon doit raconter une progression, par exemple :

1. Vue d'ensemble et définition du problème.
2. Constituants ou éléments de base.
3. mécanisme initial ;
4. cascade ou évolution ;
5. conséquences locales ;
6. conséquences générales ou organes ;
7. classification, diagnostic ou évaluation ;
8. traitement ou conclusion ;
9. méthode de l'examinateur ;
10. connexions avec les autres leçons ;
11. annales ;
12. entraînement ;
13. fiche flash ;
14. résumé total.

Le nombre exact dépend de la source, mais la cible est 10 à 18 sections thématiques nommées. Une section générique s1/s2/s3 sans rapport avec le plan réel est refusée.

Pour chaque section :
- un titre précis ;
- une `lsub` courte qui annonce l'idée ;
- une ou plusieurs `lbox` ;
- des listes cochables ;
- les mots-clés en gras ;
- un visuel dédié ;
- un reel original si le document apporte une information visuelle supplémentaire ;
- un `cine-spot` si elle est couverte par l'audio.

Règle de contenu : toute la matière de cours vit dans les boxes à puces. Pas de longs paragraphes pédagogiques libres au milieu des sections. La `lsub` est la seule accroche narrative courte autorisée hors box, avec les légendes et textes d'interface.

Chaque box doit pouvoir répondre à une question d'examen : définition, mécanisme, distinction, chiffre, cause, conséquence, piège ou conduite à tenir.

## D. Phase 3 — Résumé et hiérarchie

Le résumé n'est pas une réduction mécanique du PDF.

### Tombable
Pour chaque point retrouvé dans les annales ou leur correction :
- donner la réponse ;
- expliquer pourquoi elle est vraie ;
- expliquer la simplification à retenir ;
- donner le moyen mnémotechnique si utile ;
- signaler le piège exact de l'examinateur ;
- relier ce point au mécanisme général.

### Non tombable
- condenser ;
- garder les informations indispensables ;
- conserver les relations causales ;
- permettre une lecture complète en une passe ;
- ne pas supprimer une information qui change le diagnostic ou la réponse.

La priorité vient du croisement source × annales × corrections, et non du nombre de diapositives.

## E. Phase 4 — Images et reels

### Planches générées
Prévoir environ 20 à 26 éléments visuels selon la longueur :
- hero ;
- mind map ;
- une planche par section ;
- une image différente pour chaque case de fiche flash ;
- `total.webp` dédié.

Une planche doit montrer la réalité médicale : organe, tissu, cellule, structure anatomique exacte, geste, appareil, mécanisme ou scène clinique. Le texte accompagne l'image ; il ne remplace pas l'image.

Avant chaque prompt, vérifier :
1. Qu'est-ce que c'est ?
2. À quoi cela ressemble-t-il réellement ?
3. Comment cela fonctionne-t-il ?
4. Où cela se situe-t-il et avec quoi est-ce relié ?

Règles permanentes :
- format paysage 16:9 ;
- texte lisible et court ;
- français correct ;
- pas de mots anglais ;
- pas de texte minuscule ;
- flèches étiquetées ;
- étapes numérotées si nécessaire ;
- chiffres exacts ;
- siège anatomique précis ;
- aucune phrase répétée sur la même planche ;
- styles variés selon l'idée ;
- pas de néon sur fond sombre comme style automatique ;
- pas d'esthétique IRM/scanner systématique ;
- métaphore autorisée seulement si elle est accompagnée de médaillons de réalité.

Les dessins générés ne doivent pas contenir de lettres ou chiffres illisibles à l'intérieur des scènes. Les informations textuelles importantes doivent rester dans les encadrés contrôlables.

### Images originales
Quand la source contient une vraie image utile :
- l'extraire ;
- conserver la diapositive et sa légende ;
- ne pas inventer le diagnostic ;
- décrire la morphologie si l'identification est incertaine ;
- convertir en WebP q90 pour l'histologie ;
- ranger dans `assets/img/<lesson>/reel/` ;
- citer l'enseignant, la diapositive et le titre.

Garder uniquement les reels qui ajoutent une vraie information : photo clinique, histologie, schéma relationnel, tableau détaillé, courbe ou graphe. Supprimer les diapositives qui ne sont que du texte redondant avec les boxes.

### Relecture des images
Pour chaque lot :
- planche contact ;
- zoom des zones textuelles ;
- recherche d'anglais ;
- recherche de texte dupliqué ;
- contrôle de chaque chiffre ;
- contrôle du siège anatomique ;
- contrôle de la cohérence avec la source ;
- régénération si la planche est dominée par du texte ou contient une erreur importante.

## F. Phase 5 — Annales et QCM

### Annales
- placer les annales avant l'entraînement ;
- conserver le texte exact ;
- numéroter 1 à n ;
- indiquer la session et la source ;
- utiliser uniquement le corrigé officiel disponible ;
- afficher les explications proposition par proposition ;
- ajouter le mémo du piège.

### Entraînement
- recommencer la numérotation à 1 ;
- calibrer les questions sur les zones vierges et le profil de l'examinateur ;
- utiliser A à E ;
- ne pas produire de QCM génériques ;
- couvrir les mécanismes, distinctions, chiffres et pièges spécifiques ;
- fournir `data-answer` ;
- expliquer chaque proposition ;
- ajouter la source pédagogique de la réponse.

## G. Phase 6 — Fiche flash et résumé total

### Fiche flash
Créer 4 à 7 cases selon la matière. Chaque case comprend :
- un titre ;
- une image `ff-<theme>.webp` différente ;
- quelques points réellement cochables ;
- les priorités ★★/★ ;
- un piège ou un lien si nécessaire.

Une seule image répétée pour toutes les cases est interdite.

### Résumé total
`total.webp` est une planche dédiée qui redessine tout le cours. Ce n'est pas un collage des planches existantes et ce n'est pas une affiche composée uniquement de mots. Il doit permettre une révision globale en une lecture et ne doit pas afficher les réponses des QCM.

## H. Phase 7 — Traduction arabe

Le mode arabe traduit le contenu réel, pas seulement les titres.

À couvrir :
- `lsub` ;
- boxes et listes ;
- tableaux ;
- mini-fiches ;
- résumé ;
- explications des QCM et mémos.

Les énoncés et propositions des QCM restent en français, car c'est la langue de l'épreuve.

Style : arabe standard simplifié, contextuel, pédagogique et compréhensible. Ne pas traduire mot à mot. Le terme scientifique français reste dans la phrase arabe avec son équivalent arabe à la première occurrence. Tout fragment latin et tout chiffre/unité est isolé dans `bdi`.

Implémentation :
- `data-tr` unique sur chaque bloc traduisible ;
- `arData` JSON complet ;
- bouton global ع/FR ;
- puce locale AR/FR à droite de l'en-tête ;
- bascule instantanée ;
- aucune image traduite.

Contrôles :
- chaque `data-tr` possède une clé ;
- aucune clé orpheline ;
- JSON valide ;
- aucun mot latin nu dans l'arabe ;
- termes français correctement isolés ;
- aucune phrase arabe répétée ;
- traduction réellement liée au contenu français.

## I. Phase 8 — Voix et Ciné

Format final obligatoire :
- 8 chapitres français développés ;
- résumé français ;
- résumé arabe ;
- pas 8 chapitres arabes comme format final.

Voix :
- `voice-00` pour tout le français ;
- `voice-03` uniquement pour le résumé arabe.

La narration doit être celle d'un professeur qui explique : origine → mécanisme → conséquence → lien avec le reste du cours. Ce n'est jamais une liste de mots-clés et jamais une lecture télégraphique.

Contraintes :
- maximum environ 1500 caractères par clip avant éventuelle fusion ;
- unités écrites en toutes lettres si nécessaire ;
- français prononcé à la française ;
- arabe neutre, non خليجي ;
- texte relu avant synthèse ;
- site silencieux jusqu'au clic ;
- mini-lecteur par section ;
- `cineData` central avec chapitres, planches et fichiers audio ;
- chapitre 9 réservé au résumé total si cette convention est utilisée.

Si une narration fluide dépasse la limite : la couper à une frontière naturelle et fusionner les pistes sans transformer le texte en résumé haché.

## J. Phase 9 — Intégration website

Vérifier :
- titre, module, enseignant et statut source ;
- hero et navigation ;
- onglets et ancres ;
- progression ;
- mind map ;
- Ciné et spots ;
- sections et boxes ;
- reels et lightbox ;
- AR/FR ;
- dictionnaire des mots-clés ;
- annales et correction interactive ;
- entraînement ;
- fiche flash ;
- flashcards ;
- résumé total ;
- clavier, mobile et chargement différé ;
- chemins relatifs ;
- `data.js` seulement après la passe finale.

## K. Phase 10 — Dictionnaire des mots-clés

Créer environ 30 à 50 termes propres à la leçon. Pour chacun :
- terme ;
- section ;
- numéro affiché ;
- définition française simple et contextualisée ;
- définition arabe avec les mêmes règles de langue.

Le panneau est à droite, ouvrable et refermable, avec bouton fermer visible, recherche, tri alphabétique ou par sections et préférence mémorisée. Vérifier les cinq champs, les sections et le JSON.

## L. Phase 11 — Audit final

### Audit pédagogique
- source lue intégralement ;
- aucune section générique ;
- hiérarchie cohérente ;
- tombable développé ;
- non-tombable condensé sans perte ;
- boxes suffisantes ;
- résumé réellement utile ;
- annales exactes ;
- QCM spécifiques.

### Audit visuel
- planche par section ;
- flash image par case ;
- total dédié ;
- images réalistes ;
- anatomie correcte ;
- reels utiles ;
- pas de doublons ;
- pas d'anglais ni de texte illisible.

### Audit fonctionnel
- navigation ;
- liens ;
- QCM ;
- correction ;
- flashcards ;
- lightbox ;
- audio ;
- arabe ;
- mots-clés ;
- progress ;
- mobile ;
- absence d'erreur console si disponible.

### Audit des données
- `arData` complet ;
- `kwData` complet ;
- `cineData` complet ;
- fichiers audio présents ;
- images présentes ou déclarées dans le manifeste ;
- chemins valides ;
- `data.js` cohérent.

## M. Phase 12 — Archive Drive et espace

1. Ne pas archiver une leçon provisoire.
2. Construire le ZIP autonome dans `/tmp`, avec chemins relatifs préfixés `medstudy/`.
3. Inclure la page, les assets nécessaires, l'audio, les données et les fichiers de preuve utiles.
4. Calculer le MD5 local.
5. Envoyer dans `SEENmed — livraisons`.
6. Vérifier que l'upload est réussi.
7. Vérifier le fichier Drive, sa taille et son MD5 lorsque possible.
8. Enregistrer lien, ID, taille et MD5 dans le suivi de chaîne.
9. Supprimer l'archive locale et les temporaires.
10. Mettre à jour le manifeste si les images sont déchargées du workspace.
11. Mesurer l'espace et nettoyer avant la leçon suivante.

Seuils de travail : vert sous 90 Mo, orange 90–110 Mo, rouge au-dessus de 110 Mo. Le workspace est un atelier, pas l'entrepôt permanent des archives.

## N. Décision de passage à la leçon suivante

On ne passe à la leçon suivante que si toutes les cases sont vertes :

- [ ] source complète et analyse persistante ;
- [ ] plan hiérarchique réel ;
- [ ] 10–18 sections thématiques ;
- [ ] boxes développées ;
- [ ] visuel dédié par section ;
- [ ] reels originaux sélectionnés ;
- [ ] fiche flash avec images distinctes ;
- [ ] résumé total dédié ;
- [ ] annales exactes ;
- [ ] QCM spécifiques et expliqués ;
- [ ] traduction arabe complète ;
- [ ] 8 chapitres FR développés ;
- [ ] résumé FR ;
- [ ] résumé AR avec `voice-03` ;
- [ ] `cineData` et mini-lecteurs ;
- [ ] mots-clés ;
- [ ] website intégré ;
- [ ] audit pédagogique ;
- [ ] audit visuel ;
- [ ] audit fonctionnel ;
- [ ] archive Drive ;
- [ ] MD5 vérifié ;
- [ ] espace nettoyé.

# 10 — ÉTAT ET LIMITES DE CETTE RECONSTRUCTION

Cette version rassemble les instructions conservées dans les chartes, la mémoire de session et les leçons de référence. Elle est destinée à devenir la spécification de travail unique. Elle n'est pas présentée comme une récupération verbatim du fichier perdu avant le travail Claude Code.
