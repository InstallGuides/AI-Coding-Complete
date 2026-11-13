---
name: new-spec
description: Start a new feature spec from the template in 3-specifications/, with a date and the next SPEC number. Use when the user wants to start a new spec, plan a feature, or "spec out" an idea from the backlog before building it.
---

# Start a new spec

When the user wants to plan a new feature:

1. Check today's date with `date`. Find the highest `SPEC-NNN` in `3-specifications/` and use the next number.
2. Copy `3-specifications/SPEC-template.md` to `3-specifications/YYYY-MM-DD-SPEC-<NNN>-<short-kebab-title>.md`, and fill in the Date line.
3. Fill in what you can from the user's request: Goal, Why, Behavior, Done when, Out of scope. Leave anything unclear as an explicit question.
4. **"Done when" must include a check you can run**, such as `uv run scripts/check_site.py` ending with `All checks passed`, plus anything else that shows the feature works.
5. Keep the Status at `draft`. If the idea came from `0-project-management/backlog.md`, link its line there to the new spec.
6. Show the draft and get the user's OK **before** building anything.

Spec first, build second.
