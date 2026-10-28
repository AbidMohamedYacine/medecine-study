# SEENmed — Diagnostic prouvé et réparation de la base (28/10/2026)

> Suite de `00-AUDIT-NEUTRE-2026-10-28.md`. Tout ce qui suit a été **vérifié
> sur les fichiers eux-mêmes** (4 parties Drive téléchargées, MD5 contrôlés,
> extraction en `/tmp`, audits automatisés, test HTTP réel). Décisions
> appliquées : voir `DECISIONS-UTILISATEUR-2026-10-28.md`.
> **Aucun fichier Drive n'a été modifié ni effacé. Aucun envoi Drive effectué.**

---

## 1. Récupération des 4 parties — intégrité prouvée

| Partie | Taille (o) | MD5 Drive = MD5 local |
|---|---|---|
| part1-of4 | 83 872 343 | `c74f1cdb3ef8f16eddaf18e74ca3284d` ✅ |
| part2-of4 | 83 416 172 | `0c1077944701f9da6ac32c141d307c4c` ✅ |
| part3-of4 | 83 861 192 | `2165fa1671678a76591a047abddff2dc` ✅ |
| part4-of4 | 77 994 131 | `94c446dfc0c873b60729370325aec3a9` ✅ |

Entrées : 489 + 206 + 733 + 774 = **2 202**, soit exactement l'inventaire
annoncé de la baseline `SEENmed-DASHBOARD-FIXED-FULL-53-AN03-06-10.zip`
(manifeste complet : `manifeste-inventaire-baseline-2202.json`).
Les 4 parties sont le **découpage par fichiers de cette même baseline**.

## 2. Le bug « AN-03 / AN-06→10 séparés » — cause racine double, prouvée

### 2a. Séparation physique dans l'archive (ce que l'utilisateur voyait)
Sur 2 202 entrées, **484 sont hors du dossier `medstudy/`** :
- 6 pages : `lecons/an-03…`, `an-06…`, `an-07…`, `an-08…`, `an-09…`, `an-10…`
- 420 images `assets/img/an-{03,06,07,08,09,10,11,13,14}/…`
- 58 audios `assets/audio/an-{03,06,07,08,09,10}/…`

Or chaque page référence `../css`, `../js`, `../assets`, `../index.html`.
Placée dans `lecons/` à la racine, elle cherche ces dossiers **à côté** de
`lecons/` — où ils n'existent pas : audit des références dans l'état d'origine
= **17 à 28 références cassées par page** (CSS/JS/fonts introuvables), page
inutilisable dès l'extraction. C'est un défaut de **fabrication de
l'archive** (fusion à deux racines), pas une erreur de l'utilisateur.

### 2b. Séparation logique dans `data.js` (ce que le tableau de bord montrait)
Malgré le nom « DASHBOARD-FIXED » et la description Drive (« URLs corrigées
pour AN-08/09/10 »), le `data.js` réel de la baseline contient, pour
**an-03, an-06, an-07, an-08, an-09, an-10** : `qcm: 0, recu: false`
**et aucune `url`**. Conséquence mécanique (`dashboard.js` l.29-31) : pas de
bouton « Ouvrir le résumé », statut « À venir ». **L'affirmation
« dashboard réparé » de l'ancien agent est fausse sur pièces.**
Même défaut, passé inaperçu, pour **ra-06** (page présente, `recu: true`,
`qcm: 15`, mais pas d'`url`). Total : **7 pages construites et
inatteignables** ; 0 URL pointant vers un fichier absent.

## 3. Réparation réalisée (base propre, racine unique `medstudy/`)

1. Pages AN-03, AN-06→10 déplacées → `medstudy/lecons/` ; images et audios
   correspondants → `medstudy/assets/img|audio/` (zéro collision vérifiée).
2. `data.js` corrigé (diff complet versionné dans `base-propre-2026-10-28/`) :
   `url` + `recu: true` pour les 6 leçons, `url` pour ra-06, compteurs QCM
   **comptés dans les pages mêmes** (annales/entraînement) :

   | Leçon | Annales | Entraînement | Audio | Images |
   |---|---|---|---|---|
   | an-03 MEC | 11 | 15 | 9 pistes | 43 |
   | an-06 Métabolisme | 2 | 20 | 9 | 51 (+11 manquantes, §5) |
   | an-07 Immunopathologie | 6 | 20 | 10 | 77 |
   | an-08 Réparation | 15 | 20 | 10 | 43 |
   | an-09 Formes inflammation | 13 | 20 | 10 | 86 |
   | an-10 Étiologie cancer | 6 | 20 | 10 | 22 |
3. **AN-11+ retirés de la base de travail** (décision utilisateur) :
   4 entrées `data.js` (an-11→14) supprimées, **98 fichiers images
   (11 212 442 o) exclus** — détail CRC/tailles dans
   `manifeste-suppressions-AN11plus.json`. Les originaux restent intacts
   dans les archives Drive : restauration possible à tout moment.
4. Aucun contenu pédagogique, aucun visuel, aucune architecture modifiés.

## 4. Validation (preuves, pas promesses)

- Audit automatisé complet (`tools/audit_seenmed.py`, réutilisable) :
  URLs→fichiers manquants **0** · pages inatteignables **0** ·
  `data-lesson-id` discordants **0** · références locales cassées :
  **11 au total, toutes dans AN-06** (§5), 0 sur les 58 autres pages.
- `MED_DATA.totalDispo()` : **52 → 59 résumés ouvrables**.
- Test HTTP réel (serveur local, apercu navigateur actif) : `/`, progression,
  les 6 pages AN, ra-06, images et MP3 → **200** ; seul
  `assets/img/an-06/ff-1.webp` → 404 (défaut connu §5).
- Archive propre fabriquée en `/tmp` (racine unique `medstudy/`) :
  **`SEENmed-BASE-PROPRE-2026-10-28_AN03-06-10-RA06_SANS-AN11PLUS.zip`**
  — 2 104 fichiers · 318 049 357 o · MD5
  **`e4f0448d3f5b8ca4f06e99328dbe99cc`** · `testzip` OK.
  **Non téléversée** (autorisation Drive non encore donnée).

## 5. Défaut résiduel unique : 11 images d'AN-06 jamais livrées

`ff-1…ff-6.webp`, `mindmap.webp`, `n-atherome.webp`, `n-goutte.webp`,
`n-protides.webp`, `resume-total.webp` sont référencées par la page
(dont `cineData`) mais **absentes de toutes les archives vérifiées** :
baseline 4 parties, `SEENmed-ANAPATH-AN01-AN11-…-v2-with-audio.zip`
(MD5 `09267f65…`), `SEENmed-decharge-2026-10-27-img-audio-12-lecons.zip`
(MD5 `c355c6b1…`). Elles n'ont donc jamais été livrées. À régénérer selon
la vraie `CHARTE-IMAGES.md` — module de **janvier**, non bloquant pour
novembre. AN-06 reste entièrement lisible (texte, QCM, arabe, audio).

## 6. État réel par module après réparation (pages ouvrables / programme)

| Module | Ouvrables | Manquantes au programme |
|---|---|---|
| Psychologie (psy) | 6/9 | psy-06, psy-08, psy-09 |
| Sémiologie Générale (sg) | 4/6 | sg-04, sg-05 |
| **Cardiologie (ca)** | **11/11** | — |
| **Pneumologie (pn)** | **0/12** ⚠️ | pn-01 → pn-12 |
| Physiopathologie (ph) | 12/13 | ph-09 (HTA) |
| Biochimie (bi) | 4/7 | bi-04, bi-05, **bi-06 biomarqueurs cardiaques** |
| Radiologie (ra) | 6/7 | ra-05 (radioanatomie du cœur, 17 QCM annales) |
| Anapath (an) — *janvier* | 10/10 | suite à reconstruire (décision §3) |
| Immuno (im) — *janvier* | 7/17 | im-06, im-09 → im-17 |

### ⚠️ Alerte calendrier (J-29 avant le 26/11)
Si l'unité du 26/11 est bien « Cardio-Respiratoire » au complet, le trou
majeur n'est pas l'anapath : c'est **la pneumologie à 0/12**, devant
bi-06, ra-05 et ph-09. **Le programme exact de l'examen doit être confirmé
par l'utilisateur avant tout plan de production** — c'est la seule
information que les fichiers ne peuvent pas fournir.

### Générations de leçons (métriques : `metriques-59-lecons.json`)
- Leçons « nouvelle génération » (arabe `arData` + mots-clés + Ciné audio) :
  an-03/05/06/07/08/09/10, ca-02/03/04/05/06/10/11, ph-02/05/06/07/08/11/12/13,
  ra-02/04/06, im-05/08. Ex. an-07 : 26 sections, 96 `lbox`, 107 `data-tr`.
- Leçons antérieures (FR seul, sans audio) : ca-01/07/08/09, ph-01/03/04/10,
  bi-*, ra-01/03/07, sg-*, psy-*, im-01→04/07, an-01/02/04 — **utilisables
  en révision**, mais hors méthode complète actuelle.
- L'ancien étiquetage « ph-02/05/06/07/08/11/12 dégradées » (26/10) **ne
  correspond plus aux métriques actuelles** (ph-02 : 24 sections/64 lbox ;
  ph-06 : 23/64) : une réparation a manifestement eu lieu ensuite. Cela ne
  vaut **pas** validation pédagogique — un contrôle visuel/contenu reste
  à faire leçon par leçon avant de les déclarer « validées ».

## 7. Chartes récupérées et mises à l'abri

Dans `chartes-recuperees/` : la **vraie `CHARTE-IMAGES.md` (14 Ko)** et
**`CHARTE-IMMUNO.md` (22 Ko)**, extraites de `medstudy/assets/img/`.
⚠️ Le fichier `medstudy/CHARTE-IMAGES.md` (877 o) reste un **panneau
d'avertissement** : ne jamais le prendre pour la charte. Les « petites
corrections de chartes » évoquées par l'utilisateur restent à préciser.

## 8. Règles de travail désormais verrouillées

Code et documents légers → **Git (ce repo)** ; archives complètes →
**Drive uniquement**, racine unique `medstudy/`, nom daté + MD5 + manifeste ;
grosses manipulations → **`/tmp`**, jamais dans l'espace sauvegardé ;
chaque livraison passe `tools/audit_seenmed.py` à **0 référence cassée**
(hors défauts explicitement documentés) avant d'être annoncée ;
une seule leçon active à la fois, chartes **relues dans les fichiers**
avant production ; voix : les identifiants `voice-00/03` appartenaient à
l'ancienne session — à revalider au premier lot audio (sans ré-audition
inutile si les voix équivalentes sont confirmées par l'utilisateur).

## 9. Prochaines étapes proposées (dans l'ordre)

1. Utilisateur : confirmer le **programme exact du 26/11** (pneumo incluse ?)
   et autoriser (ou non) l'**envoi Drive** du ZIP propre ci-dessus.
2. Envoi Drive vérifié (taille + MD5 relus côté Drive), baseline d'origine
   conservée intacte à côté.
3. Plan novembre chiffré sur les manques réels (§6), une leçon à la fois,
   méthode intégrale, en commençant par le plus tombable.
4. Après le 26/11 : phase janvier — régénération des 11 images AN-06,
   reconstruction AN-11+ et Immuno depuis les sources authentiques.
