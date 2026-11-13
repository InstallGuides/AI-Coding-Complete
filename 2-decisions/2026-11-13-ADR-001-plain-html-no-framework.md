# ADR-001: Build the site with plain HTML and CSS, no framework

**Status:** accepted
**Date:** 2026-11-13

An ADR (architecture decision record) is a short note of a choice and why, so it isn't argued over again later.

## Decision

Write the site as plain HTML files and one CSS stylesheet in `site/`, with no framework, no JavaScript and no build step.

## Why

- Two pages don't need a framework. Plain files open in a browser with a double-click, so you can see every change at once.
- Nothing to install beyond what the check script uses (uv, which runs Python).
- Every host compared in `1-research/2026-11-13-hosting-options.md` publishes a plain folder as it is.

## Alternatives considered

- **A static-site generator or framework** (such as Astro or Eleventy): useful for many pages, but it adds Node, a build step and a folder of generated files.
- **A website builder service**: no files to learn from, and the site lives on someone else's platform.

## Consequences

Shared parts, such as the header and footer, are repeated in each page. If the site grows past a few pages, revisit this decision with a new ADR.
