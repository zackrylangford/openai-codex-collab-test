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
4. The generated HTML files will appear in `site/`.

You can deploy the contents of `site/` to any static hosting service such as GitHub Pages.
