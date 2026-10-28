# DETAILS LOCK — Registre unique des détails qui ne doivent plus dériver

> But (demande utilisateur 28/10) : aucun « détail en général » — comme
> le format audio arabe — ne doit plus être perdu, contredit ou réinventé
> entre agents/sessions. Ce registre est la **seule source de vérité**
> pour chaque détail listé. En cas de conflit avec un ancien document,
> **ce registre + les vraies chartes priment**. Chaque détail porte son
> statut : ✅ CONFIRMÉ (par l'utilisateur ou par les fichiers) ·
> ⏳ À VALIDER (ne pas appliquer en silence) · 📄 LU DANS LES FICHIERS.

## A. Décisions produit (utilisateur)
- ✅ **Audio** : 8 chapitres FR développés + résumé FR + **résumé AR
  uniquement**. Jamais 8 chapitres arabes (l'ancien format ra-02 est
  historique). Narration fluide de professeur (origine→mécanisme→
  conséquence), jamais une liste ; ~900-1500 car./clip, couper+fusionner
  si besoin ; français prononcé à la française ; arabe neutre non-khaliji ;
  unités en toutes lettres ; site silencieux sans clic.
- ⏳ **Voix** : `voice-00` (FR) / `voice-03` (AR) appartenaient à
  l'ancienne session. À revalider au premier lot : si indisponibles,
  l'utilisateur re-choisit **une fois** des équivalentes (FR narration ;
  AR féminine éducative neutre), puis verrouillage définitif.
  Astuce filtre TTS 📄 : éviter « fusée » à l'oral → « queue de comète
  verticale » (« fusées » OK à l'écrit).
- ✅ **Priorités examen** : 26/11 = Cardio-Respiratoire **avec pneumo** ;
  janvier = Anapath + Immuno seuls.
- ✅ **AN-11+** : absents de la base de travail (reconstructions future
  depuis sources) ; archives Drive d'origine intactes.
- ✅ **Stockage strict** : une base officielle datée à la fois sur Drive
  (racine unique `medstudy/`, MD5 publiés, jamais d'écrasement) ;
  code/docs légers en Git ; gros fichiers en `/tmp` pendant le travail ;
  aucun ZIP >100 Mo via le connecteur (découpage en parties ≤ ~80 Mo,
  extraction fusionnée vérifiée).

## B. Structure d'une leçon (📄 CHARTE-LECON restaurée + mesuré)
- 10-18 **sections thématiques nommées** (plan réel du cours, jamais
  s1-s6 génériques) ; contenu **en `lbox` à puces cochables**, zéro
  paragraphe de prose hors boîte (seule exception : courte `lsub`) ;
  références : AN-03/MEC, ca-10 (structure), ph-10/ca-08/im-04/bi-03.
- **20-26 planches** : hero, mindmap (style neuf/leçon), 1/section,
  `ff-*` 1/case de fiche flash (4-7 cases, jamais une image unique),
  `total.webp` = synthèse **générée dédiée** (pas de collage, sans
  réponses QCM).
- **QCM numérotés** : annales exactes d'abord (texte + corrigé officiel,
  jamais inventés), puis entraînement renuméroté, explication
  proposition par proposition + mémo piège + `data-answer`.
- **Méthode résumé** : tombable (annales) = développé (pourquoi +
  simplification + mnémotechnique + piège) ; non-tombable = condensé
  sans perte ; hiérarchie = cours × annales × corrigés.

## C. Images (📄 vraie CHARTE-IMAGES 14 Ko — relue le 28/10)
- Règle mère : **montrer la chose réelle** (organe/cellule/geste/tracé +
  scène clinique), test des 4 Questions avant tout prompt ; métaphore
  seulement porteuse **avec médaillons de réalité**, jamais décor dominant ;
  **siège anatomique exact** allumé dans l'organe ; jamais la même phrase
  deux fois ; jamais de planche « que des mots » (y compris ff/total) ;
  dessins **sans lettres à l'intérieur**, texte dans encadrés listés.
- 100 % français, aucun anglais, chiffres écrits, flèches étiquetées,
  étapes numérotées, ≤~12 mots/étiquette, aucun texte minuscule ;
  styles **variés** choisis pour l'idée ; rejetés : néon-sur-fond-sombre
  systématique et esthétique IRM/scanner ; paysage 16:9 ; PNG→WebP
  **q83** (planches) puis suppression du PNG ; relecture zoom obligatoire
  (anglais / doublons / chiffres inventés), réparations sans crédit quand
  possible ; quota 10 générations/tour → ne jamais compresser le format.
- **Reels** : extraction PyMuPDF AVANT génération, jeter <120 px, légende
  = texte de la diapo (jamais de diagnostic inventé), WebP **q90**,
  `assets/img/<lecon>/reel/`, rendu `.reel-strip` source citée
  (enseignant + diapo + titre), jamais agrandi (`max-height:330px`) ;
  **sélectif** : garder photos/schémas/tableaux/courbes, supprimer les
  diapos-texte.
- Recettes anti-défauts génération : `CHARTE-IMMUNO.md` §12-§14
  (comptes explicites, jamais d'équation, mots inventés, layouts fiables…)
  — à appliquer à tous les modules, pas qu'à l'immuno.

## D. Arabe & mots-clés (📄 CHARTE-ARABE / CHARTE-MOTS-CLES)
- Bascule hybride (globale ع/FR + puce locale **à droite**) ; couverture
  totale des boxes/tableaux/explications QCM ; **énoncés QCM en français** ;
  arabe standard simplifié contextuel (jamais mot-à-mot) ; terme FR gardé
  en `<bdi class="fr-term">` + équivalent arabe 1ʳᵉ occurrence ; aucun
  latin nu (chiffres/unités en `fr-plain`) ; `data-tr`↔`arData` zéro
  orpheline, JSON validé.
- Mots-clés : panneau **à droite**, fermer visible, tri alpha/sections,
  30-50 termes contextualisés FR+AR (`kwData` t/s/n/d/a).
- Application : leçons nouvelles depuis ra-02 ; les anciennes pages FR
  seules restent utilisables (pas de retouche rétroactive sauf demande).

## E. Intégration & vérité des livraisons (📄 + incidents vécus)
- Chaîne unique à tester à chaque livraison (`tools/audit_seenmed.py`
  doit sortir à 0, hors défaut documenté) : `data.js` url ↔ fichier ↔
  `body[data-lesson-id]` ↔ assets ↔ progression (`refId`/alias unique,
  ex. psy-01 alias sg-00) ↔ boutons dashboard (`url` ⇒ « Ouvrir le
  résumé » ; `recu` = cours reçu en amphi, ne pas confondre).
- **Une validation technique ≠ qualité pédagogique** ; jamais déclarer
  « fini » un partiel ; une leçon active à la fois ; source absente =
  pause déclarée ; **relire les chartes dans les fichiers** avant chaque
  leçon (jamais de mémoire — incident de la fausse charte, 26/10).
- Pièges d'archive bannis : ZIP multi-racines (cause du bug AN-03/06-10),
  noms quasi-identiques FINAL/CORRECT/FIXED sans MD5, fusion manuelle
  non auditée, compteur `qcm: 0` laissé sur une page construite.

## F. Contradictions anciennes — tranchées ici définitivement
| Sujet | Anciens docs disaient | **Règle verrouillée** |
|---|---|---|
| Chapitres audio AR | 8 AR (workflow/ciné) vs résumé seul | **Résumé AR seul** ✅ |
| Images AN-11/13/14 | conserver vs tout supprimer | **Hors base de travail, archives intactes** ✅ |
| Référence structure | MEC vs ca-10 vs ph-* | **ca-10 structure + MEC/ph-10 profondeur** |
| « Dashboard fixed » 27/10 | affirmé | **Faux sur pièces — réparé le 28/10** |
| ph dégradées (26/10) | 16 lbox | **Métriques actuelles supérieures ; validation visuelle encore requise** |
