# Décisions de l'utilisateur — 28/10/2026 (source d'autorité)

Ces décisions ont été prises **directement par l'utilisateur dans cette
conversation** (formulaire de Questions + messages). Elles priment sur tous
les documents de l'ancien agent conservés dans `handoff-ancien-agent/`.

1. **Priorité immédiate** : réparer le tableau de bord / l'intégration,
   puis rendre **utilisables en révision toutes les leçons du programme
   de l'examen du 26 novembre 2026**. Les reconstructions lourdes viennent
   ensuite, une leçon à la fois.
2. **AN-11 et suivantes (anapath)** : **suppression confirmée de la base
   de travail** (pages, entrées de données, images, voix). Application
   sûre retenue : suppression dans la *base propre* uniquement, avec
   manifeste (`manifeste-suppressions-AN11plus.json`) ; les archives
   Drive d'origine restent **intactes** (filet de sécurité réversible).
   Aucun fichier Drive n'a été effacé.
3. **Format audio définitif** : **8 chapitres FR développés + résumé FR
   + résumé AR uniquement** (pas de 8 chapitres arabes). Narration fluide
   de professeur, français prononcé à la française, arabe neutre.
4. **Transfert du site** : l'utilisateur a fourni le site en **4 parties
   ZIP sur Drive** et a demandé à l'agent de s'en occuper entièrement
   (« you deal with them not me »), avec exigence de prudence sur le
   **stockage** et la sauvegarde. Fait : téléchargement partie par partie,
   déplacement immédiat en `/tmp`, MD5 vérifiés, aucun gros fichier dans
   le repo Git.
5. **Règle de bascule** (message libre de l'utilisateur) : si la solution
   d'origine s'avère meilleure que les nouvelles solutions envisagées,
   l'agent doit le dire — condition unique : **le travail doit
   fonctionner parfaitement, sans problèmes**. Application : la baseline
   d'origine a été **conservée et réparée** (pas de nouveau système),
   car l'audit a prouvé qu'elle était récupérable à 100 % à
   l'exception de 11 images d'AN-06 jamais livrées.
6. **Aucun envoi Drive sans autorisation explicite** : règle maintenue.
   **Addendum (même jour)** : l'utilisateur a autorisé l'envoi de la
   base propre (« do it »), organisé strictement. Fait le 28/10 :
   dossier Drive `SEENmed — livraisons / 00_BASE-OFFICIELLE_2026-10-28/`
   (LISEZ-MOI + 4 parties, tailles et MD5 relus côté Drive = locaux).
   Tout futur envoi exigera une nouvelle autorisation.
7. **Programme du 26/11 confirmé (28/10)** : la **pneumologie est
   incluse** ; seuls Anapath + Immunologie sont reportés à janvier.
   Voir `02-PLAN-26-NOVEMBRE-2026.md`.
8. **« Details » clarifiés (28/10)** : il s'agit de **tous les détails
   de méthode en général** (ex. le format audio arabe) qui ne doivent
   ni se perdre ni dériver. Réponse mise en place :
   `03-DETAILS-LOCK.md` (registre unique, statuts, contradictions
   tranchées), à relire avec les chartes avant chaque leçon.

## Points encore ouverts
- Fourniture des **PDF sources** des 22 leçons manquantes de novembre
  (liste priorisée dans `02-PLAN-26-NOVEMBRE-2026.md`) — sans source,
  aucune construction (règle de méthode).
- Revalidation des **voix** au premier lot audio (anciens identifiants
  liés à la session précédente).
