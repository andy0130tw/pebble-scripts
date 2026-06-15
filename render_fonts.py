from fontgen import Font

MAX_GLYPHS_EXTENDED = 255 * 128
MAX_GLYPH_SIZE = 512

specs = [
    ('24',      18, 5, False),
    ('24-bold', 18, 5, True),
    ('28',      21, 5, False),
    ('28-bold', 21, 5, True),
]
fauxbold = [False, True]

for spec in specs:
    print('spec', spec)
    name, px, offs, bb = spec

    f = Font(f'SarasaGothicTC-Light.ttf', px, MAX_GLYPHS_EXTENDED, MAX_GLYPH_SIZE, False)

    f.set_codepoint_list('cps-kuro.json')
    if bb:
        f.set_fauxbold(True)

    f.set_heightoffset(offs)

    f.build_tables()

    with open(f'noto-{name}.pbf', 'wb') as out:
        out.write(f.bitstring())
