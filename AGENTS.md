# Working in this project

This is **AI-Coding-Complete**, a full-size example of spec-driven development with an AI assistant. Its worked example is a two-page website in `site/`. The user may be new to coding. Help them keep the habit; it's the point of this folder.

## How to help here

- Explain what you're about to do in plain language before you do it, and work in small steps.
- Prefer the simplest thing that works. Don't introduce tools or frameworks unless asked.
- Ask before installing software, deleting files, or running anything that changes the system.
- Define any technical term the first time you use it.

## How this project works

You remember nothing between conversations, so the files here are the project's memory. Read the relevant ones before you act, and keep them current.

- **Backlog first.** Ideas and bugs go in `0-project-management/backlog.md`. Nothing is built until it has an agreed spec.
- **The loop:** plan (`plan`), decide (`new-decision`), write a spec (`new-spec`), write a playbook (`new-playbook`), build from it (`run-playbook`), preserve the work (`preserve-our-work`). Implement specs, nothing more. If a spec is wrong, fix it and confirm with the user, then build.
- **A task is done only when `uv run scripts/check_site.py` ends with `All checks passed`.**
- **File names** in `0-project-management/`, `2-decisions/`, `3-specifications/` and `4-playbooks/` are `YYYY-MM-DD-<ID>-NNN-slug.md`, with IDs `PM`, `ADR`, `SPEC` and `PB` and the next number in that folder. An ID never changes once cited. Other folders use `YYYY-MM-DD-slug.md`.
- **Documents** start with a title, then `**Status:**` and `**Date:**` lines.
- **Folders:** see the list in `README.md`. Handoff notes go in `work-ledger/`.
- **Changelog entries** are one to three sentences on what changed and in which files. The reasoning goes in the handoff note.
- **Dates:** check today's date with `date` before writing one.

## Before you change anything: Git

If this folder isn't under Git yet (it has no `.git` folder), offer to set it up before you change anything: run `git init` and make a first commit of the files as they are. Explain that a commit is a saved snapshot the user can go back to. Ask before each commit, stage files by name, and never commit a `.env` file. After each finished task, offer to commit.

## Tools on this Mac

Check what is installed (for example `uv --version`) before you install anything, and ask first.

## Secrets

API keys and other secrets go in the user's `~/.env` file, never in code, committed files or chat. This folder's `.gitignore` leaves out `.env` as a safety net.

## Keeping this file useful

This file is how you remember this project between conversations, so keep it short and current:

- **When the user corrects you on something that will come up again, offer to add one line here.** Write the rule, not the story behind it.
- **Keep it to a page or two.** Longer material goes in its own file, with one line here saying when to read it.
- **Before stopping mid-task, offer to write a handoff note** in `work-ledger/` (the `preserve-our-work` skill does this).
- **Write down facts that are easy to get wrong**, such as the site's address once published, as one line here with the date you checked.
