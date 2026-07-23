#!/usr/bin/env python3
"""
build_pdf.py — Dark Squares Producer Package PDF Builder

Combines all Producer-Package section Markdown files into a single
professionally formatted PDF:
  DARK_SQUARES_TELEVISION_SERIES_PRODUCER_PACKAGE_v1.0.pdf

Requirements:
    pip install markdown weasyprint

Usage:
    python3 build_pdf.py

Output:
    DARK_SQUARES_TELEVISION_SERIES_PRODUCER_PACKAGE_v1.0.pdf
    DARK_SQUARES_PRODUCER_PACKAGE_SOURCE.md  (combined source)
"""

import os
import sys

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

REPO_ROOT = os.path.dirname(os.path.abspath(__file__))
PKG_DIR = os.path.join(REPO_ROOT, "Producer-Package")
OUTPUT_PDF = os.path.join(
    REPO_ROOT, "DARK_SQUARES_TELEVISION_SERIES_PRODUCER_PACKAGE_v1.0.pdf"
)
OUTPUT_MD = os.path.join(REPO_ROOT, "DARK_SQUARES_PRODUCER_PACKAGE_SOURCE.md")

SECTIONS = [
    "00_COVER.md",
    "01_CONFIDENTIALITY.md",
    "02_TABLE_OF_CONTENTS.md",
    "03_CREATOR_LETTER.md",
    "04_EXECUTIVE_OVERVIEW.md",
    "05_EXECUTIVE_ONE_SHEET.md",
    "06_SERIES_FACT_SHEET.md",
    "07_LOGLINE.md",
    "08_SERIES_SYNOPSIS.md",
    "09_CREATOR_BIOGRAPHY.md",
    "10_SERIES_CONCEPT.md",
    "11_TONE_THEMES_FORMAT.md",
    "12_SEASON_ONE_OVERVIEW.md",
    "13_SEASON_ONE_EPISODE_GUIDE.md",
    "14_PRINCIPAL_CHARACTERS.md",
    "15_SUPPORTING_CHARACTERS.md",
    "16_WORLD_LOCATIONS.md",
    "17_TIMELINE_CONTINUITY.md",
    "18_FUTURE_SEASONS.md",
    "19_PILOT_SAMPLE.md",
    "20_MANUSCRIPT_INVENTORY.md",
    "21_VISUAL_LOOKBOOK.md",
    "22_RIGHTS_CONTACT.md",
    "23_CLOSING.md",
]

# ---------------------------------------------------------------------------
# CSS Stylesheet
# ---------------------------------------------------------------------------

CSS = """
/* Page setup */
@page {
    size: letter;
    margin: 1.1in 1.0in 1.0in 1.0in;
    @bottom-center {
        content: "DARK SQUARES — Confidential Review Copy — © Alfred HJR. All Rights Reserved.";
        font-size: 7pt;
        color: #888;
        font-family: Arial, Helvetica, sans-serif;
    }
    @bottom-right {
        content: counter(page);
        font-size: 8pt;
        color: #555;
        font-family: Arial, Helvetica, sans-serif;
    }
}

/* Page break utility */
.page-break {
    page-break-after: always;
    break-after: page;
}

hr.page-break-hr {
    page-break-after: always;
    break-after: page;
    border: none;
    margin: 0;
}

/* Base typography */
body {
    font-family: Georgia, 'Times New Roman', Times, serif;
    font-size: 10.5pt;
    line-height: 1.6;
    color: #1a1a1a;
    background: #fff;
}

/* Headings */
h1 {
    font-family: Arial, Helvetica, sans-serif;
    font-size: 22pt;
    font-weight: bold;
    color: #0a0a0a;
    letter-spacing: 0.05em;
    text-transform: uppercase;
    margin-top: 0.6em;
    margin-bottom: 0.4em;
    border-bottom: 2px solid #1a2b4a;
    padding-bottom: 0.2em;
}

h2 {
    font-family: Arial, Helvetica, sans-serif;
    font-size: 15pt;
    font-weight: bold;
    color: #1a2b4a;
    letter-spacing: 0.03em;
    margin-top: 1.2em;
    margin-bottom: 0.3em;
}

h3 {
    font-family: Arial, Helvetica, sans-serif;
    font-size: 12pt;
    font-weight: bold;
    color: #3d3d3d;
    margin-top: 1.0em;
    margin-bottom: 0.2em;
}

h4 {
    font-family: Arial, Helvetica, sans-serif;
    font-size: 10.5pt;
    font-weight: bold;
    color: #3d3d3d;
    margin-top: 0.8em;
    margin-bottom: 0.2em;
}

/* Paragraphs */
p {
    margin: 0.5em 0;
    orphans: 3;
    widows: 3;
}

/* Blockquotes */
blockquote {
    border-left: 3px solid #1a2b4a;
    margin: 1em 1em 1em 0;
    padding: 0.5em 0 0.5em 1.2em;
    color: #2a2a2a;
    font-style: italic;
    font-size: 11pt;
    background: #f6f7fa;
}

blockquote p {
    margin: 0.2em 0;
}

/* Horizontal rules */
hr {
    border: none;
    border-top: 1px solid #c0c0c0;
    margin: 1.5em 0;
}

/* Tables */
table {
    border-collapse: collapse;
    width: 100%;
    margin: 1em 0;
    font-size: 9.5pt;
    font-family: Arial, Helvetica, sans-serif;
}

th {
    background: #1a2b4a;
    color: #c0c0c0;
    font-weight: bold;
    text-align: left;
    padding: 6px 10px;
    border: 1px solid #1a2b4a;
}

td {
    padding: 5px 10px;
    border: 1px solid #c0c0c0;
    vertical-align: top;
}

tr:nth-child(even) td {
    background: #f4f6fa;
}

/* Code blocks (screenplay dialogue) */
pre {
    background: #f4f4f4;
    border: 1px solid #ddd;
    border-left: 3px solid #1a2b4a;
    padding: 0.8em 1em;
    font-family: 'Courier New', Courier, monospace;
    font-size: 9pt;
    white-space: pre-wrap;
    word-wrap: break-word;
    page-break-inside: avoid;
    break-inside: avoid;
}

code {
    font-family: 'Courier New', Courier, monospace;
    font-size: 9pt;
    background: #f4f4f4;
    padding: 1px 3px;
}

/* Strong / emphasis */
strong {
    font-weight: bold;
    color: #0a0a0a;
}

em {
    font-style: italic;
}

/* Lists */
ul, ol {
    margin: 0.5em 0;
    padding-left: 1.5em;
}

li {
    margin: 0.2em 0;
}

/* Section dividers */
.section-divider {
    page-break-before: always;
    break-before: page;
}

/* Cover page special styling */
.cover-title {
    text-align: center;
    font-size: 36pt;
    font-weight: bold;
    letter-spacing: 0.1em;
    color: #0a0a0a;
    margin-top: 2in;
}

/* Screenplay formatting */
.scene-heading {
    font-weight: bold;
    text-transform: uppercase;
    font-family: 'Courier New', Courier, monospace;
}

.character-name {
    text-align: center;
    font-family: 'Courier New', Courier, monospace;
    font-weight: bold;
    text-transform: uppercase;
    margin-top: 1em;
}

.dialogue {
    margin: 0 2em;
    font-family: 'Courier New', Courier, monospace;
    font-size: 9.5pt;
}
"""

# ---------------------------------------------------------------------------
# Helper functions
# ---------------------------------------------------------------------------


def combine_sections() -> str:
    """Read and concatenate all section files."""
    parts = []
    parts.append(
        "<!-- DARK SQUARES PRODUCER PACKAGE SOURCE — v1.0 — Alfred HJR — "
        "Auto-assembled from Producer-Package/ sections -->\n"
    )
    for fn in SECTIONS:
        path = os.path.join(PKG_DIR, fn)
        if not os.path.exists(path):
            print(f"  WARNING: Section file not found: {path}", file=sys.stderr)
            continue
        with open(path, "r", encoding="utf-8") as f:
            content = f.read().strip()
        parts.append(content)
        # Insert a page break between sections (not after the last one)
        parts.append("\n\n---\n\n")

    return "\n\n".join(parts)


def markdown_to_html(md_text: str) -> str:
    """Convert Markdown to HTML."""
    try:
        import markdown as md_lib

        extensions = ["tables", "fenced_code", "nl2br"]
        return md_lib.markdown(md_text, extensions=extensions)
    except ImportError:
        # Fallback: use pandoc
        import subprocess
        import tempfile

        with tempfile.NamedTemporaryFile(
            mode="w", suffix=".md", delete=False, encoding="utf-8"
        ) as f:
            f.write(md_text)
            tmp = f.name
        result = subprocess.run(
            ["pandoc", "-f", "markdown", "-t", "html", tmp],
            capture_output=True,
            text=True,
        )
        os.unlink(tmp)
        if result.returncode != 0:
            raise RuntimeError(f"pandoc failed: {result.stderr}")
        return result.stdout


def build_full_html(body_html: str) -> str:
    """Wrap body HTML in a complete HTML document with CSS."""
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="author" content="Alfred HJR">
<meta name="subject" content="Dark Squares Television Series Producer Package v1.0">
<title>Dark Squares — Producer Package v1.0</title>
<style>
{CSS}
</style>
</head>
<body>
{body_html}
</body>
</html>"""


def generate_pdf(html_content: str, output_path: str) -> None:
    """Generate PDF from HTML using WeasyPrint."""
    try:
        from weasyprint import HTML

        print(f"  Generating PDF with WeasyPrint...")
        HTML(string=html_content).write_pdf(output_path)
        size_kb = os.path.getsize(output_path) // 1024
        print(f"  PDF written: {output_path} ({size_kb} KB)")
    except ImportError:
        raise RuntimeError(
            "WeasyPrint is not installed. Run: pip install weasyprint"
        )


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main():
    print("Dark Squares Producer Package — PDF Builder")
    print("=" * 60)

    # 1. Check section files
    missing = [s for s in SECTIONS if not os.path.exists(os.path.join(PKG_DIR, s))]
    if missing:
        print(f"WARNING: Missing section files: {missing}")

    if not os.path.isdir(PKG_DIR):
        print(f"ERROR: Producer-Package directory not found: {PKG_DIR}", file=sys.stderr)
        sys.exit(1)

    # 2. Combine sections into source document
    print("Step 1: Combining section files...")
    md_source = combine_sections()
    with open(OUTPUT_MD, "w", encoding="utf-8") as f:
        f.write(md_source)
    print(f"  Source written: {OUTPUT_MD}")

    # 3. Convert to HTML
    print("Step 2: Converting Markdown to HTML...")
    body_html = markdown_to_html(md_source)
    full_html = build_full_html(body_html)

    # 4. Generate PDF
    print("Step 3: Generating PDF...")
    generate_pdf(full_html, OUTPUT_PDF)

    print()
    print("=" * 60)
    print("BUILD COMPLETE")
    print(f"  PDF:    {OUTPUT_PDF}")
    print(f"  Source: {OUTPUT_MD}")
    print("=" * 60)


if __name__ == "__main__":
    main()
