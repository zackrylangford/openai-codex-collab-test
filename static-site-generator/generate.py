import os
from pathlib import Path
import markdown
from jinja2 import Environment, FileSystemLoader

CONTENT_DIR = Path(__file__).parent / "content"
TEMPLATE_DIR = Path(__file__).parent / "templates"
OUTPUT_DIR = Path(__file__).parent / "site"


def load_markdown_files():
    pages = {}
    for md_file in CONTENT_DIR.glob("*.md"):
        with open(md_file, "r", encoding="utf-8") as f:
            text = f.read()
        html = markdown.markdown(text)
        name = md_file.stem
        pages[name] = html
    return pages


def build_site():
    env = Environment(loader=FileSystemLoader(TEMPLATE_DIR))
    template = env.get_template("base.html")

    pages = load_markdown_files()

    # Ensure output directory exists
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # Prevent GitHub Pages from running Jekyll
    (OUTPUT_DIR / '.nojekyll').touch()

    for name, html in pages.items():
        rendered = template.render(title=name.title(), content=html, pages=pages.keys())
        with open(OUTPUT_DIR / f"{name}.html", "w", encoding="utf-8") as f:
            f.write(rendered)

    print(f"Generated {len(pages)} page(s) in {OUTPUT_DIR}")


if __name__ == "__main__":
    build_site()
