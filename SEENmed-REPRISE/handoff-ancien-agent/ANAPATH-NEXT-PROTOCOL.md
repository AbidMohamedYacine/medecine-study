# ANAPATH next protocol — dashboard, lesson coordination and rebuild scope

## Current baseline

The intended baseline is the latest verified Drive package built from the genuine 53-lesson website plus the added AN-06, AN-07 and AN-08 assets. Do not use the older malformed concatenated archive.

## Rebuild scope

- AN-15 and every ANAPATH lesson after it: rebuild from the source from zero. Do not treat existing pages as final and do not use them as pedagogical templates.
- AN-11, AN-13 and AN-14: do not erase the existing pages/assets blindly. Preserve and inventory their existing images, then compare each image with the new source-grounded lesson content when those lessons are rebuilt from Drive sources later. Reuse only images that actually match the new content.
- AN-06, AN-07, AN-08, AN-09 and AN-10: treat as completed candidate lessons, but verify page, images, audio, Arabic, QCM, data and dashboard coordination before declaring them finished.
- MEC / AN-03: must remain visible and openable.

## Dashboard/site coordination audit

For every completed lesson, verify all of the following as one chain:

1. The lesson page exists at the exact path listed in `medstudy/js/data.js`.
2. The lesson ID in `data.js` equals the page `body[data-lesson-id]`.
3. The page is linked from the correct module/tableau card.
4. The page link is not broken by a wrong filename, accent, case or alias.
5. The page's assets use paths that exist.
6. The page appears in the correct module and does not appear as absent or unfinished when its verified status is recorded.
7. The progress key used by the dashboard matches the page/reference ID.
8. Aliases are explicit and do not create duplicate or invisible lessons.
9. `recu`, `url`, QCM counts and display labels are consistent.
10. The dashboard, module cards and progression page all use the same data source and same reference ID.

Specific lessons to test first:
- AN-03 MEC
- AN-06
- AN-07
- AN-08
- AN-09
- AN-10
- AN-11
- AN-13
- AN-14
- RA-06 thorax pathologique

## Safe correction rule

Do not modify the Drive baseline directly. Work in `/tmp` or a controlled workspace copy, create a manifest of every changed file, test the dashboard and page links, then upload a named increment to Drive. Never delete the only copy of an image before its replacement and manifest entry exist.

## Storage rule

The workspace is already over the snapshot limit. Keep full archives and extracted website copies in `/tmp`, upload them to Drive, then remove them immediately. Keep only source-grounded analyses, the method, charters, manifests and the current lesson's minimal working files in `/home/user`.
