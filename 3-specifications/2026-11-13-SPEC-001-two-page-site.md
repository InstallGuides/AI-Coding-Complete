# SPEC-001: A two-page personal website

**Status:** done
**Date:** 2026-11-13

Builds on: `2-decisions/2026-11-13-ADR-001-plain-html-no-framework.md`

## Goal

A small personal website with a home page and an about page, ready for you to make your own.

## Why

To give the project a real thing to build, publish and measure, so every numbered folder has a believable job.

## Behavior

- `site/index.html`, the home page: a header image, your name, one welcoming paragraph, and a link to the about page.
- `site/about.html`: a short "about me" section and a link back home.
- Both pages share one stylesheet, `site/style.css`, and the same header and footer.
- Placeholder text says "Your Name" and similar, so it's obvious what to replace.
- No JavaScript and no files from other websites, so the site works opened straight from the disk.

## Done when (acceptance)

- [x] Double-clicking `site/index.html` opens the home page, and its link reaches the about page and back.
- [x] In a terminal in this folder, `uv run scripts/check_site.py` ends with `All checks passed`. The script checks that every page has a title and that every link and image inside the site exists, and prints each page's size.

## Out of scope

- Your own text and photo. That's SPEC-002.
- Publishing. That's a procedure, in `4-playbooks/2026-11-13-PB-002-publish-the-site.md`.
- A contact form, which needs a server. It was in the first draft (`8-archive/2026-11-13-spec-001-first-draft.md`) and was dropped.
