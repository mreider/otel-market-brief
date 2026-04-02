#!/usr/bin/env python3
"""
Build a print-quality PDF from the market brief.

Setup:
  brew install pango
  pip install weasyprint beautifulsoup4 lxml

Usage:
  python pdf/build.py
"""

import os
import platform
from pathlib import Path

if platform.system() == "Darwin":
    brew_lib = "/opt/homebrew/lib"
    if os.path.isdir(brew_lib):
        os.environ.setdefault("DYLD_LIBRARY_PATH", brew_lib)

ROOT = Path(__file__).resolve().parent.parent
PDF_DIR = Path(__file__).resolve().parent


def build():
    from bs4 import BeautifulSoup, Comment
    import weasyprint

    html = (ROOT / "index.html").read_text()
    soup = BeautifulSoup(html, "html.parser")

    # Remove web-only elements
    for el in soup.find_all("footer"):
        el.decompose()
    for el in soup.find_all("div", class_="downloads"):
        el.decompose()

    # Remove HTML comments (em-dash dividers leak as visible text)
    for comment in soup.find_all(string=lambda t: isinstance(t, Comment)):
        comment.extract()

    # Swap the web stylesheet for the print one
    for link in soup.find_all("link", rel="stylesheet"):
        link.decompose()

    print_css = (PDF_DIR / "print.css").read_text()
    style_tag = soup.new_tag("style")
    style_tag.string = print_css
    soup.head.append(style_tag)

    # Darken SVG strokes/fills for print
    _remap = {
        "#e5e5e5": "#888", "#eee": "#aaa", "#ddd": "#777",
        "#d5d5d5": "#777", "#ccc": "#555", "#bbb": "#444",
        "#aaa": "#333", "#999": "#333", "#e0dcd6": "#c5c0b8",
        "#d9d4cc": "#b5b0a8", "#ccc6bc": "#a5a098", "#b8b0a5": "#8a8278",
        "#e8e4df": "#ccc8c2", "#d4cfc8": "#b0aba4",
    }
    for svg in soup.find_all("svg"):
        for el in svg.find_all(True):
            for attr in ("stroke", "fill"):
                val = (el.get(attr) or "").lower()
                if val in _remap:
                    el[attr] = _remap[val]
            sw = el.get("stroke-width")
            if sw:
                try:
                    el["stroke-width"] = str(max(float(sw) * 1.5, 0.6))
                except ValueError:
                    pass

    out = ROOT / "downloads" / "otel-market-brief.pdf"
    out.parent.mkdir(parents=True, exist_ok=True)

    doc = weasyprint.HTML(string=str(soup), base_url=str(ROOT))
    doc.write_pdf(str(out))
    print(f"  PDF → {out}")


if __name__ == "__main__":
    print("Building PDF...\n")
    build()
    print("\nDone.")
