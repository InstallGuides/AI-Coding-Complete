# PB-001: Build SPEC-001 (the two-page site)

**Status:** done
**Date:** 2026-11-13

A playbook is step-by-step instructions your assistant follows. This one is a one-time handoff: a plan and a task list, so a fresh conversation can build the site without the one that wrote the spec.

## Read first

- `3-specifications/2026-11-13-SPEC-001-two-page-site.md`: what to build, and how you'll know it's done.
- `2-decisions/2026-11-13-ADR-001-plain-html-no-framework.md`: already decided, plain HTML and CSS.

## Plan

Four files in `site/`: two pages, a stylesheet and a header image. The image is drawn in `5-assets/` first and copied into `site/images/`. The about page's text is drafted in `5-assets/` first too.

## Tasks

Do one task at a time, check it, and tick its box before starting the next.

- [x] 1. Draw the header image as `5-assets/2026-11-13-header-image.svg`, and copy it to `site/images/header.svg`.
- [x] 2. Write `site/style.css`: readable text, a centered column, and styles for the header and footer.
- [x] 3. Write `site/index.html` with the header image, the placeholder name, a welcome paragraph and a link to the about page.
- [x] 4. Draft the about text in `5-assets/2026-11-13-about-page-draft.md`, then write `site/about.html` from it.
- [x] 5. Check the site: every page in `site/` has a title, and every link and image points to a file that exists. Fix anything that's wrong. Record each page's size in `7-performance/2026-11-13-page-sizes.md`.
- [x] 6. Tick the spec's "Done when" boxes and set its Status to `done`.
- [x] 7. Update `CHANGELOG.md` and write a handoff note in `work-ledger/`.

## Done when

Every task above is ticked, the site checks out, and every box in the spec's "Done when" list is ticked.
