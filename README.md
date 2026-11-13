# Start here: AI-Coding-Complete

This folder is a full-size example of spec-driven development with an AI assistant: the method from AI-Coding-Lite, laid out for a project that runs for months. Its worked example is a small website you can make your own.

*Step 3 of 3: the same method at the size of a real project.*

## Open this folder with your AI assistant

- **Claude Desktop:** click **Code**, choose **Open folder…**, and pick this folder.
- **ChatGPT app (Codex):** click **Add new project**, choose this folder, and start a Codex chat.
- **Claude Code or Codex in a terminal:** open a terminal in this folder ([how](https://mac.install.guide/terminal/open)), then type `claude` or `codex`.

## Try it

1. Double-click `site/index.html` to see the site.
2. *"Let's make the site mine. Start a new spec for replacing the placeholder text."*
3. *"Write a playbook for SPEC-002, then build from it one task at a time."*
4. *"Preserve our work."*

## What's in here

- `0-project-management/`: the overview, and `backlog.md` for ideas and bugs.
- `1-research/`: what was learned before deciding.
- `2-decisions/`: decision records (ADRs).
- `3-specifications/`: what to build, and how you'll know it's done.
- `4-playbooks/`: plans and task lists, and procedures you repeat, such as publishing.
- `5-assets/`: images and draft text, staged before they go into the site.
- `6-outreach/`: announcements and messages about the project.
- `7-performance/`: measurements, such as page sizes.
- `8-archive/`: finished or replaced documents, kept but out of the way.
- `work-ledger/`: handoff notes, one per chunk of work.
- `site/`: the website. `scripts/`: the check. `CHANGELOG.md`: what changed, newest first.

## Why dates and IDs in file names

Files in folders 0, 2, 3 and 4 are named like `2026-11-13-ADR-001-plain-html-no-framework.md`. The date sorts files in the order they were written. The ID (`ADR-001`) never changes once another document mentions it, so references between documents stay clear.

## The loop

Write ideas and bugs in `0-project-management/backlog.md` first, and decide later what to build. Then each habit has a skill: **plan** (`plan`), **decide** (`new-decision`), **write a spec** (`new-spec`), **write a playbook** (`new-playbook`), **build from it** (`run-playbook`), and **preserve our work** (`preserve-our-work`). A task is done only when the check passes.

## Check the site

In a terminal in this folder, type `uv run scripts/check_site.py`. It checks that every page has a title and that every link and image works, prints each page's size, and ends with `All checks passed`. If the terminal says `command not found: uv`, [install uv](https://mac.install.guide/python/install-uv) first.

## The instruction files

`AGENTS.md` holds the instructions your assistant reads. `CLAUDE.md` is one line that points Claude to the same file, so edit `AGENTS.md` and leave `CLAUDE.md` alone.

## Keep going

- When you're happy with the site, publish it with `4-playbooks/2026-11-13-PB-002-publish-the-site.md`.
- Anything secret, such as an API key, goes in a file named `.env` in your home folder, never in this folder or in chat.

## Learn more

[Spec-Driven Development](https://mac.install.guide/ai/spec-driven-development/) and [Numbered Project Folders](https://mac.install.guide/project-files/numbered-folders) on Mac Install Guide.
