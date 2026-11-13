# PB-002: Publish the site with Netlify Drop

**Status:** ready (this example has never been published)
**Date:** 2026-11-13

A procedure you repeat each time you want the site online, or updated. It uses Netlify Drop, the simplest option in `1-research/2026-11-13-hosting-options.md`. Netlify's steps were checked in its documentation on 2026-11-13 (`https://docs.netlify.com/manage/projects/add-new-project/`). If a screen looks different, check that page again and update this playbook.

1. **Check the site first.** In a terminal in this folder, type `uv run scripts/check_site.py`. It must end with `All checks passed`.
2. **Make sure nothing private is in `site/`.** Everything in that folder becomes public.
3. **Sign in to Netlify** at `https://app.netlify.com/login`, or create a free account. Without an account, Netlify deletes a dropped site within an hour unless you claim it.
4. **Go to** `https://app.netlify.com/drop`.
5. **Drag the `site` folder** (the folder itself, not the whole project) from the Finder onto the drop zone.
6. **Open the address Netlify gives you**, ending in `netlify.app`, and click through both pages.
7. **To update the site later,** run the check again, open the site's page in Netlify, and drag the updated `site` folder onto it.
8. **Record it:** note the address and the date in `0-project-management/2026-11-13-PM-001-overview.md`, and add a line to `CHANGELOG.md`.

Your assistant can explain each step, but you do steps 3 to 6 yourself: they need your account, and they publish to the web.
