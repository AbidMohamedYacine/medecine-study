# SEENmed — PROTOCOLE DE COORDINATION 4 AGENTS (v1, 2026-10-29)

> **Complète le HANDOFF** (`HANDOFF-NOUVEL-AGENT.md`, dossier Drive kit `1bHMhdFd94LIgR_GD9vIkv2zMRK-KjFYI`) et **prime sur lui** pour : coordination multi-agents, discipline de quotas, qualité des images v2, `data.js` partagé. Aucun Git. **Drive = seule source de vérité.**
> Dossier de coordination (racine Drive) : `01_COORDINATION-4-AGENTS_2026-10-29` — ID **`1P_NzJcrBQIbUc9r0JjXzmb0Lk-C8XTsA`**.

## 1. Les 4 agents et leurs files (queues)
- **AGENT-1** (chat d'origine) : sg-05 → sg-04 → bi-04 → ph-09, puis aide globale.
- **AGENT-2** (premier agent externe) : **pn-07 (en cours, réservée)** → pn-05 → pn-03 → pn-08 → pn-11.
- **AGENT-3** (nouvel agent) : pn-02 → pn-06 → pn-09 → pn-12 → pn-10.
- **AGENT-4** (nouvel agent) : psy-09 → psy-08 → psy-06.
- Une file **ne vaut pas réservation** : le verrou (LOCK, §3) seul réserve. File terminée → prendre la 1ʳᵉ leçon `LIBRE` du registre par priorité (S > A > B), après le contrôle §2. **ra-05 = BLOQUÉE** (aucune source) : personne n'y touche sans consigne de l'utilisateur.

## 2. Contrôle obligatoire AVANT de toucher une leçon (60 secondes, à chaque reprise)
1. Charge les outils Drive (`list_connector_tools`, chaque tour).
2. Cherche (`google_drive__search_files`) : `name contains '<id-leçon>'` — regarde **livraisons** et **LOCK_**.
3. Lis le **dernier** `REGISTRE-LECONS_*.csv` du dossier coordination.
4. Décision, sans exception :
   - Dossier `*_LIVRAISON-<id>_*` + ZIP + LISEZ-MOI présents → **LIVRÉE : ne jamais refaire** (un patch est une nouvelle livraison delta du seul propriétaire, sur demande de l'utilisateur).
   - Dossier `LOCK_<id>_AGENT-*` présent → **RÉSERVÉE/EN COURS : ne pas toucher**, même sans livraison. Lis le dernier `STATUT_*` pour info, passe à ta file.
   - `BLOQUEE` au registre → passer.
   - Sinon → `LIBRE` : réservable (§3).

## 3. Réserver (CLAIM) — avant tout téléchargement/génération
1. Crée dans le dossier coordination un sous-dossier **`LOCK_<id>_AGENT-<ton numéro>`**.
2. Uploade dedans `STATUT_<AAAA-MM-JJ-HHMM>.txt` (modèle §6) avec étape `RESERVATION`.
3. Re-cherche `<id>` : si un **autre** LOCK plus ancien existe → écris `ABANDON.txt` dans ton LOCK (« doublon, je me retire ») et passe à autre chose. **Ne supprime/modifie jamais le LOCK, le STATUT ou les fichiers d'un autre agent.**

## 4. Pendant le travail (anti-perte, workspaces éphémères)
- À **chaque fin d'étape** (source lue / lot images / page / audio / audit), uploade un nouveau `STATUT_<horodatage>.txt` dans ton LOCK (modèle §6). Le plus récent fait foi.
- Après le build de la page (avant l'audio) et avant toute fin de tour risquée, uploade dans ton LOCK un **`EN-COURS_<id>_<étape>.zip`** (PLAN-SOURCE, builder, scripts audio, page, WebP du jour) : si ton workspace est réinitialisé, tu reprends de là, **jamais de zéro**.
- **Limite d'usage atteinte en plein travail** : arrête-toi, laisse un dernier STATUT précis (fait / reste / générations déjà consommées). Les autres agents **sautent** ta leçon indéfiniment ; seul l'utilisateur peut réassigner (le repreneur crée alors son LOCK en référençant l'ancien et repart des `EN-COURS`).

## 5. Terminer et livrer (séquence de fermeture, dans l'ordre)
1. Numéro de livraison = **max existant + 1** (cherche `name contains 'LIVRAISON-'` ; dernier connu : 05 → prochain **06**), dossier **à la RACINE Drive** (jamais imbriqué dans une autre livraison) nommé `NN_LIVRAISON-<id>_<AAAA-MM-JJ>`.
2. ZIP delta avec dossier racine **`medstudy/`** obligatoire : `medstudy/{lecons/<page>.html, js/data.js, assets/img/<id>/**, assets/audio/<id>/**}` + `LISEZ-MOI-<id>.txt` (« dézippe dans le dossier qui CONTIENT medstudy, accepte la fusion » + contenu + MD5) + `ARTEFACTS-<id>.zip` (PLAN-SOURCE, builder, scripts, page, data final, WebP).
3. Vérifie les **tailles** retournées par Drive == locales.
4. Uploade dans ton LOCK un `TERMINE.txt` (dossier livraison ID, ZIP ID, MD5, tailles).
5. Uploade dans le dossier coordination le nouveau registre **`REGISTRE-LECONS_<AAAA-MM-JJ-HHMM>.csv`** (copie du dernier + ta ligne mise à `LIVREE`) **et** ton **`data_COURANT_<AAAA-MM-JJ>_<id>.js`** (§7). Ne supprime jamais les anciennes versions.

## 6. Modèle STATUT (à copier tel quel)
```
LECON: <id> — <titre>
AGENT: AGENT-<n>
ETAPE: RESERVATION | SOURCE_LUE | IMAGES_LOT1 | IMAGES_LOT2 | PAGE_CONSTRUITE | AUDIO | AUDIT_OK | LIVRAISON_EN_COURS | TERMINE | BLOQUE_LIMITE
DATE_HEURE: <AAAA-MM-JJ HH:MM>
SOURCE: <fichier, ID Drive, MD5, pages>
FAIT: <liste courte>
RESTE: <liste courte et exacte>
GENERATIONS (cumul leçon): images OK <n> / échecs <n> ; audios OK <n> / échecs <n>
GENERATIONS (ce tour): images <n>/10 ; audios <n>/10
FICHIERS: <EN-COURS zip / dossier livraison / IDs>
```

## 7. `data.js` partagé — LA règle anti-écrasement
Quatre agents qui patchent chacun leur copie locale peuvent **régresser** les activations des autres. Donc :
1. Avant de patcher, télécharge le **`data_COURANT_*` le plus récent** du dossier coordination et pars de LUI (jamais d'un vieux data.js local). Semence actuelle : `data_COURANT_2026-10-29_apres-pn04.js` (bi-05, bi-06, pn-01, pn-04 actifs — vérifié).
2. Ne modifie **que la ligne de ta leçon** (format §4.2 du HANDOFF).
3. Contrôle avant livraison : ton `data.js` doit contenir `recu: true` + `url` pour **toutes** les leçons `LIVREE` du dernier registre **plus** la tienne. Sinon : ne livre pas, rebase sur le dernier `data_COURANT`.

## 8. Discipline de génération — LES ÉCHECS BRÛLENT DU QUOTA (ne négocie pas)
- Caps durs par **message de l'utilisateur** : **10 images, 10 audios**. Les appels **échoués ou refusés comptent** (429, cap, texte trop long) et consomment de l'usage journalier. Vécu : 10 images réussies + un 2ᵉ bloc de 10 dans le même message = 10 appels brûlés pour rien.
- **Règle du bloc unique compté** : avant d'envoyer, liste numérotée des appels (1..N ≤ 10), relue ; envoie **un seul bloc** ; après 10 tentatives (succès ou non), **zéro nouvel appel de génération dans ce message**, même si tout a réussi. Aucun retry dans le même tour après un échec de cap/429 : note-le au STATUT, ce sera le prochain GO.
- Audio : **compte les caractères avant** (cible ≤ 1400, max absolu 1500).
- Avant de générer quoi que ce soit, vérifie que le fichier n'existe pas déjà (site reconstruit, `EN-COURS`, livraisons). **Existant = on ne régénère pas.**
- Note tes compteurs dans chaque STATUT (§6) : les autres agents et l'utilisateur doivent voir ce qui a été consommé.

## 9. QUALITÉ IMAGE v2 (retour utilisateur — s'applique à toute nouvelle planche)
Les planches génériques sur fond blanc vide sont **refusées**. Chaque planche est un **outil d'apprentissage dense et exact** :
1. **Contrat de planche** (écrit dans le PLAN-SOURCE AVANT le prompt) : QUESTION (ce que l'étudiant doit comprendre) · OÙ (organe/tissu/lieu anatomique ou scène clinique) · À QUOI ÇA RESSEMBLE (morphologie, coupe, échelle) · COMMENT ÇA MARCHE (mécanisme en étapes numérotées/flèches) · CONNEXIONS (liens entre structures/systèmes, flèches étiquetées) · RÉACTION/EFFET (conséquences) · SÉQUENCE/TEMPS (axe, avant/après) · COMPARAISON (normal vs pathologique si pertinent) · TEXTE EXACT (titres + chiffres + étiquettes, mot pour mot) · INTERDITS (aucune valeur inventée, aucun texte parasite).
2. **Fond contextualisé, jamais vide** : environnement tissulaire/organique, scène de laboratoire/urgences, profondeur et matière — au service du contenu, sans nuire à la lisibilité. Seule exception : la zone de tracé d'un graphique peut rester claire, mais intégrée dans une composition contextualisée (panneau, scène, vignettes).
3. **Grammaire visuelle** : titre FR impeccable, structure focale grande, cartouches avec lignes de rappel, inset/zoom, codes couleur constants dans la leçon, légende si symboles, flèches de flux/causalité, repères chiffrés exacts.
4. **Plusieurs planches par section quand il faut** : si une section contient anatomie + mécanisme, ou une cascade, un algorithme, une comparaison (> 5 faits clés) → **2 planches** (A : où/à quoi ça ressemble ; B : comment ça marche/ça réagit). Mieux vaut 2 planches justes qu'1 illisible. Ajuste le plan d'images et les slots (§8) en conséquence — la quantité cible (~21-23) peut monter, jamais au prix d'un dépassement de cap.
5. **Contrôle qualité sans pitié** : planche-contact + **zoom pleine taille sur toute planche avec texte/chiffres**. Rejet si : orthographe/chiffre faux ou inventé, flèche dans le mauvais sens, structure absente ou surnuméraire, fond vide, contenu qui ne couvre pas le contrat. Rejetée = régénération au prochain GO avec prompt enrichi, marquée `PROVISOIRE` au STATUT — **jamais livrée en l'état**.
6. Les leçons déjà livrées (bi-05, bi-06, pn-01, pn-04) ne sont **pas** reconstruites pour la v2 sans demande explicite de l'utilisateur (un upgrade d'images = nouveau delta du propriétaire).

## 10. Communication avec l'utilisateur (format court, à chaque tour)
```
[<id>] ÉTAPE: <où j'en suis> · FAIT: <...> · RESTE: <...> · QUOTA CE TOUR: img <n>/10, audio <n>/10
```
3 lignes max hors livraison. Jamais « fini » pour du partiel.

## 11. Reconstruction du site pour un nouvel agent (rappel — détail HANDOFF §1.5)
Base `00_BASE-OFFICIELLE_2026-10-28` (4 parties) → deltas dans l'ordre : **01** (bi-05 images/audio seulement), **02** (bi-06 + page bi-05 corrigée), **03** (2 planches bi-06 finales), **04 pn-01**, **05 pn-04**, puis **`js/data.js` := dernier `data_COURANT_*`** du dossier coordination. Audit attendu : **63 pages**, unreachable NONE, 11 refs an-06. (pn-01/pn-04 : leurs ZIP sont **sans** préfixe `medstudy/` — dézipper DANS `medstudy/`.)
