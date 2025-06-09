# Codex Collaboration Sandbox

This repository is a playground for collaborating with the Codex agent. It now includes a simple Python **static site generator** located in `static-site-generator/`.

Run `generate.py` to convert Markdown content into a static HTML site. Pages are
created from the Markdown files in `static-site-generator/content/` and
cross-linked via a simple navigation bar. A GitHub Actions workflow in
`.github/workflows/deploy.yml` builds the site and deploys it to **GitHub Pages**
whenever changes are pushed.

To enable deployment, activate GitHub Pages for this repository and choose the
"GitHub Actions" source. The workflow will publish the generated site
automatically.


Having trouble with this. 