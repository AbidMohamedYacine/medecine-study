# SEENmed project handoff — definitive reset plan

## Read first

Read these files before doing anything:

1. `analysis/ARENA-AGENT-HANDOFF.md`
2. `analysis/SEENMED-METHOD-COMPLETE-CONSOLIDATED.md`
3. `analysis/WORKFLOW-LOCK.md`
4. `analysis/ANAPATH-NEXT-PROTOCOL.md`
5. `analysis/MAINLINE-BASELINE.md`

The user is restarting AN-11 and every later lesson from zero. Do not continue the previous AN-11 draft.

## Authoritative website baseline

Correct full Drive package:

- Name: `SEENmed-DASHBOARD-FIXED-FULL-53-AN03-06-10.zip`
- Drive link: https://drive.google.com/file/d/1c3uzXvv_QeI22Uax23_D24fNCOqIl0vs/view?usp=drivesdk
- Size: 329,264,608 bytes
- Files: 2,202
- MD5: `1fa8f6240b2b2a95b396e58569adf08d`

Do not use the incorrect 122 MB package. Do not overwrite the verified Drive baseline. Do not upload a new package unless the user explicitly authorizes it.

## Definitive scope reset

### Keep and repair

Keep AN-01 through AN-10. In particular, preserve and verify:

- AN-03 / MEC
- AN-06
- AN-07
- AN-08
- AN-09
- AN-10

The user saw AN-03 and AN-06 through AN-10 separated from the correct module/tableau de bord. This must be investigated and fixed before rebuilding AN-11+.

Required dashboard repair audit:

1. Compare the saved workspace against the latest Drive baseline.
2. Identify the actual dashboard/module/data separation problem.
3. Verify `data.js`, module IDs, lesson IDs, URLs, aliases and `recu` flags.
4. Verify page paths and body `data-lesson-id` values.
5. Verify dashboard cards, progression page and module view use the same data source.
6. Verify progress keys and links for AN-03, AN-06, AN-07, AN-08, AN-09 and AN-10.
7. Fix the issue without changing the validated visual architecture.
8. Test every repaired “Ouvrir le résumé” button.

### Delete and rebuild from zero

Delete every ANAPATH item related to AN-11 and later from the working website baseline:

- AN-11
- AN-12
- AN-13
- AN-14
- AN-15 and every later ANAPATH lesson
- their lesson HTML pages;
- their dashboard/data entries;
- their progress aliases/keys;
- their lesson-specific audio;
- their lesson-specific generated assets;
- their lesson-specific page references.

The user has now explicitly reversed the earlier “retain AN-11/13/14 images” decision. For this reset, remove all AN-11+ website lesson content and assets completely. Rebuild them later from authentic sources.

Do not delete unrelated modules or the completed AN-01 through AN-10 assets.

## What the new agent will receive

The user will provide:

1. the saved workspace from the previous work;
2. the latest full website version from Drive.

Analyze both before modifying anything. The Drive version is the complete reference; the workspace may contain partial or incorrect changes.

## Required workflow

### Phase 1 — restore a clean connected base

1. Inspect the saved workspace.
2. Extract the full Drive baseline independently in `/tmp`.
3. Compare manifests, page paths, data files, scripts, CSS, images and audio.
4. Remove AN-11+ completely.
5. Repair the AN-03/06/07/08/09/10 dashboard/module separation.
6. Test front end and back end.
7. Produce a clean named base manifest.

### Phase 2 — rebuild future lessons one at a time

For every lesson from AN-11 onward:

1. Read the complete authentic source.
2. Write a source-grounded plan.
3. Build the full page using the validated MEC/SEENmed architecture, not a simplified shell.
4. Include 10–18 named thematic sections.
5. Use complete `lbox` bullet content.
6. Create dedicated visual boards and a dedicated résumé total board.
7. Build one image per flash-card case.
8. Build the résumé from the source, including tombable priorities and exam traps.
9. Add exact annales when available; never invent official answers.
10. Add specific QCM with proposition-by-proposition explanations.
11. Translate the complete course into contextual Arabic.
12. Generate 8 developed French audio chapters and a French résumé audio.
13. Generate the Arabic résumé audio only, unless explicitly instructed otherwise.
14. Add `cineData`, flashcards, progress, lightbox and all navigation.
15. Audit all front-end and back-end connections.
16. Package and verify only after the lesson is genuinely complete.

## Voice and narration rules

- French chapters must be developed, normally about 900–1500 characters where justified.
- Do not use short compressed clips.
- One Arabic voice is for the Arabic résumé only.
- Do not generate eight Arabic chapter voices unless the user explicitly changes the order.

## Storage rules

- Full archives and extracted complete websites belong in `/tmp`, never `/home/user`.
- Keep only minimal working files, manifests, plans, audits and current-lesson work in `/home/user`.
- Never delete a source before a safe manifest and replacement/source copy exist.
- Run `python3 tools/espace.py` after cleanup.

## User operating order

When the user says `go`, continue autonomously. Do not wait for acceptance or narrate every tiny step. Maximize useful work per response and use the full available tool capacity. Work efficiently toward a complete lesson in two or three substantial responses when technically possible. Do not jump ahead while the current correction or lesson is incomplete. Report only meaningful results, blockers and final verification.

## Immediate next action

Do not continue the current AN-11 draft. Wait for the user’s saved workspace and latest Drive version, then:

1. analyze both;
2. remove AN-11+ completely;
3. repair the dashboard/module separation for AN-03 and AN-06 through AN-10;
4. verify the clean connected base;
5. only then begin a new source-grounded AN-11 build from zero.
