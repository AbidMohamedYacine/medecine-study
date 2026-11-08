# Contrôles DELTA38 — grandes planches

Les outils originaux sont conservés inchangés dans `SEENmed-REPRISE/qualite-2026-10-30/`. Ils prescrivent 1376×768 et signalent donc encore les trois infographies DELTA38 (1536×1024, 1024×1536, 1024×1536). Ce n'est pas une validation verte des outils originaux.

Deux copies adaptées maintiennent tous leurs contrôles et ajoutent une prise en charge explicite des grandes planches : attribut HTML `data-large-planche="true"`, côtés d'au moins 768 pixels, surface d'au moins 1 400 000 pixels, ratio entre 0,5 et 2,3, dimensions déclarées exactement égales aux dimensions réelles. Les images non marquées gardent la règle originale. Une image illisible est maintenant une erreur, pas un simple passage silencieux. Aucun redimensionnement ou étirement des trois planches.

Le test négatif reproduit les cas d'image non déclarée, trop petite, absente, corrompue et de dimensions erronées ; chacun provoque une sortie 1 dans les deux contrôleurs. Usage : `python3 test-audits-grandes-planches.py /tmp/.../medstudy` (Pillow requis pour générer la petite image du test). Les scripts de structure/zoom et de thèmes utilisent un serveur temporaire sur 8096 et Playwright.

Sur ca-04 après extraction et fusion de DELTA38 : audit adapté strict 0/0, vérificateur adapté 0 ; tests négatifs 10/10 ; runtime adapté cardio 21/21 ; QCM 9/9 + 16/16 en FR et en AR ; 21 images statiques chargées aux largeurs 390 et 1280 ; 20 onglets et 2 synthèses ; zoom défilable ; 4 thèmes sur fond, onglet actif, boxes ; 2103 autres fichiers inchangés. Runtime original inchangé : TargetCloseError, donc non validé. Les fichiers audio n'ont pas été écoutés.
