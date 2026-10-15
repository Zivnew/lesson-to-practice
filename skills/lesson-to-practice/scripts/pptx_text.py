"""Extract the text of every slide in a .pptx file, in slide order.

Usage: python pptx_text.py <lesson.pptx> <output.txt>

Uses only Python's standard library. Writes UTF-8, so non-Latin text
(Hebrew, Arabic, ...) is kept intact.
"""
import html
import re
import sys
import zipfile


def slide_number(name):
    return int(re.findall(r"\d+", name)[0])


def main(src, dest):
    with zipfile.ZipFile(src) as z:
        slides = sorted(
            (n for n in z.namelist() if re.match(r"ppt/slides/slide\d+\.xml$", n)),
            key=slide_number,
        )
        out = []
        for name in slides:
            xml = z.read(name).decode("utf-8")
            out.append(f"--- slide {slide_number(name)} ---")
            for para in re.findall(r"<a:p>(.*?)</a:p>", xml, re.S):
                text = html.unescape("".join(re.findall(r"<a:t>(.*?)</a:t>", para, re.S)))
                if text.strip():
                    out.append(text)
    with open(dest, "w", encoding="utf-8") as f:
        f.write("\n".join(out) + "\n")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit("Usage: python pptx_text.py <lesson.pptx> <output.txt>")
    main(sys.argv[1], sys.argv[2])
