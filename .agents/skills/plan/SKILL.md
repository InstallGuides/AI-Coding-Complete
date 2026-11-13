---
name: plan
description: Capture or refresh the project's goals, roadmap and status in the 0-project-management overview, and keep backlog.md tidy. Use at the start of a project, when priorities change, or when the user has an idea or finds a bug that isn't ready to build.
---

# Plan the project

**When the user has a new idea or finds a bug:** add one line to `0-project-management/backlog.md`, with today's date (check it with `date`). Don't build it yet. Deciding comes later.

**When the user is starting out or rethinking direction:**

1. Open the overview in `0-project-management/` (the `…-PM-001-overview.md` file). If there's none, create one named `YYYY-MM-DD-PM-001-overview.md`.
2. Keep it brief: **what** the project is and who it's for, **why** it exists, a **roadmap** (a checklist of the next few specs), and the current **status**. Update its `**Date:**` line.
3. Read `backlog.md` with the user. For each item they decide to build, add it to the roadmap and link the line in the backlog to its spec once the spec exists.

Plan at the project level here. Detailed "what to build" for one feature belongs in a spec (`new-spec`).
