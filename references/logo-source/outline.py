"""Replace the wordmark <text> elements in the Antares lockups with outlined paths.

Usage: outline.py <space-grotesk.ttf> <host-grotesk.ttf> <out-dir> <svg>...
Layout matches SVG textLength + lengthAdjust="spacing": glyph advances at the
instanced weight, with the leftover width spread evenly across the gaps.
"""
import re, sys, pathlib
from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen

WEIGHT = 700
FONT_FOR_CLASS = {"antares": "space", "intel": "host"}

def load(path):
    f = TTFont(path)
    return instantiateVariableFont(f, {"wght": WEIGHT}) if "fvar" in f else f

def outline(font, text, x, y, size, length):
    upem = font["head"].unitsPerEm
    cmap, gs, hmtx = font.getBestCmap(), font.getGlyphSet(), font["hmtx"]
    names = [cmap[ord(c)] for c in text]
    s = size / upem
    advances = [hmtx[n][0] * s for n in names]
    gap = (length - sum(advances)) / (len(names) - 1)
    pen, cx = SVGPathPen(gs), x
    for n, adv in zip(names, advances):
        gs[n].draw(TransformPen(pen, (s, 0, 0, -s, cx, y)))
        cx += adv + gap
    return pen.getCommands()

TEXT_RE = re.compile(r'<text x="([\d.]+)" y="([\d.]+)" class="font-(antares|intel)[^"]*" font-size="([\d.]+)" fill="(#[0-9A-Fa-f]{6})"[^>]*textLength="([\d.]+)"[^>]*>([A-Z]+)</text>')
STYLE_RE = re.compile(r'\s*<style type="text/css">.*?</style>', re.S)

def main(space_path, host_path, out_dir, *svgs):
    fonts = {"space": load(space_path), "host": load(host_path)}
    out = pathlib.Path(out_dir)
    for p in map(pathlib.Path, svgs):
        src = p.read_text()
        def sub(m):
            x, y, kind, size, fill, length, text = m.groups()
            d = outline(fonts[FONT_FOR_CLASS[kind]], text, float(x), float(y), float(size), float(length))
            return f'<path aria-hidden="true" fill="{fill}" d="{d}"/>'
        body, count = TEXT_RE.subn(sub, src)
        if count != 2:
            sys.exit(f"{p.name}: expected 2 wordmark <text> elements, found {count}")
        body = STYLE_RE.sub("", body, count=1)
        body = body.replace('">\n  <defs>', '" role="img" aria-labelledby="title">\n  <title id="title">Antares Intelligence</title>\n  <defs>', 1)
        (out / p.name).write_text(body)
        print(f"{p.name}: outlined, {len(body)} bytes")

if __name__ == "__main__":
    main(*sys.argv[1:])
