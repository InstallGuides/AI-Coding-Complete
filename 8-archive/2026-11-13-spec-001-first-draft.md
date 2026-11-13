# SPEC-001 (first draft): A personal website with a contact form

**Status:** superseded by `3-specifications/2026-11-13-SPEC-001-two-page-site.md`
**Date:** 2026-11-13

This was the first draft of SPEC-001. It's kept to show how a spec changes before anything is built. The contact form was dropped: it needs a server to receive messages, and that would break the decision to keep the site as plain files (`2-decisions/2026-11-13-ADR-001-plain-html-no-framework.md`).

## Goal

A personal website with a home page, an about page, and a contact form.

## Behavior

- A home page and an about page.
- A contact form that emails messages to the site's owner.

## Done when

- [ ] The pages open in a browser.
- [ ] A message sent through the form arrives by email.
