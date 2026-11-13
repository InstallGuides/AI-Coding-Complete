---
name: new-playbook
description: Write a playbook in 4-playbooks/, with a date and the next PB number. Usually a plan and task list from an agreed spec, for a fresh conversation to build from; sometimes a procedure the user repeats, such as publishing. Use when a spec is agreed and it's time to plan the build, or when the user has a task they'll do more than once.
---

# Write a playbook

A playbook is step-by-step instructions an assistant can follow without you in the room. There are two kinds, and both go in `4-playbooks/`:

- **A plan and task list from a spec**, the usual kind: a one-time handoff from the spec to the conversation that builds it.
- **A procedure you repeat**, such as publishing the site. Operations teams call this a runbook.

1. Check today's date with `date`. Find the highest `PB-NNN` in `4-playbooks/` and use the next number.
2. Create `4-playbooks/YYYY-MM-DD-PB-<NNN>-<short-kebab-title>.md`, starting with the title, then `**Status:**` and `**Date:**` lines.
3. **For a spec:** list the spec and its decisions under "Read first". Write a short plan (the approach, and which files change), then a checklist of small tasks in order. The last tasks are: run `uv run scripts/check_site.py`; tick the spec's "Done when"; preserve the work. Write no code yet.
4. **For a repeated procedure:** a numbered list of exact steps, with what success looks like. Mark any step the user must do themselves, such as signing in.
5. Write it so a fresh conversation that never saw this one could follow it cold.

When a plan and task list is ready, suggest starting a fresh conversation to build from it (the `run-playbook` skill).
