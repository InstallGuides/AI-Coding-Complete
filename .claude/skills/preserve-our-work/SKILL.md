---
name: preserve-our-work
description: Save the session's progress so the next conversation can continue. Updates CHANGELOG.md and writes a handoff note in work-ledger/. Use when finishing a chunk of work, wrapping up, or when the user says "preserve our work" or "checkpoint this".
---

# Preserve our work

**Why this exists:** you don't remember past conversations, and your working memory fills up within a long one. The next conversation knows only what's written in this folder. So before you stop, save what you did and what's next.

Steps:

1. **Check today's date** with `date` first. A conversation can run past midnight.
2. **CHANGELOG.md:** add a dated bullet, newest first: one to three sentences on what changed and in which files, naming the spec. The reasoning goes in the handoff note.
3. **Handoff note:** add `work-ledger/YYYY-MM-DD-<short-slug>.md`. Start with a title and a one-sentence `**Summary:**`, then **what** you did, **decisions and paths not taken**, and **what's next**. Add a one-line link to it at the top of `work-ledger/index.md`.
4. **Tidy the plan:** tick finished items in the overview's roadmap and in `0-project-management/backlog.md`. Add any new ideas to the backlog.
5. If the project uses Git, offer to commit. Stage files by name (`git add <file>`), never `git add -A`. **Never commit secrets** (`.env` is git-ignored).

Write a handoff note for a *meaningful chunk* of work, not every tiny edit. A future conversation, or a different assistant, should be able to read it and continue cold.
