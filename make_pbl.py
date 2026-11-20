import os
import sys

sys.path.append(os.path.join(os.environ['PEBBLE_SDK_PATH'], 'pebble/common/tools'))
sys.path.append(os.path.join(os.environ['PEBBLE_SDK_PATH'], 'pebble/common/waftools'))

from pbpack import ResourcePack
# from resources.resource_map.resource_generator_font import FontResourceGenerator


pack = ResourcePack(is_system=False)

RES_SLOT_NUM = 19

ress = [
  'zh_TW/zh_TW.mo',
  'cubic-14.pbf',
  'cubic-14.pbf',  # TODO: no bold for now
  'shstw-18.pbf',
  'shstw-18b.pbf',
  'shstw-24.pbf',
  'shstw-24b.pbf',
  'shstw-28.pbf',
  'shstw-28b.pbf',
]

for res in ress:
    with open(res, 'rb') as f:
        pack.add_resource(f.read())

for _ in range(RES_SLOT_NUM - len(ress)):
    pack.add_resource(b'')

with open('cubic-shstw-beta3f-20261120.pbl', 'wb') as out:
    pack.serialize(out)
