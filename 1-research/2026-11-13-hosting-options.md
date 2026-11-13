# Ways to publish a small website with no build step

**Status:** done
**Date:** 2026-11-13

The site is a folder of plain HTML, CSS and one image, so it needs a host that publishes a folder as it is. These facts were checked in each host's documentation on 2026-11-13. Hosts change their terms, so check again before you rely on them.

| Host | How you publish the `site/` folder | Account | Address | Notes |
|---|---|---|---|---|
| Netlify Drop | Drag the folder onto `app.netlify.com/drop` | Free account to keep the site; without one, the site is deleted within an hour unless you claim it | `<name>.netlify.app` | The simplest. Drag a new folder onto the site's dashboard to update it. |
| Cloudflare Pages | In the dashboard, Workers & Pages, create an application, then drag and drop the folder or a `.zip` | Free account | `<name>.pages.dev` | A drag-and-drop project can't be switched to publishing from Git later. |
| GitHub Pages | Publish from a branch, but only from the repository's top folder or a `docs` folder | Free account; the repository on GitHub | `<user>.github.io/<repo>` | A site in `site/` needs a GitHub Actions workflow, or the folder renamed `docs`. |

**Sources:** Netlify, "Add new project" (`https://docs.netlify.com/manage/projects/add-new-project/`); Cloudflare, "Direct Upload" (`https://developers.cloudflare.com/pages/get-started/direct-upload/`); GitHub, "Configuring a publishing source for your GitHub Pages site" (`https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site`).

**What this means:** any of the three can host plain files. No host needs a framework or a build step, which supports keeping the site plain HTML (`2-decisions/2026-11-13-ADR-001-plain-html-no-framework.md`). Netlify Drop is the easiest first publish (`4-playbooks/2026-11-13-PB-002-publish-the-site.md`).
