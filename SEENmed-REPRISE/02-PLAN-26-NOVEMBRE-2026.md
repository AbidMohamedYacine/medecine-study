# Plan 26 novembre 2026 — Unité Cardio-Respiratoire (J-29 au 28/10)

**Programme confirmé par l'utilisateur le 28/10/2026** : examen le
**26/11/2026** incluant la **pneumologie** ; seuls **Anapath et
Immunologie** sont reportés (fin janvier). Modules de novembre :
Psychologie, Sémiologie Générale, Cardiologie, Pneumologie,
Physiopathologie, Biochimie, Radiologie.

## État de départ (base propre vérifiée du 28/10)

- **Construites et ouvrables : 43 leçons de novembre**
  (psy 6/9 · sg 4/6 · ca 11/11 · pn 0/12 · ph 12/13 · bi 4/7 · ra 6/7).
- **Manquantes : 22 leçons** (liste ci-dessous). Toutes sont à
  `recu: false` dans `data.js` (état au 06/10) et **aucun PDF source
  évident n'est présent dans ce repo** pour elles. Règle de méthode :
  *source absente = leçon en pause, jamais inventée* → voir § « Sources
  à fournir ».

## Priorité de construction (tombable d'abord — QCM d'annales ELITE)

### Tier S — à construire en premier (fort rendement EMD)
| Rang | Leçon | QCM annales | Pourquoi |
|---|---|---|---|
| 1 | ra-05 Imagerie et radioanatomie du cœur | 17 | le plus tombé des manquantes |
| 2 | bi-05 Métabolisme des lipides/lipoprotéines | 15 | très tombé |
| 3 | bi-06 Biomarqueurs cardiaques | 10 | cœur de l'unité |
| 4 | pn-01 Sémiologie de la dyspnée | 6 | fondation de toute la pneumo |
| 5 | pn-04 Expectoration / vomique | 8 | tombé + différentiels |
| 6 | sg-05 Sémiologie pondérale | 8 | tombé |

### Tier A — cœur pneumo + compléments tombés
pn-07 Signes physiques (5) · pn-05 Hémoptysie (5) · pn-03 Toux (4) ·
pn-08 Syndromes médiastinaux (4) · pn-11 Syndromes pleuraux (4) ·
sg-04 Troubles d'hydratation (6) · bi-04 Liquides d'épanchement (6)

### Tier B — compléter si le temps le permet
pn-02 Douleurs thoraciques pneumo (3) · pn-06 Dysphonie (3) ·
pn-09 Syndromes pulmonaires (3) · pn-12 Ponction pleurale (3) ·
pn-10 Syndromes bronchiques (1) · ph-09 HTA (4) ·
psy-09 Personnalité (4) · psy-08 Prescription (2) · psy-06 Inaugural (0)

> Ordre pneumo conseillé à l'intérieur des tiers : pn-01 → pn-07 →
> pn-09/pn-10/pn-11 (syndromes) → pn-03/pn-04/pn-05 (symptômes) →
> pn-08 → pn-02/pn-06/pn-12. Chaque leçon suit la **méthode intégrale**
> (chartes relues dans les fichiers, source complète, annales exactes
> ELITE, planches réelles, arabe complet, audio 8 FR + résumés FR/AR,
> audit à 0 référence cassée). **Une seule leçon active à la fois.**

## Réalisme calendrier (honnête)

Une leçon au format complet consomme ~2-3 tours substantiels (quotas
images/audio par tour). 22 leçons parfaites en 29 jours exigeraient un
rythme quotidien soutenu **et** les sources dès maintenant. La stratégie
sûre est donc double :
1. **Révision immédiate** sur les 43 leçons déjà ouvrables (la base
   propre est ligne, progression fonctionnelle) — ne pas attendre les
   constructions pour réviser.
2. **Constructions dans l'ordre Tier S → A → B**, chacune livrée
   complète ou pas du tout (jamais de squelette déclaré « fini »).
   À J-7, gel des constructions : place aux recouches/flashcards.

## Sources — RÉSOLU le 28/10 (voir `04-PROTOCOLE-SOURCES-ET-VERSIONS.md`)

Dépôt N-1 MedHaven + dépôt N « UE 1: Cardio » cartographiés :
**21/22 leçons ont une source** (dont ph-09 déjà en version 2026) ;
seule ra-05 reste sans source (séances identifiées, en attente).
Construction immédiate sur N-1, patch différentiel à l'arrivée des
PDF N — sans attendre. Ordre effectif : ra-05 bloquée → **bi-05 en
cours** (plan-source fait : `travail/bi-05-lipides/PLAN-SOURCE.md`)
→ bi-06 → pn-01 → suite des tiers.

## Sauvegarde officielle (faite le 28/10)

Drive → `SEENmed — livraisons / 00_BASE-OFFICIELLE_2026-10-28/`
(https://drive.google.com/drive/folders/1O5QMhvttWd402VUjfyQwAaDeJRfRIvnK)
: LISEZ-MOI + 4 parties, **tailles et MD5 relus côté Drive = locaux**.
Toute future version suivra la même discipline stricte (nouveau dossier
daté, racine unique `medstudy/`, MD5 publiés, jamais d'écrasement).
