#!/usr/bin/env python3
"""
pdf_to_markdown.py — Convert a PDF into a Markdown file with extracted images.

Usage:
    python pdf_to_markdown.py input.pdf [output_folder]

Produces:
    output_folder/
        <pdf_name>.md          # Markdown with text + image references
        images/                # Extracted images (PNG)

Dependencies:
    pip install pymupdf
    System: poppler-utils (provides pdftotext)  — optional, used as fallback

Filtering rules for images (tuneable below):
    - Skip images smaller than MIN_DIMENSION pixels on either side
      (filters out icons and decorative bits).
    - Skip images matching BANNER_FILTER (recurring page-header banner).
    - Deduplicate by xref so the same embedded image is saved only once.
"""

import argparse
import os
import re
import sys
from pathlib import Path

try:
    import fitz  # PyMuPDF
except ImportError:
    sys.exit("Missing dependency: install with  pip install pymupdf")


# ---- Tuneable filters --------------------------------------------------------

MIN_DIMENSION = 100          # px — skip images smaller than this on either side
BANNER_FILTER = {            # skip images matching ALL these size constraints
    "width_range":  (700, 760),   # typical recurring banner width
    "height_range": (130, 150),   # typical recurring banner height
}
# Set BANNER_FILTER = None to disable banner filtering.

# ------------------------------------------------------------------------------


def is_banner(width: int, height: int) -> bool:
    """Return True if image dimensions match the recurring banner filter."""
    if BANNER_FILTER is None:
        return False
    wmin, wmax = BANNER_FILTER["width_range"]
    hmin, hmax = BANNER_FILTER["height_range"]
    return wmin <= width <= wmax and hmin <= height <= hmax


def extract_images(doc: "fitz.Document", images_dir: Path) -> dict[int, list[str]]:
    """
    Extract images from the PDF, filtering out decorative/duplicate ones.

    Returns a dict mapping page_number (1-indexed) -> list of relative image paths,
    in the order they appear on that page.
    """
    images_dir.mkdir(parents=True, exist_ok=True)
    seen_xrefs: set[int] = set()
    page_images: dict[int, list[str]] = {}

    for page_num, page in enumerate(doc, start=1):
        per_page: list[str] = []
        page_idx = 0
        for img_info in page.get_images(full=True):
            xref = img_info[0]
            width = img_info[2]
            height = img_info[3]

            if width < MIN_DIMENSION or height < MIN_DIMENSION:
                continue
            if is_banner(width, height):
                continue
            if xref in seen_xrefs:
                continue
            seen_xrefs.add(xref)

            try:
                pix = fitz.Pixmap(doc, xref)
                if pix.n - pix.alpha > 3:           # CMYK → convert to RGB
                    pix = fitz.Pixmap(fitz.csRGB, pix)
                page_idx += 1
                filename = f"page{page_num:02d}_img{page_idx:02d}.png"
                pix.save(images_dir / filename)
                per_page.append(f"images/{filename}")
                pix = None  # release
            except Exception as err:
                print(f"  [warn] page {page_num} xref {xref}: {err}", file=sys.stderr)

        if per_page:
            page_images[page_num] = per_page

    return page_images


def extract_page_text(page: "fitz.Page") -> str:
    """
    Extract text from a page, lightly cleaned up.
    Collapses runs of blank lines and trims trailing whitespace per line.
    """
    raw = page.get_text("text")
    lines = [ln.rstrip() for ln in raw.splitlines()]
    cleaned: list[str] = []
    blank = False
    for ln in lines:
        if ln.strip():
            cleaned.append(ln)
            blank = False
        elif not blank:
            cleaned.append("")
            blank = True
    return "\n".join(cleaned).strip()


def build_markdown(doc: "fitz.Document",
                   page_images: dict[int, list[str]],
                   title: str) -> str:
    """Assemble the markdown document, interleaving text and image references per page."""
    parts: list[str] = [f"# {title}\n"]

    for page_num, page in enumerate(doc, start=1):
        parts.append(f"\n<!-- page {page_num} -->\n")
        text = extract_page_text(page)
        if text:
            parts.append(text)
            parts.append("")  # blank line after text

        for rel_path in page_images.get(page_num, []):
            stem = Path(rel_path).stem
            parts.append(f"![{stem}]({rel_path})")
            parts.append("")

    return "\n".join(parts).rstrip() + "\n"


def slugify(name: str) -> str:
    """Make a filesystem-safe slug from a string."""
    name = re.sub(r"[^\w\s-]", "", name).strip()
    name = re.sub(r"[\s_]+", "_", name)
    return name or "document"


def convert(pdf_path: Path, out_dir: Path) -> Path:
    """
    Convert pdf_path into a markdown file inside out_dir.
    Returns the path to the generated markdown file.
    """
    if not pdf_path.is_file():
        raise FileNotFoundError(pdf_path)

    out_dir.mkdir(parents=True, exist_ok=True)
    images_dir = out_dir / "images"

    print(f"Opening {pdf_path.name} …")
    doc = fitz.open(pdf_path)
    print(f"  {len(doc)} pages")

    print("Extracting images …")
    page_images = extract_images(doc, images_dir)
    total_imgs = sum(len(v) for v in page_images.values())
    print(f"  {total_imgs} images kept across {len(page_images)} pages")

    print("Building markdown …")
    title = pdf_path.stem.replace("_", " ")
    md = build_markdown(doc, page_images, title)

    md_path = out_dir / f"{slugify(pdf_path.stem)}.md"
    md_path.write_text(md, encoding="utf-8")
    print(f"  wrote {md_path}")

    doc.close()
    return md_path


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Convert a PDF into a Markdown file with extracted images."
    )
    parser.add_argument("pdf", type=Path, help="Path to the input PDF.")
    parser.add_argument(
        "out_dir",
        type=Path,
        nargs="?",
        default=None,
        help="Output folder (default: <pdf_stem>_md next to the PDF).",
    )
    args = parser.parse_args()

    out_dir = args.out_dir or args.pdf.with_name(f"{args.pdf.stem}_md")
    md_path = convert(args.pdf, out_dir)
    print(f"\nDone → {md_path}")


if __name__ == "__main__":
    main()
