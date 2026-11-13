"""Check the website in site/ (SPEC-001's "Done when").

Run it in a terminal in this project's folder:

    uv run scripts/check_site.py

For every .html page in site/, it checks that the page has a title and that
every link and image inside the site exists. Then it prints each page's size,
counting the images and stylesheet the page loads. It ends with
"All checks passed", or lists each problem and exits with an error.
"""

from html.parser import HTMLParser
from pathlib import Path
import sys

SITE = Path(__file__).resolve().parent.parent / "site"


class PageReader(HTMLParser):
    """Collects a page's title and the files it links to."""

    def __init__(self):
        super().__init__()
        self.title = ""
        self.in_title = False
        self.links = []

    def handle_starttag(self, tag, attrs):
        if tag == "title":
            self.in_title = True
        for name, value in attrs:
            if name in ("href", "src") and value:
                self.links.append(value)

    def handle_endtag(self, tag):
        if tag == "title":
            self.in_title = False

    def handle_data(self, data):
        if self.in_title:
            self.title += data


def is_inside_site(link):
    """True for links to files in this site; false for web addresses and page anchors."""
    return not link.startswith(("http://", "https://", "mailto:", "#", "//"))


def main():
    problems = []
    sizes = []
    pages = sorted(SITE.glob("*.html"))
    if not pages:
        problems.append("no .html pages found in site/")
    for page in pages:
        reader = PageReader()
        reader.feed(page.read_text(encoding="utf-8"))
        name = page.name
        if not reader.title.strip():
            problems.append(f"{name}: has no <title>")
        total = page.stat().st_size
        counted = set()
        for link in reader.links:
            if not is_inside_site(link):
                continue
            target = (page.parent / link.split("#")[0]).resolve()
            if not target.exists():
                problems.append(f"{name}: '{link}' doesn't exist")
            elif target.suffix != ".html" and target not in counted:
                counted.add(target)
                total += target.stat().st_size
        sizes.append((name, total))

    print("Page sizes, counting the images and stylesheet each page loads:")
    for name, total in sizes:
        print(f"  {name:<12} {total / 1024:6.1f} KB")
    if problems:
        print("Problems:")
        for p in problems:
            print(f"  {p}")
        sys.exit(1)
    print("All checks passed")


if __name__ == "__main__":
    main()
