---
name: run-playbook
description: Follow an existing playbook in 4-playbooks/, building a spec from its task list one task at a time, or running a repeated procedure. Use when the user says "build from PB-003", "run PB-002" or "follow the playbook".
---

# Execute a playbook

When asked to follow a playbook:

1. Read the named playbook in `4-playbooks/` (ask which one if it's unclear), and the spec and decisions it builds on.
2. Work through it in order. For a task list, do one task at a time: check it, tick its box, and tell the user before starting the next. For a procedure, show the user each step and its result. Pause if a step needs a decision from them, or their account.
3. **Before you tick any task that changes the site, run `uv run scripts/check_site.py`.** If it doesn't end with `All checks passed`, fix the problem first.
4. If reality differs from the playbook (a step is wrong, missing or out of date), tell the user and offer to update the playbook. If the spec itself is wrong, fix the spec and confirm with the user before you build.

When a task list is finished, check the work against the spec's "Done when" list, set the spec's Status to `done`, then offer to preserve the work.
