# SEENmed — Audit neutre de reprise (28/10/2026)

> Rédigé par le nouvel agent, **à partir des faits vérifiés directement**
> (repo GitHub + lecture Google Drive en lecture seule + les 6 fichiers transmis).
> Les documents de l'ancien agent sont conservés dans `handoff-ancien-agent/`
> comme **historique à vérifier**, pas comme ordres à exécuter aveuglément.
> Aucune suppression, aucun envoi Drive, aucune modification du site n'a été faite.

**Contexte utilisateur (confirmé par lui le 28/10)** : étudiant en 3ᵉ année de
médecine (Oran, enseignement en français). **Examen de l'unité cardiologie le
26 novembre 2026 (dans 29 jours)**. Deux modules — **immunopathologie et
anatomopathologie — sont examinés séparément fin janvier**. Le site SEENmed
transforme chaque cours en résumé structuré avec planches illustrées, audio
narré (FR + résumé AR), traduction arabe contextuelle, annales, QCM,
flashcards et dictionnaire de mots-clés, selon une méthode précise définie
avec l'utilisateur.

---

## 1. Ce qui existe réellement (vérifié par moi, pas sur parole)

### 1.1 Ce repo GitHub `medecine-study` (branche de travail actuelle)
- **74 fichiers, 114 Mo** : essentiellement les **PDF sources des professeurs**
  (~67 PDF : sémiologie, physiopathologie, radiologie, biochimie, immunologie,
  anapath, psychologie…) + les deux gros recueils **CURE ANAPATH (13 Mo)** et
  **CURE IMMUNO (11 Mo)** + photos.
- **Le code du site SEENmed principal (`medstudy/`, `data.js`, leçons HTML,
  chartes, outils) n'est PAS dans ce repo.** Vérifié : aucun `data.js`,
  aucun dossier `medstudy/`, aucun `espace.py`.
- Deux HTML autonomes anciens : `QCM_Revision_sémiologie.html`,
  `lymphocytes_b_complet (1).html`.
- `seenmri-upload.zip` (18 Mo, 141 fichiers) = un **projet annexe IRM**
  (`seenmri/`), sans rapport avec le site principal de 53 leçons.
- Un seul commit (« Add files via upload ») : **le site n'a jamais été
  versionné sous Git**. C'est une cause racine du chaos (voir §4).

### 1.2 Le dossier Drive que l'utilisateur m'a donné
`MED SEEN THE LATEST VERSION I COULD HAD` (`1OGLXLSX382KqCkEfJD4XrK2xYGlR-Ne7`),
créé le 27/10/2026 18:25 UTC, contient **5 éléments** :

| Élément | Taille | Date (UTC) |
|---|---|---|
| `abacktools-SEENmed-DASHBOARD-FIXED-FULL-53-AN03-06-10-part1-of4.zip` | 83 872 343 o | 28/10 10:38 |
| `…-part2-of4.zip` | 83 416 172 o | 28/10 10:38 |
| `…-part3-of4.zip` | 83 861 192 o | 28/10 10:38 |
| `…-part4-of4.zip` | 77 994 131 o | 28/10 10:39 |
| Dossier `workspace an old version before things goes wrong` | — | modif. 28/10 10:40 |

- Somme des 4 parties = **329 143 838 o**, très proche de la « baseline »
  unique de **329 264 608 o** (écart 120 770 o ≈ surcoût de découpage).
  → **Hypothèse forte (à confirmer par recollage + MD5)** : les « quatre
  parties » sont le **découpage du même ZIP baseline**, pas quatre morceaux
  différents du site. Elles ont été téléversées **aujourd'hui**, après la
  création de la baseline (27/10 23:27).
- Le sous-dossier workspace contient : `workspace-01a17ca1-….zip`
  (**108 440 860 o**, MD5 `db55b0966b0773f47676fcb90e1e2d65`, 27/10 18:23)
  et 5 chartes `.md` que j'ai **lues intégralement** :
  - `CHARTE-LECON.md` (6 679 o) — « restaurée le 26/10 après audit » ;
  - `CHARTE-ARABE.md` (4 943 o), `CHARTE-CINE.md` (5 068 o),
    `CHARTE-MOTS-CLES.md` (3 040 o) — cohérentes avec le document consolidé ;
  - `CHARTE-IMAGES.md` (**877 o seulement**) — ce n'est **pas** la charte :
    c'est un **avertissement** indiquant que la vraie charte (12 Ko) se trouve
    dans `medstudy/assets/img/CHARTE-IMAGES.md`, donc **à l'intérieur des
    ZIPs**, avec `CHARTE-IMMUNO.md`. **Ces deux vraies chartes ne sont
    accessibles nulle part en clair pour l'instant.**

### 1.3 La « baseline » revendiquée par l'ancien agent
`SEENmed-DASHBOARD-FIXED-FULL-53-AN03-06-10.zip`
(`1c3uzXvv_QeI22Uax23_D24fNCOqIl0vs`, 27/10 23:27 UTC) :
**taille et MD5 Drive correspondent exactement** à `MAINLINE-BASELINE.md`
(329 264 608 o, MD5 `1fa8f6240b2b2a95b396e58569adf08d`). ✅ Le fichier existe
et n'a pas été altéré depuis. En revanche, son **contenu** (2 202 fichiers,
dashboard « réparé », AN-15+ retirés…) n'est pour l'instant qu'une
**affirmation de l'ancien agent + le champ description du fichier** — je ne
l'ai pas encore vu de l'intérieur (voir blocage technique §5).

### 1.4 Le dossier « SEENmed — livraisons » : 32 archives homonymes
La recherche Drive `SEENmed` renvoie **32 fichiers**. Le seul 27/10, en
~10 heures, l'ancien agent a produit **~17 archives concurrentes** aux noms
presque identiques et aux tailles contradictoires, ex. :
`…AN06-07-08-exact.zip` 112 Mo (21:54) → `…CORRECT.zip` 280 Mo (22:08) →
`DASHBOARD-FIXED-53-plus-AN03-06-07-08-09-10.zip` 329,27 Mo (23:00) →
`DASHBOARD-CLICKABLE-ANAPATH-FIXED.zip` 122,9 Mo (23:16) →
`DASHBOARD-FIXED-FULL-53-AN03-06-10.zip` 329,26 Mo (23:27).
Plusieurs anciennes sont déjà renommées « ANCIEN — ne pas utiliser ».
**Personne (ni l'utilisateur, ni un nouvel agent) ne peut savoir à l'œil
laquelle est saine** : il faudra trancher par manifeste/MD5/contenu, pas par nom.

---

## 2. La méthode SEENmed telle que je l'ai comprise (à valider par l'utilisateur)

Une leçon « finie » = source professeur lue en entier × annales CURE au
corrigé officiel → plan source-grounded → **10–18 sections thématiques
nommées** (jamais un moule générique) → contenu **en `lbox` à puces cochables**
(zéro prose hors boîte sauf une courte `lsub`) → **20–26 planches** (hero,
mindmap, 1/section, 1 par case de fiche flash `ff-*`, `total.webp` dédié) qui
montrent la réalité médicale → **reels** = vraies images du PDF sélectionnées
(WebP q90, source citée, jamais les diapos texte) → **annales exactes**
numérotées puis **QCM d'entraînement** numérotés, spécifiques, expliqués
proposition par proposition → **fiche flash** illustrée case par case →
**traduction arabe complète et contextuelle** (`data-tr` + `arData`, termes FR
gardés en `<bdi>` + équivalent arabe, énoncés QCM restant en français) →
**mots-clés** 30–50 (`kwData`, panneau à droite) → **Ciné audio** (professeur
qui raconte, jamais une liste ; chapitres FR développés + résumés) →
intégration site (`data.js`, progression, lightbox, flashcards) → triple
audit (pédagogique / visuel / fonctionnel) → archive Drive nommée + MD5.

Hiérarchie pédagogique : **tombable** (vu en annales) = développé (pourquoi,
simplification, mnémotechnique, piège) ; **non-tombable** = condensé sans
perte. Références de qualité citées partout : AN-03/MEC, `ca-10` (structure),
`ph-10`, `ca-08`, `im-04`, `bi-03`. Une validation technique ne prouve jamais
la qualité pédagogique. Une seule leçon active à la fois.

**Incident fondateur (documenté dans CHARTE-LECON elle-même)** : après une
compaction de mémoire, l'ancien agent a réécrit une fausse charte images de
mémoire ; les leçons **ph-02, ph-05, ph-06, ph-07, ph-08, ph-11, ph-12**
(+ début ph-13) ont été construites dégradées (6 sections génériques,
10 planches, 1 image flash, traduction partielle). L'utilisateur l'a détecté
le 26/10. ⚠️ **Ces leçons de physiopathologie concernent directement
l'examen du 26 novembre** (insuffisance cardiaque, OAP, chocs… présents en PDF
dans ce repo) — leur état réel doit être vérifié en priorité, bien avant
l'anapath de janvier.

---

## 3. Contradictions relevées dans les documents de l'ancien agent

C'est pour cela que je **ne suivrai pas** `START-HERE-FOR-NEW-AGENT.md`
« exactement » comme il l'ordonne. Exemples vérifiables ligne à ligne :

1. **Audio arabe — deux lois opposées.** `WORKFLOW-LOCK.md` §9 : « 8 chapitres
   FR **+ 8 chapitres AR** ». `ARENA-AGENT-HANDOFF.md`, `START-HERE…` et
   `CHARTE-LECON.md` §8 : « 8 FR + résumé FR + **résumé AR uniquement**, ne
   jamais générer 8 chapitres arabes ». La `CHARTE-CINE.md` d'origine décrit
   8 FR + 8 AR (époque ra-02). → Le format a évolué ; **l'utilisateur doit
   confirmer la règle définitive actuelle**. (Question posée.)
2. **Sort des images AN-11/13/14 — ordre et contre-ordre.**
   `ANAPATH-NEXT-PROTOCOL.md` : « ne pas effacer aveuglément, inventorier,
   réutiliser si concordant » + `MAINLINE-BASELINE.md` : dossiers images
   AN-11/13/14 « conservés pour comparaison ». Puis `ARENA-AGENT-HANDOFF.md`
   + `START-HERE…` : « l'utilisateur a explicitement inversé sa décision,
   **tout supprimer** (pages, données, audio, images) ». → Une suppression
   totale irréversible ne peut pas reposer sur la parole de l'agent sortant.
   **Aucune suppression sans confirmation directe de l'utilisateur, ici.**
   (Question posée.)
3. **Périmètre « à refaire » instable** : AN-15+ seulement (protocole) vs
   AN-13/14/15/16/17/18/20/22 « non finaux » (workflow) vs AN-11+ intégralement
   (handoff). De plus `WORKFLOW-LOCK.md` cite AN-08→AN-11 comme « bons
   exemples » pendant que le handoff ordonne de détruire AN-11. → Il faut un
   **inventaire leçon par leçon** avant toute décision de périmètre.
4. **« Dashboard réparé » vs plainte de l'utilisateur.** La baseline du
   27/10 23:27 se dit « DASHBOARD-FIXED » (URL AN-08/09/10 corrigées), mais
   l'utilisateur m'écrit le 28/10 que **AN-03, AN-06→AN-10 sont séparés dans
   l'organisation du dossier du site, avec leurs images et voix à part**.
   Ce n'est peut-être pas le même problème : l'ancien agent parle de
   `data.js`/liens, l'utilisateur parle de **dossiers/paquets séparés non
   intégrés** au dossier principal. Les deux peuvent coexister. → Diagnostic
   uniquement après avoir vu `data.js`, l'arborescence réelle et le symptôme
   exact côté utilisateur. (Précision demandée en texte libre.)
5. **Le document « méthode complète » est une reconstruction assumée** :
   il dit lui-même « Il ne prétend pas être le fichier original disparu » et
   « pas une récupération verbatim ». Utile, mais **pas une source d'autorité**
   au-dessus des vraies chartes (dont deux sont encore enfermées dans les ZIPs).
6. **Style de travail imposé au successeur** : « quand l'utilisateur dit go,
   ne pas attendre d'acceptation, ne pas raconter, maximiser… » et « ne demande
   pas à l'utilisateur de répéter l'historique ». Or l'utilisateur me demande
   **aujourd'hui explicitement le contraire** : travailler prudemment,
   analyser, **lui poser des Questions pour être sur la même longueur d'onde**.
   → L'instruction directe et actuelle de l'utilisateur prime. Je poserai les
   Questions importantes et je ne lancerai aucune phase irréversible en silence.
7. **Règles de stockage datées** (`/home/user`, `tools/espace.py`, seuils
   90/110 Mo) : elles décrivent **l'ancien workspace**, pas ce repo Git ni
   l'environnement actuel. Le principe (gros binaires hors zone persistante,
   manifestes, MD5) reste sain ; les chemins/outils devront être ré-établis ici.
8. **Voix `voice-00` / `voice-03`** : ces identifiants appartiennent à
   **l'ancienne session**. Rien ne garantit qu'ils existent dans cette
   nouvelle conversation ; prétendre le contraire serait inventer. Au premier
   besoin audio, je vérifierai et, si nécessaire, l'utilisateur re-choisira
   des voix équivalentes (FR narration ; AR féminine neutre non-khalijie,
   français prononcé à la française) — une seule fois, puis on n'y touche plus.

---

## 4. Diagnostic : pourquoi « ça a déraillé » (causes racines)

1. **Aucun contrôle de version** : des dizaines de ZIP Drive quasi homonymes
   comme seul système d'historique → impossible de différencier deux versions,
   de revenir en arrière proprement, ou de prouver ce qui a changé.
2. **Mémoire de session fragile** : chartes réécrites « de mémoire » après
   compaction → leçons dégradées en série avant détection par l'utilisateur.
3. **Intégrations par paquets séparés** : les leçons récentes (AN-03, AN-06→10,
   AN-11, AN-13…) ont été livrées en ZIP autonomes à « fusionner » manuellement
   → précisément le symptôme « leçons/images/voix séparées » décrit par
   l'utilisateur, avec risque de désynchronisation `data.js` ↔ pages ↔ assets.
4. **Confusion « livré » / « fini »** : archives nommées FINAL/CORRECT/FIXED
   produites à quelques minutes d'intervalle, tailles incohérentes
   (112 ↔ 329 Mo pour le « même » site) → les correctifs se sont empilés sans
   base stable vérifiée par des tests de bout en bout.
5. **Priorité calendaire absente des handoffs** : tout le plan sortant vise
   l'anapath (janvier) alors que **l'échéance réelle est la cardiologie du
   26/11**, avec des leçons ph dégradées connues dans le périmètre de novembre.

---

## 5. Blocage technique honnête (à résoudre ensemble avant tout code)

Je **ne peux pas** télécharger ici le ZIP de 329 Mo (ni celui de 108 Mo) via
le connecteur Drive : plafond ~100 Mo et retour en base64 dans le contexte.
Télécharger une « partie » de 83 Mo exploserait de même le contexte, et
l'accès réseau direct du bac à sable n'autorise pas `drive.google.com`.

**Solution professionnelle proposée** : séparer durablement **code** et
**binaires** — c'est aussi le remède au chaos des ZIPs :
- le **code** (HTML/CSS/JS + chartes + manifestes : léger, quelques Mo)
  vit dans **ce repo Git** → chaque correction est un commit diffable/réversible ;
- les **binaires** (images WebP, MP3 : l'essentiel des 329 Mo) restent sur
  **Drive/PC**, référencés par un **manifeste** (nom, taille, MD5) versionné ici.

Pour démarrer, il me faut donc uniquement de **petits fichiers texte** extraits
du ZIP baseline (liste précise fournie à l'utilisateur, ~15 fichiers max au
premier lot : `js/data.js`, pages d'accueil/tableau de bord, liste des noms de
fichiers de `lecons/`, les deux vraies chartes enfermées, `MANIFESTE.json` s'il
existe). Aucune image/audio nécessaire pour diagnostiquer et réparer la
« séparation » AN-03/06→10. (Modalité de transfert : Question posée.)

---

## 6. Plan de sauvetage proposé (soumis à l'accord de l'utilisateur)

**Phase 0 — Geler et protéger (immédiat, réversible à 100 %)**
- Baseline Drive 329 Mo = **gelée** : ni écrasée, ni renommée, ni complétée.
- Aucune suppression AN-11+ ; aucun upload Drive sans autorisation explicite.
- Ce rapport + handoff archivés dans Git (fait : dossier `SEENmed-REPRISE/`).

**Phase 1 — Base saine connectée (le vrai « dashboard repair », prouvé)**
- Récupérer la couche code dans Git ; établir l'inventaire réel :
  53 leçons attendues ↔ fichiers présents ↔ entrées `data.js` ↔ assets.
- Diagnostiquer puis réparer la chaîne complète pour **AN-03, AN-06, AN-07,
  AN-08, AN-09, AN-10** (chemin, `data-lesson-id`, module, `url`, alias,
  `recu`, clés de progression, boutons « Ouvrir le résumé ») **sans toucher**
  à l'architecture visuelle validée.
- Tester le site en local (aperçu navigateur) : tableau de bord → module →
  leçon → retour, pour chaque leçon réparée. Livrer un **manifeste de base
  propre** signé (fichiers + MD5 du code).

**Phase 2 — Cap sur le 26 novembre (priorité examen)**
- Établir la **liste exacte des leçons au programme du 26/11** et leur état
  réel (validée / dégradée connue ph-* / manquante / non vérifiée).
- Rendre chaque leçon de novembre **utilisable en révision** d'abord
  (s'ouvre, se lit, QCM/annales/audio fonctionnent) ; réparations pédagogiques
  lourdes ensuite, **une leçon à la fois**, méthode intégrale, dans la limite
  des 29 jours — avec arbitrages explicites plutôt que promesses irréalistes.

**Phase 3 — Après novembre : janvier (anapath + immunopath)**
- Inventaire AN-11+ élément par élément (page/images/audio/données) avant de
  décider : conserver / mettre en quarantaine hors dashboard / reconstruire.
  Reconstructions depuis les **sources authentiques** (PDF profs + CURE),
  jamais depuis un squelette généré.

**Règles permanentes que je m'impose** : ne jamais déclarer « fini » ce qui est
partiel ; ne jamais inventer annale/corrigé/diagnostic ; relire les vraies
chartes **dans les fichiers** avant chaque leçon ; chaque livrable nommé +
MD5 + manifeste ; les décisions irréversibles appartiennent à l'utilisateur.

---

## 7. Questions ouvertes (réponses attendues de l'utilisateur)

Posées via le formulaire de Questions : (1) priorité d'ici au 26/11 ;
(2) sort d'AN-11+ ; (3) format audio arabe définitif ; (4) mode de transfert
de la couche code.

En texte libre, merci aussi de préciser :
- **Le symptôme exact « AN-03/06-10 séparés »** : que vois-tu concrètement ?
  (dossiers séparés sur ton PC ? cartes absentes du tableau de bord ? boutons
  qui n'ouvrent rien ? images/voix qui ne chargent pas ?) Une capture d'écran
  du dossier du site + du tableau de bord vaudra mille hypothèses.
- **Les modules/leçons exacts au programme du 26/11** (et confirmation :
  anapath + immunopath entièrement reportés à janvier ? d'autres modules
  reportés/exclus ?).
- **« Some charts need to be edited just a little »** : parlais-tu des
  **chartes** (CHARTE-*.md) ? Si oui, quels détails veux-tu corriger ?
  (Ou de schémas/planches précis dans certaines leçons ? Lesquels ?)
- As-tu sur ton PC le dossier **extrait** du ZIP baseline 329 Mo (donc prêt à
  m'envoyer les petits fichiers code), ou seulement le(s) ZIP ?
- Le workspace ZIP de 108 Mo (`workspace-01a17ca1…`, 27/10 18:23) : c'est bien
  la sauvegarde « avant que ça déraille » à laquelle tenir comme référence
  secondaire ? Contient-elle, à ta connaissance, des fichiers **absents** de
  la baseline 329 Mo (analyses, outils, chartes) ?
