# Journal d'images — phase 2 (STANDARD-OR-v3 §8.3)

Style des lots ff-* : infographie dense bleu nuit/or, titres et libellés français
exacts, 1376×768 WebP q83. Contrôle : lecture zoom de chaque planche (agent-1).

## Lot 1 — 2026-10-30 (10 générations, 1 bloc) : 8 installées, 2 rejetées

| Fichier | Verdict | Raison |
|---|---|---|
| pn-04/ff-types.webp | **GARDER** | 5 types, libellés et chiffres exacts (150 à 200 par 24 h, 4 couches) |
| pn-04/ff-vomique.webp | **GARDER** | qualités/formes/origines exactes, mécanisme lisible |
| pn-01/ff-gravite.webp | **GARDER** | tous les seuils exacts (FC 120, SpO2 90 %, BNP 300, D-dimères 500) |
| bi-06/ff-troponine.webp | **GARDER** | trio TnC/TnI/TnT + horloges 1–2 h / 3–6 h exacts |
| bi-06/ff-cinetique.webp | **GARDER** | 3 courbes + durées exactes (24 h, 2–3 j, TnT 10 j) |
| pn-04/ff-pieges.webp | GARDER (corriger un jour) | dense et juste ; manquent les libellés « 100 mL/j, 95 % d'eau » et « tubage gastrique » (présents dans la liste HTML voisine) |
| pn-04/ff-bronchorrhee.webp | GARDER (corriger un jour) | 7 critères + 5 couleurs exacts ; le libellé « le matin : toilette des bronches » absent (soleil seul) |
| pn-01/ff-nyha.webp | GARDER (corriger un jour) | bascule 2 étages présente ; libellé « Stade IV : dyspnée de repos » absent |
| pn-01/ff-composantes.webp | **REFAIRE** | générée sans aucun libellé (icônes seules) — non installée |
| pn-01/ff-phases.webp | **REFAIRE** | libellés phase/Kussmaul/Cheyne-Stokes absents + compteur décoratif « 028 » inventé — non installée |

Anciennes versions sauvegardées (banc local agent-1, `/tmp/old-ff-2026-10-30/`).
Installées : delta 10 Drive. Audit après installation : 0 bloquant ×3.

## À générer (lots suivants, selon quotas autorisés)
- REFAIRE : pn-01 ff-composantes, pn-01 ff-phases (prompts renforcés : libellés en gros).
- bi-06 : ff-algo, ff-bnp (même style).
- Planches de sections des 3 leçons (celles jugées pauvres/hors format ; bi-06 : 16 planches 1536×1024 signalées IMG-DIMS).
- Éventuels CORRIGER ci-dessus si un lot a des places libres.
