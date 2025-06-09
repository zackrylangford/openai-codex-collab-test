# Static Site Generator

This project is a minimal Python-based static site generator. It converts Markdown files in the `content/` directory into HTML files in `site/` using Jinja2 templates from `templates/`.

## Features
- Simple generation of static HTML pages
- Uses [Markdown](https://python-markdown.github.io/) for content
- Uses [Jinja2](https://jinja.palletsprojects.com/) templates for layout

## Usage
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Place Markdown files in the `content/` folder.
3. Run the generator:
   ```bash
   python generate.py
   ```
4. The generated HTML files will appear in the `site/` directory (ignored from version control).

### GitHub Pages Deployment

A workflow (`.github/workflows/deploy.yml`) is included to automatically build
the site and deploy it to **GitHub Pages**. Enable GitHub Pages in the repository
settings and select "GitHub Actions" as the source. Pushing changes to the
`work` branch will trigger the workflow and publish the updated site.
