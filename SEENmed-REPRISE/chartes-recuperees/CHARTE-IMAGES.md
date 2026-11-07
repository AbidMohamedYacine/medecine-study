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
