# SEENmed — PROTOCOLE ÉQUIPE DYNAMIQUE v2 (2026-10-30)

> **Ce protocole remplace les files fixes du v1.** Il complète le HANDOFF et prime sur lui pour : choix des leçons, coordination entre agents, nouvelles leçons, exclusions, `data.js`/progression et diffusion des nouvelles. Les règles techniques du HANDOFF et du v1 (recette de leçon, quotas, qualité image v2, livraison) restent valables.
>
> **Principe : un cerveau Drive, quatre mains.** Aucun agent ne possède une file obligatoire. L'utilisateur peut donner n'importe quelle leçon à n'importe quel agent. La sécurité vient de la synchronisation + des verrous + des preuves Drive, pas d'une répartition figée.

## 0. Adresses de l'équipe
- Coordination : `01_COORDINATION-4-AGENTS_2026-10-29` — ID `1P_NzJcrBQIbUc9r0JjXzmb0Lk-C8XTsA`
- Journal d'événements : sous-dossier `JOURNAL` — ID `1Z-m3YbXzF8ErEQZUS3d6zdW0D5UCrg3E`
- Sources reçues hors cartographie : sous-dossier `INBOX-SOURCES` — ID `1uvGclplmey2ug8CIYUUX-I4SI89O_AvY`
- Kit/méthode : `00_KIT-NOUVEL-AGENT_2026-10-29` — ID `1bHMhdFd94LIgR_GD9vIkv2zMRK-KjFYI`
- Verrou existant pn-07 / AGENT-2 : `1mtjxyqRrSoirVJvXdpiu9FvDNk6hvHPF`

## 1. Ordre de vérité en cas de désaccord
1. **Preuve de livraison Drive** : dossier `*_LIVRAISON-<id>_*` + ZIP + LISEZ-MOI.
2. **LOCK + dernier STATUT** de la leçon.
3. **Dernier REGISTRE** daté/horodaté.
4. **Événements JOURNAL** postérieurs au registre.
5. **Dernier data_COURANT**.
6. Mémoire d'un chat ou ancien plan : **jamais autoritaire**.

Conséquence : si le registre dit « libre » mais qu'une livraison ou un LOCK existe, la livraison/le LOCK gagnent. Si deux informations se contredisent sans preuve supérieure, statut `A_VERIFIER` : ne construis pas, publie un événement et demande une consigne courte.

## 2. SYNC-60 au début de chaque session/tour de travail
Avant de construire, patcher ou répondre sur l'état global :
1. Charge les outils Drive.
2. Lis le dernier `REGISTRE-LECONS_*` du dossier coordination.
3. Liste les fichiers du `JOURNAL` postérieurs à ce registre et lis ceux qui concernent : ta leçon, les exclusions, les nouvelles leçons, les priorités, `data.js`.
4. Cherche sur tout Drive : `name contains '<id-leçon>'` pour la leçon visée ; vérifie livraison et `LOCK_`.
5. Si tu vas toucher `data.js`, identifie le dernier `data_COURANT_*`.
6. Si l'utilisateur vient de te donner une information qui change le périmètre/statut/priorité/source/méthode : **publie-la d'abord dans le JOURNAL (§8), puis agis**. Un chat ne transmet rien aux autres ; Drive est la mémoire partagée.

## 3. Choix dynamique d'une leçon — aucune file stricte
Ordre de décision :
1. **Leçon explicitement donnée par l'utilisateur** dans ce chat (titre, source jointe, lien, fichier Git/Drive) → candidate prioritaire, après contrôle d'état.
2. Si l'utilisateur dit seulement « GO » → première leçon `A_FAIRE` de plus haute priorité dans le registre (d'abord `URGENTE`, puis S, A, B), non verrouillée, non exclue, sourcée.
3. Continuité de module = simple départage d'égalité, jamais une obligation.
4. **Un seul chantier actif par agent.** Si l'utilisateur te donne une autre leçon pendant un chantier : checkpoint + STATUT `EN_PAUSE_UTILISATEUR` sur l'actuelle, événement JOURNAL, puis nouveau verrou. Ne mélange pas deux builds dans un même tour sauf demande explicite.
5. Si la leçon demandée est `LIVREE` → ne refais rien ; réponds avec dossier/ZIP de preuve. Si elle est verrouillée par un autre → ne la touche pas ; réponds propriétaire + dernière étape. Si elle est `NE_PAS_FAIRE`/`BLOQUEE` → rappelle la décision/la cause en 1 ligne ; seul un nouvel ordre explicite de l'utilisateur peut la rouvrir (publie l'événement de réouverture).

## 4. Verrouillage (anti-doublon)
Avant téléchargement de source, génération ou écriture :
1. SYNC-60 (§2) sur l'id exact **et** sur le titre probable si l'id est incertain.
2. Crée `LOCK_<id>_AGENT-<n>` à la racine du dossier coordination.
3. Uploade immédiatement `STATUT_<AAAA-MM-JJ-HHMM>_RESERVATION.txt` (§9).
4. Re-cherche l'id : en cas de deux LOCK, **le plus ancien gagne** ; le second dépose `ABANDON.txt` dans son propre LOCK et s'abstient. Ne supprime/modifie jamais les fichiers d'un autre agent.
5. Aucun verrou n'expire automatiquement. Si un chat/compte disparaît, seul l'utilisateur peut réassigner : le repreneur publie un événement `TRANSFERT`, crée son LOCK, référence l'ancien et repart uniquement des checkpoints Drive/artefacts existants.
6. Un chat de remplacement reçoit un **nouveau numéro d'agent**, sauf si l'utilisateur dit explicitement qu'il hérite du numéro et des verrous.

## 5. États officiels
- `A_CLASSER` : leçon/source nouvelle pas encore identifiée de façon sûre.
- `A_FAIRE` : dans le périmètre, libre.
- `RESERVEE` / `EN_COURS` / `EN_PAUSE_LIMITE` / `EN_PAUSE_UTILISATEUR` : propriétaire unique via LOCK.
- `LIVREE` : preuve Drive complète.
- `A_PATCHER` : livrée, mais correction ou source N demandée ; nouveau delta du propriétaire (ou transfert explicite), jamais reconstruction.
- `BLOQUEE_SOURCE` : source absente/illisible ; cause obligatoire.
- `NE_PAS_FAIRE` : décision utilisateur ; motif + date obligatoires.
- `A_VERIFIER` : contradiction entre preuves ; aucun travail tant que non tranchée.

## 6. Une source arrive par chat, Git, lien ou Drive
L'agent qui la reçoit est responsable de la rendre visible à l'équipe **avant** de construire :
1. Identifie-la : titre, module, enseignant/année si lisibles, nombre de pages/diapos, taille, MD5.
2. Si le fichier est accessible dans ton workspace : uploade une copie dans `INBOX-SOURCES/<id-provisoire-ou-id>/` (ou dans ton LOCK si déjà classée). Si seul un lien/chemin Git est accessible : uploade `SOURCE.txt` avec lien/chemin exact + empreinte ; ne prétends jamais que l'équipe possède un fichier qu'elle n'a pas.
3. Cherche les doublons par **id, titre et thèmes** dans `data_COURANT`, livraisons et LOCKS.
4. Classe-la dans un seul cas :
   - **Stub existant** → garde l'id existant.
   - **Nouvelle version N d'une leçon existante/livrée** → même id, `A_PATCHER` si déjà livrée ; patch différentiel uniquement.
   - **Même page pour deux modules** → une entrée canonique + une entrée avec `alias` (§7).
   - **Vraie nouvelle leçon** → §7.
5. Publie `EVT_..._SOURCE_RECUE` ou `..._NOUVELLE_LECON`, mets à jour le registre, puis verrouille si l'utilisateur te l'assigne.

## 7. Nouvelle leçon + tableau + progression (à ne jamais oublier)
`data.js` pilote le tableau de bord et la progression : les totaux sont calculés depuis `modules[].lecons[]`; une entrée avec `url` compte comme disponible ; `alias` donne l'identifiant de progression partagé et évite le double comptage (`refId`/`totalDispo`).
1. **Identifiant** : prochain numéro libre du préfixe de module dans le dernier `data_COURANT`. **Ne réutilise jamais un id, ne renumérote jamais les anciennes leçons** (progression locale de l'utilisateur indexée par id). L'ordre pédagogique dans le tableau peut différer de l'ordre numérique : insère l'entrée à la bonne place dans le module sans changer les autres ids.
2. **Entrée provisoire immédiate** dans un nouveau `data_COURANT` : `{ id: '<nouvel-id>', nom: '<titre exact>', qcm: <nombre d'annales vérifié ou 0>, recu: <true seulement si le cours est effectivement reçu/source fournie> }`, sans `entr` ni `url` tant que la page n'existe pas. Si le même contenu doit apparaître dans un 2ᵉ module : 2ᵉ entrée avec nouvel id d'affichage, `alias: '<id-canonique>'`, même future `url`.
3. **Notification équipe + utilisateur** : événement `NOUVELLE_LECON` (id, titre, module, source, annales trouvées ou « à cartographier ») + ligne au registre + réponse courte à l'utilisateur. Les autres agents la découvriront à leur SYNC-60.
4. Si la leçon n'est pas livrée dans la même session et que l'utilisateur veut déjà la voir dans le site : micro-livraison numérotée `NN_DELTA-TABLEAU_<date>` contenant uniquement `medstudy/js/data.js` (+ HTML ci-dessous si nécessaire). Sinon, l'entrée complète partira avec la livraison de la leçon.
5. **À la livraison** : complète la même entrée (`entr: 20`, `recu: true` si applicable, `url`), republie `data_COURANT`, puis contrôle progression (§10).
6. **Annales** : `qcm` = nombre réel vérifié dans ELITE/autre recueil fourni. Si la nouvelle leçon n'y figure pas : `qcm: 0`, aucun QCM présenté comme annale ; entraînement clairement séparé. Si des annales sont retrouvées ensuite : événement + mise à jour `qcm`/page par patch du propriétaire.

## 8. Journal d'équipe — parler une fois, informer tout le monde
Chaque information donnée par l'utilisateur à **un seul** agent mais utile aux autres doit devenir un événement immutable dans `JOURNAL` :
`EVT_<AAAA-MM-JJ-HHMM>_AGENT-<n>_<TYPE>_<id-ou-GLOBAL>.txt`

Types minimum : `DECISION`, `NOUVELLE_LECON`, `SOURCE_RECUE`, `EXCLUSION`, `REOUVERTURE`, `PRIORITE`, `TRANSFERT`, `LIVRAISON`, `BLOCAGE`, `METHODE`.
Contenu : date/heure, agent émetteur, leçon/module, fait exact (reprendre les mots/décision de l'utilisateur sans les déformer), conséquence sur le registre/data, fichiers/IDs concernés, action attendue.
Après un événement qui change l'état, publie aussi un **nouveau registre complet horodaté**. Ne modifie ni ne supprime les événements/registres des autres ; les corrections se font par un événement plus récent.

## 9. STATUT et checkpoints (modèle obligatoire)
Dans ton LOCK, à la réservation, à chaque fin d'étape, avant une pause et à la fermeture : `STATUT_<AAAA-MM-JJ-HHMM>_<ETAPE>.txt`
```
LECON: <id> — <titre>
AGENT: AGENT-<n>
ETAPE: RESERVATION | SOURCE_LUE | IMAGES_LOT1 | IMAGES_LOT2 | PAGE_CONSTRUITE | AUDIO | AUDIT_OK | LIVRAISON_EN_COURS | TERMINE | EN_PAUSE_LIMITE | EN_PAUSE_UTILISATEUR | A_PATCHER
DATE_HEURE: <AAAA-MM-JJ HH:MM>
SOURCE: <fichier, ID/chemin, MD5, pages>
FAIT: <court, vérifiable>
RESTE: <exact>
GENERATIONS CUMUL LECON: images OK <n> / échecs <n> ; audios OK <n> / échecs <n>
GENERATIONS CE TOUR: images <n>/10 ; audios <n>/10
DATA: <data_COURANT de départ / publié, ou "non touché">
FICHIERS: <IDs LOCK, EN-COURS, livraison>
```
Après le build de page et avant tout arrêt risqué : `EN-COURS_<id>_<étape>.zip` dans le LOCK (PLAN-SOURCE, builder, scripts uploadés avant génération audio, page, WebP). Une limite atteinte ne doit jamais transformer un chantier en mystère.

## 10. `data.js`, tableau et progression — transaction en 5 temps
1. Télécharge le dernier `data_COURANT` et note son nom dans le STATUT. Ne pars jamais d'une copie locale ancienne ; si ton chantier avait déjà une modification non publiée, réapplique **uniquement ta ligne** sur le dernier fichier.
2. Patch minimal : ta ligne (ou l'ajout d'une nouvelle leçon/alias). Aucun reformatage massif.
3. Juste avant upload, re-liste les `data_COURANT` : si un plus récent est apparu, reprends-le et réapplique ta ligne.
4. Vérifie : ids uniques ; alias pointant sur un id canonique existant ; chaque leçon `LIVREE` du registre/événements récents a `url` ; aucune `url` vers une page absente de la base + deltas ; totaux attendus (`totalDispo` +1 seulement pour une nouvelle page unique, +0 pour un alias).
5. Uploade `data_COURANT_<AAAA-MM-JJ-HHMM>_<id>.js`, puis re-liste une dernière fois ; en cas de course, publie immédiatement une version fusionnée et un événement `DATA`.
6. **QA progression** : la nouvelle entrée apparaît dans le bon module du tableau ; après ajout de `url`, les compteurs module/site augmentent correctement ; le bouton/état de progression utilise `refId` (alias partagé, pas de double). Si un compteur ou une liste est codé en dur dans `index.html`/`progression.html` (à vérifier dans la base reconstruite, ne pas supposer), patche ces fichiers et inclus-les dans le même delta.

## 11. Leçons à ne pas faire / à rouvrir
- Quand l'utilisateur exclut une leçon : événement `EXCLUSION` + registre `NE_PAS_FAIRE` (motif/date). Si elle est en cours, le propriétaire s'arrête à son prochain SYNC, dépose un STATUT d'abandon et conserve les checkpoints.
- Exclure du **chantier** ne signifie pas supprimer du site. L'entrée `data.js` reste visible sauf si l'utilisateur demande explicitement de la retirer/masquer ; dans ce cas : événement séparé, transaction data (§10), micro-delta et QA progression (les anciens états locaux peuvent rester orphelins, ne réutilise pas l'id).
- Une réouverture suit le même chemin inverse (`REOUVERTURE` → `A_FAIRE` ou assignation directe).

## 12. Fin de chantier et livraison (rappel v1, toujours en vigueur)
- Dossier numéroté **à la racine Drive**, numéro = max des `*_LIVRAISON-*` et `*_DELTA-*` numérotés + 1, revérifié juste avant création. En cas de collision simultanée, le dossier créé en premier garde le numéro ; l'autre prend le suivant avant tout upload et le signale par événement.
- ZIP avec racine `medstudy/` + LISEZ-MOI + `ARTEFACTS-<id>.zip` ; tailles vérifiées ; audit officiel 0 hors 11 refs an-06 ; `TERMINE.txt` dans le LOCK ; événement `LIVRAISON` ; nouveau registre ; nouveau `data_COURANT`.
- La leçon n'est `LIVREE` qu'après preuves complètes. Si la limite coupe entre ZIP et fermeture, la preuve ZIP suffit à interdire tout redoublement ; le propriétaire ferme administrativement à sa reprise.

## 13. Quotas et images v2 (inchangés, non négociables)
HANDOFF §6/§7/§11 + PROTOCOLE v1 §8/§9 s'appliquent intégralement : **10 images / 10 audios max par message utilisateur, tentatives échouées incluses**, un seul bloc compté, aucun second bloc dans le même message, compteurs au STATUT ; **contrat de planche**, fond contextualisé jamais blanc vide, plusieurs planches si la section l'exige, zooms de contrôle, rejet de toute erreur de texte/chiffre/sens.

## 14. Réponse type à l'utilisateur (3 lignes)
```
[SYNC] Registre du <date/heure> + <n> événement(s) lu(s). [<id>] <état/propriétaire>.
[FAIT/RESTE] <...> · Quota ce tour : img <n>/10, audio <n>/10.
[PREUVE] <LOCK / livraison / fichier publié>.
```
Répondre à une question d'état global exige le même SYNC : un agent peut donc informer sur le travail des trois autres sans les avoir « entendus ».

## 15. Baseline au 2026-10-30
- Livrées : bi-05, bi-06 (AGENT-1) ; pn-01, pn-04 (AGENT-2). Base reconstruite + deltas 01→05 + dernier `data_COURANT` = **63 pages**, audit 11 refs an-06.
- Réservée/en cours : **pn-07 — AGENT-2** (LOCK ci-dessus).
- Bloquée : ra-05 (aucune source).
- Toutes les autres lignes du registre : `A_FAIRE`, **sans propriétaire ni file imposée** ; priorités S/A/B conservées comme aide au choix dynamique.
