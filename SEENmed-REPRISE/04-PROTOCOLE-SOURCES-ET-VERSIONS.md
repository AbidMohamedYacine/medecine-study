# Protocole Sources & Versions — construire sans attendre, patcher sans refaire

> Décidé avec l'utilisateur le 28/10/2026. Objectif : avancer dès
> maintenant sur les sources de l'année précédente, puis intégrer le
> PDF de l'année en cours par **différentiel ciblé** — jamais de
> reconstruction complète, jamais d'attente bloquante.

## 1. Les deux dépôts de sources (référence permanente)

| Dépôt | Drive | Rôle |
|---|---|---|
| **N-1 (MedHaven 2023)** | `3eme année médecine MedHaven (2023)` — `1-1qmHESAhjsYMXaiVULwb1LCYCNLRfyr` → `U1/ cardio` `1-D-WfHmkAJZutiVek5MWZm8LxZ9mS_Pw` | Sources complètes 2025/2026 : base de construction immédiate |
| **N (année en cours)** | `UE 1: Cardio🫀` — `12lKQj0teZe40WzK6nz3EmpixJYBqRfhH` (sous-dossiers datés oct. 2026) | Nouvelles versions des enseignants, au fil de l'eau : base des patchs |

## 2. Règles du protocole (verrouillées)

1. **Empreinte de source obligatoire** pour chaque leçon construite :
   nom de fichier, Drive ID, taille, date, nb de diapos/pages,
   enseignant, étiquette `N-1` ou `N`. Écrite dans le plan-source de
   la leçon (`travail/<lecon>/PLAN-SOURCE.md`).
2. **Construction immédiate sur N-1** au format intégral (chartes),
   sans attendre le PDF N. La page porte en interne son statut de
   source ; rien n'est inventé : les zones testées en annales mais
   absentes des diapos sont signalées dans le plan (« à confirmer sur
   source N ») et enseignées uniquement à hauteur de ce que les
   annales + corrigés officiels établissent.
3. **À l'arrivée du PDF N** (déposé par l'utilisateur ou repéré dans
   le dossier N) : extraction texte + images, **diff structuré**
   (diapos ajoutées/retirées/modifiées, chiffres, tableaux, figures),
   puis **patch ciblé uniquement** : sections touchées, planches
   concernées, `arData`/`kwData`, QCM affectés, chapitres audio
   affectés (régénérés eux seuls). Re-audit complet de la leçon,
   empreinte mise à jour `N-1 → N (patch du JJ/MM)`.
4. **Si le diff est vide ou cosmétique** : on le consigne (« source N
   identique en substance ») et on ne touche à rien.
5. Les sources téléchargées vivent en `/tmp/sources/<lecon>/` pendant
   le travail ; seuls le plan-source, les manifestes et les empreintes
   (légers) sont versionnés dans Git. Aucun PDF source lourd en Git.

## 3. Cartographie des 22 leçons manquantes de novembre (28/10/2026)

Statut : ✅ source repérée · ❌ introuvable à ce jour · (N) = déjà en
version année en cours.

| Leçon | Source N-1 (MedHaven) | Drive ID | Note |
|---|---|---|---|
| pn-01 Dyspnée | ✅ `1- Sémiologie de la dyspnée.pptx` | `1kM6mm_HOwE8dR8ADPR9a6I5yJ0g1r5Kv` | |
| pn-02 Douleurs thoraciques pneumo | ✅ `9/Douleur Thr.pdf` | `1y1ITKG5bmTfTCw1Vyse16vvYXfcNFOKx` | à confirmer à l'ouverture |
| pn-03 Toux | ✅ `3/ SEMIOLOGIE DE LA TOUX externe.pptx` | `1l2-3KF2GAZ9z9NpwN08KUmHS-NB24Ero` | |
| pn-04 Expectoration/vomique | ✅ `2/ - Expectoration-Vomique….pptx` | `1yuSa1R1VOZSKGHifIHlf8mLbPA0BhQYM` | + fichier voisin `11- Étude cytobactériologique…` (`13zhrEFV…`) hors `data.js` : à rattacher ou créer ? |
| pn-05 Hémoptysie | ✅ `5/ Hemoptysie 3eme année 2025-2026.pptx` | `1q9Hg6tWj_VwnV7ory2tBACiN8j5wDJIj` | ⚠️ 157 Ko seulement : complétude à vérifier |
| pn-06 Dysphonie | ✅ `6/ DYSPHONIE 1.pptx` | `1YhXhmmu-0OhiaaTzLBD5xTQHWct2-LJB` | |
| pn-07 Signes physiques | ✅ `7/ Signes physique en pneumologie.pptx` | `1buHhYMaITyi9XjQ9ecknQDu8V8xl0luG` | |
| pn-08 Syndromes médiastinaux | ✅ `12/ syndrome mediastinaux COURS 3EME ANNEE.pptx` | `14eKUNXPaX044P0zWel8DpYT32S7iO6yg` | |
| pn-09 Syndromes pulmonaires | ✅ `4/ syndromes pulmonaires.pdf` | `1kgbTKaEU2KsTCnImFd74QxgfG0s0Rj8M` | |
| pn-10 Syndromes bronchiques | ✅ `8/ version détaillée … syndrome bronchique.pptx` | `1SDQZ1H1KWFsD7q76Dx8HmEKkSS7qRpHf` | |
| pn-11 Syndromes pleuraux | ✅ `10/ Les syndromes pleuraux word.docx` | `17tXdoCcDFLMCxbzGKzwlsIeCD7pd3my2` | source Word (pas de diapos) |
| pn-12 Ponction pleurale | ✅ `10/ Explorations pulmonaires- la ponction pleurale….pptx` | `1sxHPXnX-X9M4KEo3sPqnzj2eY5InhFCz` | |
| sg-04 Hydratation | ✅ `5/ Semiologie hydratation.pptx` | `1ypVyhb4BJ_c3In0RcbnD1zeWNAIO6NXN` | + `6/ Désordres électrolytiques.pptx` (`1HO4K3br…`) : 2ᵉ volet probable |
| sg-05 Pondérale | ✅ `04/ -Sémiologie pondérale.pdf` | `1YwMsHFjgzgY26NCGy-ql7BnvcXjyaEUj` | |
| psy-06 Inaugural | ✅ `6_ cours inaugural semio.pdf` | `18mjMCeCdituDZXgAiCSvSF7Xar-BT4oM` | ⚠️ ne pas prendre le .pptx de 1,2 Go |
| psy-08 Prescription | ✅ `8-Psychologie de la prescription.pdf` | `1If1q9UEb6kMFqcbze7EA6aX-NK8qX7D2` | |
| psy-09 Personnalité | ✅ `9- Fonctionnement de la personnalité` | `1_sjRqNrx_mYQgMj_MiH9mMhz_gNqqcj2` | |
| bi-04 Épanchements | ✅ `5/ Liquides d'épanchement.pptx` | `1r_tAngo877Mu5e4iddiugyh8aDY0Pg2t` | |
| bi-05 Lipides | ✅ `6/ lipide - E 2026.pptx` | `1e0Aag3-u3OjWkX_ZEgg1YtZWU07owG1m` | **en cours** (plan-source fait) |
| bi-06 Biomarqueurs cardiaques | ✅ `7/biomarqeur cardiaque - E 2026.pdf` | `1qx87LvbO2yNPZFxRyX8oK0DuBqK75H3E` | |
| ph-09 HTA | ✅ **(N)** `9_physiopath HTA.pdf` | `1gMFeJH5LFBADokmObrxG-_Fy23ob-niS` | déjà en version 2026 |
| ra-05 Radioanatomie du cœur | ❌ absente des deux dépôts | — | Séances identifiées (programme radio 2025-2026) : 09.10 Dr KLOUCHA « Lecture RX thoracique normale + Radio-anatomie du cœur » ; 13.10 Dr BELMESSABIH « Explorations cardiovasculaires en imagerie ». Source à obtenir (utilisateur/enseignant) — leçon en pause, pas d'invention |

## 4. Méthode de construction — état vérifié le 28/10/2026

Réponse à « what's up with the method, do you got everything right? » :
**oui, et c'est désormais écrit et versionné**, plus seulement « su » :
- 📄 Chartes **réelles relues dans les fichiers** : CHARTE-IMAGES (14 Ko,
  relue en entier), CHARTE-LEÇON (restaurée), CHARTE-ARABE, CHARTE-CINÉ,
  CHARTE-MOTS-CLES ; CHARTE-IMMUNO (§12-14 = recettes images) récupérée.
- 🔒 `03-DETAILS-LOCK.md` : chaque détail + contradictions tranchées.
- 🎯 Références : structure ca-10, profondeur MEC/ph-10 ; audit
  `tools/audit_seenmed.py` à 0 avant toute annonce « fini ».
- ⏳ Reste ouvert (assumé, non bloquant pour démarrer) : revalidation
  des voix au premier lot audio ; source ra-05 ; rattachement des 2
  fichiers « extra » (cytobactério sécrétions, désordres électrolytiques).
