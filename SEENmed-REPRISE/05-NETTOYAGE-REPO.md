# Nettoyage du repo — 28/10/2026 (prudent, sur demande utilisateur)

## Fait
- Supprimé **1 seul fichier** : `photo_2026-10-04_20-01-27 (2).jpg`,
  doublon **octet pour octet** (MD5 `b4b91221…`) de
  `photo_2026-10-04_20-01-27.jpg` (294 790 o). Aucune perte.
- Ajouté `.gitignore` : `google_drive/`, `*.zip`, PNG/JPG bruts des
  planches en cours, `*.mp3` — le repo ne peut plus se remplir par
  accident ; seuls docs, manifestes et WebP finaux y entrent.

## Volontairement NON supprimé (et pourquoi)
- **QCM/annales** : ELITE CARDIO, CURE ANAPATH/IMMUNO, HPS 1 corrigé,
  Notes de QCMs, QCM_Revision… — intouchables (demande utilisateur).
- **PDF sources des professeurs** : encore nécessaires (patchs source N,
  phase janvier Anapath/Immuno). Les « quasi-doublons » détectés
  (ex. ultrasons ×2 à 6 octets près, pathologie vasculaire ×3) ne sont
  **pas identiques** : suppression seulement après comparaison de
  contenu, leçon par leçon, jamais en masse.
- **`seenmri-upload.zip` (17,9 Mo)** : projet annexe IRM de
  l'utilisateur, hors périmètre « leçons » — décision lui appartenant.
  Candidat n°1 si un jour il faut vraiment alléger l'arbre de travail.

## Vérité technique à retenir
Supprimer un fichier suivi **n'allège pas l'historique GitHub**
(pack actuel ≈ 92 Mio : les objets restent dans l'historique).
Le levier réel = ne plus ajouter de lourds (`.gitignore` ci-dessus)
+ archives sur Drive + travail en `/tmp`. L'arbre de travail
(~117 Mo, quasi entièrement le commit initial de sources) est sain ;
nos ajouts SEENmed-REPRISE restent de l'ordre de quelques Mo.
