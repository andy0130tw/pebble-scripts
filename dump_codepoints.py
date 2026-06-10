import freetype

face = freetype.Face('Cubic_11.ttf')

cps = []

MAX_LATIN_CODEPOINT = 0x02AF
MIN_SYMBOLS_CODEPOINT = 0x2000
MAX_SYMBOLS_CODEPOINT = 0x2BFF
MIN_SPECIAL_CODEPOINT = 0xE0A0
MAX_SPECIAL_CODEPOINT = 0xE0A2

for cp, gidx in face.get_chars():
    if gidx == 0:
        break
    if cp <= MAX_LATIN_CODEPOINT or (cp >= MIN_SYMBOLS_CODEPOINT and cp <= MAX_SYMBOLS_CODEPOINT):
        continue
    if cp >= MIN_SPECIAL_CODEPOINT and cp <= MAX_SPECIAL_CODEPOINT:
        continue
    if cp >= 0x10000:
        continue
    cps.append(cp)

cps.sort()

import json
print(json.dumps({ 'codepoints': cps }))
