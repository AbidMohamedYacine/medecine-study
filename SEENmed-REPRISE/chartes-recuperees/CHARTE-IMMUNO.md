# CHARTE VISUELLE — MODULE IMMUNOLOGIE (SEENmed)

Toutes les images du module immuno (im-01 → im-17) utilisent **le même casting**,
**les mêmes couleurs** et **les mêmes formes**. Une cellule vue dans la fiche 1 doit
être reconnaissable instantanément dans la fiche 9. Objectif : précision scientifique
+ mémorisation visuelle + continuité d'une image à l'autre.

## 1. Rendu général
- Illustration scientifique de manuel d'immunologie moderne, traits nets, volumes doux.
- Fond bleu nuit profond (#0a0e1a → #0f1830), lueurs bleu #0077ff et turquoise #00d4aa.
- Étiquettes **en français**, blanches, courtes, reliées par des filets fins ; flèches numérotées.
- Pas de texte long sur l'image : des **mots-clés** + des **chiffres d'étape**.
- Chaque image porte en bas une **bande-légende** reprenant les symboles utilisés.

## 2. Le casting constant (forme + couleur + rôle + emplacement)

| Acteur | Forme imposée | Couleur | Rôle | Emplacement habituel |
|---|---|---|---|---|
| **Mastocyte** | grande cellule ronde **bourrée de granules** | violet, granules roses | dégranulation, histamine | **sous l'épithélium** des muqueuses et de la peau |
| **Basophile** | granules gros et sombres, noyau bilobé | bleu-noir | amines vasoactives | **sang** |
| **Éosinophile** | noyau **bilobé** (lunettes), granules gros | orange vif | défense antiparasitaire, HS tardive | sang → **tissu** |
| **PNN** | noyau **polylobé** (3-5 lobes) | rose pâle | phagocytose, enzymes | sang → **paroi vasculaire** |
| **Macrophage** | grande amibe à pseudopodes | orange brûlé | phagocytose, granulome | **tissus** |
| **Cellule dendritique** | étoile à longs prolongements | jaune doré | présentation d'antigène | peau/muqueuse → **ganglion** |
| **Lymphocyte B** | petite cellule, gros noyau, **BCR en Y** en surface | bleu clair | anticorps | **ganglion**, follicule |
| **Plasmocyte** | ovale, noyau **excentré en roue de charrette**, halo clair | bleu profond | usine à Ig | **moelle osseuse** |
| **LT CD4 Th1** | lymphocyte badge « Th1 » | vert sapin | IFN-γ → macrophage | tissu, granulome |
| **LT CD4 Th2** | lymphocyte badge « Th2 » | vert menthe | IL-4/IL-5/IL-13 → IgE, éosinophile | muqueuse |
| **LT CD4 Th17** | lymphocyte badge « Th17 » | vert olive | IL-17 → PNN | muqueuse |
| **Treg** | lymphocyte badge « Treg », petit bouclier | turquoise | tolérance, TGF | partout |
| **LT CD8 / CTL** | lymphocyte avec **granules de perforine** | rouge brique | cytotoxicité | tissu infecté |
| **Cellule NK** | lymphocyte large, granules, **récepteur FcR en crochet** | violet-bleu | ADCC | sang, tissu |
| **Cellule cible / épithélium** | cellules cubiques alignées | gris-bleu pâle | victime | tissu |

## 3. Les molécules (toujours dessinées pareil)
- **IgE** : Y fin **cyan**, toujours **posée sur le récepteur FcεRI** (ancre en U) du mastocyte.
- **IgG** : Y **bleu roi**, Fab en haut (reconnaissance), **Fc en bas** (effecteur).
- **IgM** : **pentamère** bleu foncé en étoile.
- **IgA** : dimère vert d'eau avec pièce sécrétoire, sur les muqueuses.
- **Complexe immun** : amas Ag (petits ronds rouges) + IgG, **flottant** puis **déposé**.
- **Complément** : chaîne de billes **turquoise** (C1 → C9), le **CAM** = tube planté dans la membrane.
- **HLA / CMH** : **plateforme rectangulaire grise** portant un **peptide** (bâtonnet rouge) ; classe I = sur toutes les cellules, classe II = sur les CPA.
- **TCR** : fourche à deux branches ; **BCR** : Y ancré.
- **Cytokines** : petites sphères colorées étiquetées (IL-4, IL-5, IFN-γ…).
- **Pic monoclonal** : courbe d'électrophorèse avec **pic étroit** en zone γ.

## 4. Code couleur des 4 cadres (constant dans tout le module)
- **Hypersensibilités** = rouge corail · **Auto-immunité** = violet · **Déficits immunitaires** = bleu acier · **Gammapathies monoclonales** = vert émeraude.

## 5. Règle de continuité
Chaque image doit contenir **au moins un acteur déjà vu** dans l'image précédente,
dessiné à l'identique, pour que l'œil fasse le lien : le mastocyte de la fiche
« type I » est le même que celui de la fiche « mécanismes » et de la fiche flash.

## 6. Recette de prompt validée (im-01, lot définitif)
Trois règles ont supprimé 100 % des mots déformés et des retours à l'anglais :

1. **Liste blanche de texte.** Terminer chaque prompt par :
   « RÈGLE DE TEXTE STRICTE : n'écrire QUE des chaînes de cette liste … Liste exacte autorisée : "…", "…" … Aucun autre mot nulle part. »
   Le générateur respecte la liste au mot près.
2. **Interdiction nominative de l'anglais.** Lister les mots anglais à ne jamais écrire
   (cell, mast, plasma, dendritic, eosinophil, platelets, immune complex, apoptosis).
   Sans cette ligne, les schémas en pipeline rebasculent en anglais.
3. **Jamais de nom de couleur dans un libellé.** Écrire « teinte corail » comme consigne
   de dessin, et ajouter « Aucun nom de couleur écrit sur l'image ».

Compléments :
- Décrire le **contenu de chaque pictogramme** (sinon le modèle dessine des cadres vides).
- Pour une grille de cases : donner l'en-tête ET les étiquettes de chaque case,
  et ajouter « jamais deux fois le même texte dans une case ».
- Pour des titres multiples : « les quatre titres sont tous différents, aucun n'est répété ».
- Symboles grecs → les écrire en lettres latines (« lambda », « Gamma »), jamais λ ni γ.
- Toujours : « format paysage 16/9 (1376x768) ». Prompt ≤ 450 mots.

## 7. Casting ajouté pour l'immunité anti-infectieuse (im-02 →)
| Acteur | Forme imposée | Couleur |
|---|---|---|
| **Bactérie** | bâtonnet, ou sphère en **grappe / chaînette** | gris-vert |
| **Capsule** | halo gélatineux clair autour de la bactérie | translucide |
| **Flagelle / pili** | long filament ondulant / courts poils | gris-vert |
| **Paroi** | **double trait** épais ; ADN = boucle circulaire libre | — |
| **Épithélium** | rangée de cellules **cubiques soudées**, cils ondulants | gris-bleu pâle |
| **Mucus** | voile translucide au-dessus de l'épithélium | — |
| **Pus** | poche jaunâtre entourée de PNN roses | jaune pâle |
| **Granulome** | centre clair, couronne de cellules épithélioïdes, couronne externe de lymphocytes | — |
| **PAMP / PRR** | motif **hexagonal** sur la bactérie / récepteur en **fourche** | — |

Mind map **im-02 = plan de forteresse à trois enceintes** (style consommé).

## 8. Mises en page consommées (ne pas répéter telles quelles)
im-01 : frise, roue, tableau à bandeaux de groupe, balance, coupe en étages.
im-02 : forteresse à 3 enceintes (mind map), planche d'histologie à cercles de zoom,
parcours fléché à stations, tableau matriciel 4 colonnes + éventail, rosace à 6 secteurs,
diptyque 2 panneaux, réseau radial hexagonal, fiche 3 bandes, fiche 2 colonnes à pictos,
3 coupes anatomiques juxtaposées, fiche en 4 quartiers, comparatif vaisseau/cascade,
affiche en grille 4x3 + bandeau de réponses (résumé total).

## 9. im-03 — casting et mises en page consommées
Casting : protozoaire = forme ovale violette à noyau · helminthe = long ver beige annelé,
cuticule en double trait · larve = petit ver fin · ILC2 = cellule ronde pâle SANS récepteur
de surface · regDC = étoile grise terne · Treg = turquoise à récepteurs de surface ·
éosinophile = orange bilobé à gros grains · kyste = rond à double paroi.
Mises en page consommées : carte hydrographique tropicale (mind map), arbre de
classification + bande d'épidémiologie, cellule en coupe + tableau de rappel, composition
en miroir autour d'un axe, cascade descendante à 3 étages, triptyque, 3 colonnes à
bandeaux + éventail à 6 branches, chaîne en Y, circuit en boucle + tableau, diptyque
aigu/chronique, grille de 6 vignettes numérotées + bandeau, réseau radial hexagonal
entrant/sortant, fiche en éventail à 3 volets, tableau-affiche à pastilles, fiche 2 bandes,
comparatif 2 colonnes, grille-affiche 4x3 + bandeau de réponses.

## 10. Pièges de génération confirmés sur im-03
- Le modèle **invente des sous-types lymphocytaires** (« Th31 », « Th3 ») dès qu'on lui
  demande un éventail. Parade : « exactement six flèches, pas une de plus » + interdiction
  nominative des sigles inventés.
- Il **oublie la dernière ligne d'un tableau** long. Parade : « la dernière ligne est celle
  du Th22 ».
- Il **ajoute des légendes de son cru** dans les cadres secondaires, parfois fautives
  (« oponisation de la parasite »). Parade : « ce cadre ne porte que deux étiquettes et
  rien d'autre » + interdiction nominative du mot fautif probable.
- Budget : viser **moins de 350 mots**. Les tournures du type « compte bien jusqu'à six »
  coûtent cher et déclenchent MAX_TOKENS.

## 11. sg-00 — « métaphore porteuse » et règle de visibilité (consigne utilisateur)

**Consigne reçue :** « use the proper styles for the informations… more representatif
of the idea and presenting it and it's shape and little explanation to remember it »
puis « make it more visible like it's place and how it looks ».
→ Deux règles permanentes :

1. **La forme du dessin EST l'explication.** Choisir la métaphore dont la géométrie
   reproduit le raisonnement, pas une simple grille colorée.
2. **Montrer l'endroit et l'aspect.** Dès qu'une notion a un siège corporel, dessiner
   une carte du corps + des gros plans cliniques réalistes reliés par un trait.
   Ajouter systématiquement au prompt : « typographie GRANDE et très lisible,
   aucun texte minuscule » et « l'image est remplie sans vide ».

### Les 22 mises en page de sg-00
| Image | Métaphore | Ce que la forme démontre |
|---|---|---|
| mindmap | **Montre de poche ouverte**, 5 roues nues + 5 cartes périphériques | engrenage = enchaînement obligatoire des notions |
| syndrome | Puzzle → rouage → éventail de portes | pièces = signes, rouage = mécanisme, portes = causes ouvertes |
| maladie | Carte d'identité à 5 champs + cascade à 3 paliers | état civil de la maladie ; pourquoi → comment → conséquences |
| diagnostic | Escalier à 6 marches + poteau à 5 flèches + pictogrammes de foule | on ne saute pas une marche ; foule = incidence/létalité |
| pieges | 6 cartes coupées par un ≠ + frise 48 h | la confusion est coupée en deux ; la frise déroule Charcot |
| connexions | **Temple grec à 6 colonnes** | socle = la leçon zéro ; l'étymologie grecque est le sujet |
| ff-mots | Machine à 3 blocs crantés + grande flèche vers la gauche | lecture de la fin vers le début rendue visible |
| ff-signes | Meuble à 4 tiroirs ouverts | classer = ranger |
| ff-valeur | Échelle à 3 barreaux + cloche + 6 médaillons gestuels | la valeur monte ; chaque éponyme montre son geste |
| ff-syndrome | **Carte du corps + 5 gros plans cliniques** | où ça se voit et à quoi ça ressemble |
| ff-maladie | Frise du temps, flèches avant/après le drapeau de guérison | rechute ≠ récidive devient indiscutable |
| ff-diagnostic | 6 chevrons + 5 pastilles ? + 3 cartes + foule | la démarche descend, les questions s'empilent |
| total | 4 bandes : titre / 12 blocs numérotés / bande dorée / réponses | fiche unique |

### Pièges de génération ajoutés
- **Une vignette sans étiquette** : le modèle en oublie une sur cinq → écrire
  « CHACUNE DES CINQ VIGNETTES PORTE SON ÉTIQUETTE, aucune ne reste sans étiquette »
  et préciser la position de chaque étiquette (à sa gauche / à sa droite).
- **Bande vide** : si une bande est annoncée en fin de composition, le modèle la laisse
  parfois vide et déplace son texte dans un bloc voisin → « cette bande N'EST PAS VIDE :
  elle contient la phrase suivante, écrite en entier, sur une seule ligne ».
- **Lettres dans les pictogrammes** : un livre dessiné porte « DIC », une loupe « WORD »
  → « les pictogrammes sont PUREMENT GRAPHIQUES et ne contiennent AUCUNE lettre ».
- **Mot avalé en fin de bloc** : raccourcir la chaîne plutôt qu'élargir le bloc
  (« des signes, un mécanisme, sans préjuger de la cause » → « mêmes signes,
  même mécanisme, cause non précisée »).
- **Roues dentées** : n'écrire AUCUN texte sur la roue, tout sur une carte extérieure
  reliée par un seul trait → supprime définitivement la duplication haut/bas.
- **Liste blanche > 30 entrées = MAX_TOKENS** : regrouper (une chaîne par grappe,
  toutes les réponses d'annales en une seule chaîne).

## §12 — Parades ajoutées par ph-03 (troubles hydrosodés)

**Bandeau dupliqué sur deux objets jumeaux.** Quand la planche montre deux supports côte à côte
(deux fiches, deux panneaux, deux cartes) et qu'une phrase de conclusion doit être commune, le
modèle l'imprime spontanément sur CHACUN des deux. Parade :
« une UNIQUE bande de conclusion pleine largeur est posée TOUT EN BAS DE L'IMAGE, sous les deux
fiches à la fois ; elle n'apparaît qu'UNE SEULE FOIS et n'est imprimée sur AUCUNE des deux fiches ».

**Mot avalé ou répété dans une case trop étroite.** Observé : « CARENCE D'APPORT OU OU PERTES »,
« REIN REIN INADAPTE », « A 285 IIS », « L'OSMOLALITE » sans « PLASMATIQUE ». Ce n'est pas un défaut
de typographie, c'est une case sous-dimensionnée. Double parade :
1. **raccourcir la chaîne** (« PLUS DE 300 : HYPERTONIQUE. 285 : ISOTONIQUE. » au lieu de
   « AU DESSUS DE 300 HYPERTONIQUE, A 285 ISOTONIQUE, » …) ;
2. ajouter « chaque case est GÉNÉREUSEMENT DIMENSIONNÉE pour que sa phrase tienne EN ENTIER :
   aucun mot n'est coupé, abrégé ni avalé, aucun mot n'est répété deux fois de suite ».

**Échec sans image** (`finishReasons:["STOP"], textPartsCount:0`). Distinct du MAX_TOKENS : la requête
est acceptée mais rien n'est rendu, et **le crédit est consommé**. Déclencheur observé : liste blanche
de 12 chaînes dont plusieurs de plus de 15 mots, doublée d'une consigne de composition à deux
organigrammes imbriqués. Parade : ≤ 12 chaînes, chacune courte, et une seule phrase de composition
par support.

**Bande de synthèse en bas d'affiche.** Formulation qui marche à tous les coups :
« une bande d'alerte pleine largeur, HAUTE et bien dégagée, qui N'EST PAS VIDE et qui contient
en entier, sans couper aucun mot, la dernière phrase listée ».

**Règle de contenu (utilisateur, à partir de ph-03).** Le RÉSUMÉ TOTAL ne contient plus la bande
« RÉPONSES DES ANNALES ». Les douze zones + la bande des pièges suffisent.


---

## §13 — Parades validées sur bi-02 (étapes de l'analyse biochimique, 23 images)

### 13.1 Le serpentin est un piège mortel
Un **chemin sinueux / une spirale jalonnée de nombreuses petites cases** produit
**systématiquement des doublons** : deux échecs d'affilée sur le mind map
(CONDITIONS ×2, PRÉLÈVEMENT ×2, VALEURS DE RÉFÉRENCE ×2, et le mot inventé « AUTOIRE »).
**Parade qui marche** : *peu de zones, très grandes, UNE seule longue chaîne par zone*.
Le **retable médiéval à 3 panneaux + 3 cartouches** est passé du premier coup.

### 13.2 Formules mathématiques — NE JAMAIS les écrire en équation
`SÉRUM = PLASMA − FIBRINOGÈNE` est sorti **« SERUM EGALE PLASMA FIBRINOGENE »** :
le modèle a **avalé l'opérateur**, inversant le sens. Les signes `−`, `+`, `=`, `≠`, `×`, `°`
sont fragiles. **Parade** : écrire la relation **en phrase, sans aucun opérateur** —
« LE SÉRUM EST UN PLASMA SANS FIBRINOGÈNE » — et ajouter
« ce cartouche ne contient AUCUN signe mathématique, uniquement des mots ».
Repassé parfait du premier coup.

### 13.3 Le compte explicite d'objets corrige les doublons
« **IL Y A EXACTEMENT N ÉTIQUETTES SUR TOUTE L'IMAGE, pas une de plus** »
a corrigé `pieges` (6e étiquette parasite) et `total` (10 encadrés, exact du premier coup).
Variante pour les jumeaux : « le mot qui désigne X ne figure que sur un seul panneau » (`boucle`).

### 13.4 Bégaiement — supprimer les mots-outils
« POUR LA LA BIOCHIMIE », « OU OU », « REIN REIN » viennent des **prépositions en fin de chaîne**.
**Parade** : écrire « VERT : HEPARINE DE LITHIUM, BIOCHIMIE » et non « …POUR LA BIOCHIMIE »,
+ « aucun mot n'est répété deux fois de suite ». Validé sur `tubes` v2.

### 13.5 Mots inventés
« MACIM » apparu au milieu d'une liste d'abréviations. **Parade** :
« sans ajouter aucun mot qui ne figure pas dans la liste » + « aucun mot inventé ». Validé sur `bilans` v2.

### 13.6 Mises en page classées par fiabilité (bi-02)
| Fiabilité | Mise en page |
|---|---|
| ★★★ | Traits de rappel vers étiquettes **extérieures** (`analytique`, `centrifugation`, `ff-bilans`, `ff-serum`) |
| ★★★ | **Bandes horizontales** numérotées, une chaîne par bande (`conditions`, `bilans`, `transport`) |
| ★★★ | **Objets alignés + une étiquette sous chacun** (`ff-tubes` bouchons, `ff-conditions` étiquettes suspendues) |
| ★★☆ | **Grille de 6 cases** à pictogramme + texte (`ff-pieges`, `modes`) |
| ★★☆ | **3 bandes × encadrés** pour un résumé total (`total`, 10 encadrés — exact) |
| ☆☆☆ | **Serpentin / spirale à petites cases** — à proscrire |

### 13.7 Longueur de chaîne
Au-delà de **~12 mots**, un mot saute en fin de chaîne : « PHOSPHATASE » pour
« PHOSPHATASE ALCALINE » (`ff-bilans`), « GRIS » absent de la liste des tubes (`total`).
**La seule parade est de raccourcir.** Ne pas regénérer pour un mot avalé si l'information
est correcte ailleurs dans la leçon — le risque de casser une bonne composition est supérieur au gain.

### 13.8 Budget d'un lot
**10 générations par tour, pas une de plus.** Rythme tenu sur bi-02 :
~7 nouvelles + 3 reprises, et **relire en vision AVANT d'épuiser le quota**.
Coût réel de la leçon : **26 générations pour 23 images** (3 reprises).


---

## §14 — Parades validées sur bi-03 (stress oxydatif, 22 images, 25 générations)

### 14.1 Un échec MAX_TOKENS n'écrit PAS le fichier
Il consomme pourtant un crédit. **Ne jamais déduire de l'ordre des résultats laquelle a échoué** :
faire un `ls` du dossier. (Erreur commise : j'ai cru que `roles` avait échoué alors que c'était `dommages`.)

### 14.2 Déclencheur réel du MAX_TOKENS
Ce n'est pas le nombre d'objets, c'est la **longueur du descriptif par sous-élément**.
`dommages` a échoué avec **3** zones décrites sur 2 lignes chacune ;
`roles` est passée avec **6** scènes décrites en **une demi-ligne** chacune.
→ **Règle : une ligne maximum par sous-élément, quel que soit leur nombre.**

### 14.3 Le compte explicite d'ÉTIQUETTES, distinct du compte d'objets
Annoncer « deux gros plans » ne suffit pas : `cibles` v1 a produit **3 étiquettes pour 2 objets**
(libellé du cartilage écrit deux fois). La reprise avec
« **IL Y A EXACTEMENT DEUX ETIQUETTES SUR TOUTE L'IMAGE, une à gauche et une à droite** »
est passée du premier coup. **Compter les étiquettes, pas seulement les objets.**

### 14.4 Les textes permutent entre objets si on livre une liste « à répartir »
`connexions` v1 a mis la phrase de synthèse sur l'île centrale et relégué le titre du cours
sur une île périphérique — le moyeu de la métaphore était faux.
**Parade validée : nommer chaque emplacement par sa POSITION et lui affecter son texte.**
« la pancarte de l'île CENTRALE porte exactement : … ; celle de l'île en HAUT À GAUCHE porte exactement : … »
Passé du premier coup, hub et satellites corrects.

### 14.5 Les layouts RADIAUX sont fiables avec un compte explicite
Contredit la crainte issue de bi-02. La **roue à 8 secteurs** (`pathologies`) est passée du premier coup
avec « IL Y A EXACTEMENT HUIT SECTEURS ET HUIT ETIQUETTES ». Idem le **tableau de bord à 8 voyants**.
Ce qui échoue n'est pas le radial en soi, c'est le **serpentin à petites cases sans compte annoncé**.

### 14.6 Les gradations demandées sont respectées
`ff-ero` : « UNE tête de mort au-dessus du premier, DEUX au-dessus du deuxième, QUATRE au-dessus du
troisième, TROIS au-dessus du quatrième » a été rendu **exactement**. On peut donc encoder une
**hiérarchie pédagogique** (ici : le radical hydroxyle est le plus toxique) dans un comptage de pictogrammes.

### 14.7 Mises en page classées par fiabilité (bi-03)
| Fiabilité | Mise en page |
|---|---|
| ★★★ | Objets alignés + une étiquette sous chacun (`ff-ero`, `ff-dommages`, `antiox-non`, `ff-marqueurs`) |
| ★★★ | Grille de N encadrés avec compte annoncé (`total` 8 encadrés, `marqueurs` 6 logements, `roles` 6 cartes) |
| ★★★ | Traits de rappel vers étiquettes extérieures (`dommages`, `cibles` v2, `definition`) |
| ★★★ | Radial à secteurs **avec compte annoncé** (`pathologies`, `ff-patho`) |
| ★★☆ | Hub + satellites — exige la **désignation par position** (`connexions`) |
| ★★★ | Métaphore à deux côtés opposés (`ff-definition` bascule, `ff-sources` deux portes, `ff-antioxydants` bouclier) |

### 14.8 Taux atteint
**25 générations pour 22 images** (2 reprises + 1 échec MAX_TOKENS), soit **88 % du premier coup** —
meilleur score depuis le début, obtenu en appliquant systématiquement §13 et §14.3-14.5.

### 14.9 Harnais de test — garde-fou mémoire
Au-delà de ~15 leçons, jsdom fait sauter le tas par défaut de V8 (`JavaScript heap out of memory`).
`tests/lesson-check.js` **se relance désormais tout seul** avec `--max-old-space-size=4096`
(variable `LC_BIGHEAP`), et `pretendToBeVisual` est passé à `false`. Appel inchangé : `node tests/lesson-check.js`.


## Format de sortie (depuis le tour « version complète »)

Les planches sont enregistrées en **WebP qualité 80**, plus en JPEG q87.
Même rendu à la loupe sur du texte dense, **46 % de poids en moins**.
Conversion : `python3 tools/to_webp.py --sec` puis `--refs`.
Contrôle : `python3 tools/check_images.py` (toutes les pages, 0 image cassée).
