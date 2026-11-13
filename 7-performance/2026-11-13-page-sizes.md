# Page sizes

**Status:** measured
**Date:** 2026-11-13

Measured with `uv run scripts/check_site.py` when SPEC-001 was built. Each size counts the page plus the stylesheet and image it loads.

| Page | Size |
|---|---|
| `about.html` | 2.1 KB |
| `index.html` | 1.9 KB |

Small pages load fast, even on a slow phone connection; a typical photo is 200 KB or more on its own. Measure again after a change that adds images, and add a dated row here so you can see the trend.
