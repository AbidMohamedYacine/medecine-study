# START HERE — SEENmed new Arena agent

## First instruction

Do not ask the user to repeat the project history. Read this file completely, then read:

- `analysis/ARENA-AGENT-HANDOFF.md`
- `analysis/SEENMED-METHOD-COMPLETE-CONSOLIDATED.md`
- `analysis/WORKFLOW-LOCK.md`
- `analysis/ANAPATH-NEXT-PROTOCOL.md`
- `analysis/MAINLINE-BASELINE.md`

Then inspect the workspace files the user provides and compare them with the latest full Drive website before changing anything.

## User’s required working style

The user wants autonomous, efficient, high-quality execution:

- When the user says “go” or “continue”, do the work immediately.
- Do not wait for confirmation between ordinary steps.
- Maximize useful work in each response/tool cycle.
- Do not send dozens of tiny progress messages.
- Do not narrate every command.
- Work through complete stages and report meaningful results only.
- Aim to finish one lesson in two or three substantial responses when technically possible.
- Follow the method even when it takes time; do not replace quality with shortcuts.
- Keep the user informed honestly about what is complete, incomplete or blocked.
- Never claim a lesson is finished when only images, audio or a draft page are finished.

## Definitive reset requested by the user

The user is restarting AN-11 and every later ANAPATH lesson from zero.

### Keep

AN-01 through AN-10, especially:

- AN-03 / MEC
- AN-06
- AN-07
- AN-08
- AN-09
- AN-10

### Remove from the working website baseline

Delete every AN-11+ item, including:

- lesson HTML pages;
- dashboard/data entries;
- progress IDs and aliases;
- lesson-specific audio;
- lesson-specific images and generated assets;
- page references and navigation entries.

This is a new explicit user decision. Do not preserve AN-11/13/14 old assets in the working website. They will be rebuilt from scratch later.

## First work phase

Before rebuilding any future lesson:

1. Analyze the saved workspace supplied by the user.
2. Analyze the latest full Drive version.
3. Compare manifests and structure.
4. Build a clean connected base.
5. Repair the dashboard/module separation for AN-03 and AN-06 through AN-10.
6. Test exact URLs, page IDs, `data.js`, progress keys, dashboard cards, module cards and “Ouvrir le résumé” links.
7. Only after this clean base passes should AN-11 be started.

## Main Drive baseline

Use this verified full package, not the old 122 MB error package:

https://drive.google.com/file/d/1c3uzXvv_QeI22Uax23_D24fNCOqIl0vs/view?usp=drivesdk

Name: `SEENmed-DASHBOARD-FIXED-FULL-53-AN03-06-10.zip`

Size: 329,264,608 bytes
MD5: `1fa8f6240b2b2a95b396e58569adf08d`

Do not upload or replace it unless the user explicitly authorizes a finished verified increment.

## Full lesson method

For each rebuilt lesson:

source → source-grounded plan → 10–18 named sections → structured lboxes → dedicated images → flash image per case → dedicated résumé total → annales/QCM → complete Arabic → French audio → French résumé audio → Arabic résumé audio only → cineData → website integration → technical/visual/pedagogical audit → named Drive package and MD5.

Use validated MEC and physiopathology pages as structural references. Do not use simplified drafts or generated skeleton pages as templates.

## Voice rule

- Developed French chapter narration, normally around 900–1500 characters where justified.
- One Arabic voice for the Arabic résumé only.
- Do not generate eight Arabic chapter voices unless the user explicitly changes this.
- Short compressed narration is not final.

## Storage rule

- Full archives and extracted websites go in `/tmp`.
- Keep only minimal active work, manifests, audits and method files in `/home/user`.
- Run `python3 tools/espace.py` after cleanup.
- Never upload a partial lesson as final.
