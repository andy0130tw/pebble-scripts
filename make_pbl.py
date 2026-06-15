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
  'cubic-14.pbf',
  'cubic-18.pbf',
  'cubic-18.pbf',
  'sarasa-24.pbf',
  'sarasa-24b.pbf',
  'sarasa-28.pbf',
  'sarasa-28b.pbf',
  # 'noto-28.pbf',
  # 'kuro-v5-regular/002-28px',
  # 'kuro-v5-light/002-24px',
  # 'kuro-v5-regular/005-24px',
  # 'kuro-v5-light/000-28px',
  # 'kuro-v5-regular/002-28px',
]

for res in ress:
    with open(res, 'rb') as f:
        pack.add_resource(f.read())

for _ in range(RES_SLOT_NUM - len(ress)):
    pack.add_resource(b'')

with open('cubic-sarasa-fauxbold64.pbl', 'wb') as out:
    pack.serialize(out)
