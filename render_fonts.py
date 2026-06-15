from collections import namedtuple
from fontgen import Font


MAX_GLYPHS_EXTENDED = 255 * 128
MAX_GLYPH_SIZE = 512

PbfSpec = namedtuple('PbfSpec', 'name maxh pxsize offs inp cpsrc bold')

specs = [
    PbfSpec('cubic-14.pbf',   14, 12,  0, 'Cubic_11.ttf',             'cubic11-cps.json', False),
    PbfSpec('cubic-18.pbf',   18, 12, -2, 'Cubic_11.ttf',             'cubic11-cps.json', False),

    PbfSpec('sarasa-24.pbf',  24, 19,  0, 'SarasaGothicTC-Light.ttf', 'cps-kuro.json',    False),
    PbfSpec('sarasa-24b.pbf', 24, 19,  0, 'SarasaGothicTC-Light.ttf', 'cps-kuro.json',    True),
    PbfSpec('sarasa-28.pbf',  28, 21,  0, 'SarasaGothicTC-Light.ttf', 'cps-kuro.json',    False),
    PbfSpec('sarasa-28b.pbf', 28, 21,  0, 'SarasaGothicTC-Light.ttf', 'cps-kuro.json',    True),
]

for spec in specs:
    print('spec', spec)
    name, maxh, pxsize, offs, inp, cpsrc, bb = spec

    f = Font(inp, pxsize, MAX_GLYPHS_EXTENDED, MAX_GLYPH_SIZE, False, max_height=maxh)

    f.set_codepoint_list(cpsrc)
    f.set_heightoffset(offs)
    if bb:
        f.set_fauxbold(True)

    f.build_tables()

    with open(name, 'wb') as out:
        out.write(f.bitstring())
