from fontgen import Font
from itertools import product

MAX_GLYPHS_EXTENDED = 255 * 128
MAX_GLYPH_SIZE = 512

# sizes = [14, 18, 24, 28]
# fauxbold = [False, True]

# for sz, bb in product(sizes, fauxbold):
#     print('sz', sz, bb)
#     f = Font('jf-openhuninn-2.1.ttf', sz, MAX_GLYPHS_EXTENDED, MAX_GLYPH_SIZE, False)
#     suffix = '-bold' if bb else ''

#     if bb:
#         f.set_fauxbold(True)

#     f.set_codepoint_list('cps.json')

#     f.build_tables()
#     with open(f'huninn-{sz}{suffix}.pbf', 'wb') as out:
#         out.write(f.bitstring())

f = Font('Cubic_11.ttf', 12, MAX_GLYPHS_EXTENDED, MAX_GLYPH_SIZE, False)

f.set_codepoint_list('cubic11-cps.json')
f.set_heightoffset(3)

f.build_tables()
with open(f'cubic-offs.pbf', 'wb') as out:
    out.write(f.bitstring())
