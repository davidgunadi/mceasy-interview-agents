#!/usr/bin/env python3
"""Convert a markdown file (as produced by this repo's interview agents) to PDF.

Usage: md_to_pdf.py <input.md> <output.pdf>

Supports the subset of markdown used in _questions.md / questions.md / summary.md:
headers, bold, checkboxes, blockquotes, bullet lists, horizontal rules, and
pipe tables. Not a general-purpose markdown renderer.
"""
import re
import sys

from reportlab.lib import colors
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import (
    HRFlowable,
    ListFlowable,
    ListItem,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)

styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name="H1", fontSize=18, leading=22, spaceAfter=10, spaceBefore=4, fontName="Helvetica-Bold"))
styles.add(ParagraphStyle(name="H2", fontSize=14, leading=18, spaceAfter=8, spaceBefore=12, fontName="Helvetica-Bold"))
styles.add(ParagraphStyle(name="H3", fontSize=12, leading=16, spaceAfter=6, spaceBefore=10, fontName="Helvetica-Bold"))
styles.add(ParagraphStyle(name="Body", fontSize=10, leading=14, spaceAfter=6))
styles.add(ParagraphStyle(name="Quote", fontSize=10, leading=14, spaceAfter=6, leftIndent=14, textColor=colors.HexColor("#444444")))


def inline(text: str) -> str:
    text = text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    text = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", text)
    text = re.sub(r"`(.+?)`", r"<font face='Courier'>\1</font>", text)
    text = re.sub(r"\[[xX]\]", "<b>[X]</b>", text)
    return text


def parse_table(lines):
    rows = [[c.strip() for c in row.strip().strip("|").split("|")] for row in lines]
    if len(rows) > 1 and re.match(r"^:?-+:?$", rows[1][0].strip()):
        rows.pop(1)
    return [[Paragraph(inline(cell), styles["Body"]) for cell in row] for row in rows]


def build_flowables(md_text: str):
    flow = []
    lines = md_text.splitlines()
    i = 0
    n = len(lines)
    bullet_buf = []

    def flush_bullets():
        if bullet_buf:
            flow.append(
                ListFlowable(
                    [ListItem(Paragraph(inline(b), styles["Body"])) for b in bullet_buf],
                    bulletType="bullet",
                    leftIndent=16,
                )
            )
            bullet_buf.clear()

    while i < n:
        line = lines[i].rstrip()

        if not line.strip():
            flush_bullets()
            i += 1
            continue

        if line.strip() == "---":
            flush_bullets()
            flow.append(Spacer(1, 4))
            flow.append(HRFlowable(width="100%", color=colors.HexColor("#cccccc")))
            flow.append(Spacer(1, 4))
            i += 1
            continue

        if line.startswith("|"):
            flush_bullets()
            table_lines = []
            while i < n and lines[i].strip().startswith("|"):
                table_lines.append(lines[i])
                i += 1
            data = parse_table(table_lines)
            tbl = Table(data, hAlign="LEFT", repeatRows=1)
            tbl.setStyle(
                TableStyle(
                    [
                        ("GRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#bbbbbb")),
                        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#eeeeee")),
                        ("VALIGN", (0, 0), (-1, -1), "TOP"),
                        ("FONTSIZE", (0, 0), (-1, -1), 9),
                        ("LEFTPADDING", (0, 0), (-1, -1), 4),
                        ("RIGHTPADDING", (0, 0), (-1, -1), 4),
                    ]
                )
            )
            flow.append(tbl)
            flow.append(Spacer(1, 6))
            continue

        if line.startswith("### "):
            flush_bullets()
            flow.append(Paragraph(inline(line[4:]), styles["H3"]))
        elif line.startswith("## "):
            flush_bullets()
            flow.append(Paragraph(inline(line[3:]), styles["H2"]))
        elif line.startswith("# "):
            flush_bullets()
            flow.append(Paragraph(inline(line[2:]), styles["H1"]))
        elif line.startswith("> "):
            flush_bullets()
            flow.append(Paragraph(inline(line[2:]), styles["Quote"]))
        elif line.strip() == ">":
            flush_bullets()
            flow.append(Spacer(1, 4))
        elif line.startswith("- ") or line.startswith("* "):
            bullet_buf.append(line[2:])
        else:
            flush_bullets()
            flow.append(Paragraph(inline(line), styles["Body"]))

        i += 1

    flush_bullets()
    return flow


def main():
    if len(sys.argv) != 3:
        print("Usage: md_to_pdf.py <input.md> <output.pdf>", file=sys.stderr)
        sys.exit(1)

    src, dst = sys.argv[1], sys.argv[2]
    with open(src, encoding="utf-8") as f:
        text = f.read()

    doc = SimpleDocTemplate(
        dst,
        pagesize=LETTER,
        topMargin=0.75 * inch,
        bottomMargin=0.75 * inch,
        leftMargin=0.75 * inch,
        rightMargin=0.75 * inch,
    )
    doc.build(build_flowables(text))


if __name__ == "__main__":
    main()
