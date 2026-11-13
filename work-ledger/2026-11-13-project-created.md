# Project created

**Summary:** This project was created with one worked feature, a two-page website, taken through every numbered folder from research to measurement.

## What was done

- Compared three hosts (`1-research/`), decided on plain HTML (`ADR-001`), wrote the spec (`SPEC-001`) and built it from the playbook (`PB-001`).
- The site is in `site/`. `uv run scripts/check_site.py` passes, and the page sizes are in `7-performance/`.
- The header image and the about-page text were drafted in `5-assets/`. An announcement is drafted in `6-outreach/`. The spec's first draft, with a contact form, is in `8-archive/`.

## Decisions and paths not taken

- The contact form was dropped: it needs a server, which breaks ADR-001.
- Netlify Drop was chosen for publishing because it needs no Git and no build step (`PB-002`).

## Next

- Write SPEC-002 to make the site yours, then a playbook for it, and build from it in a fresh conversation.
- Publish with PB-002 when you're happy with it.
