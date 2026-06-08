import os
import sys

sys.path.append(os.path.join(os.environ['PEBBLE_SDK_PATH'], 'pebble/common/tools'))
sys.path.append(os.path.join(os.environ['PEBBLE_SDK_PATH'], 'pebble/common/waftools'))

from pbpack import ResourcePack
from resources.resource_map.resource_generator_font import FontResourceGenerator


pack = ResourcePack(is_system=False)

RES_SLOT_NUM = 19

ress = [
  'strings.mo',
  'huninn-14.pbf',
  'huninn-14-bold.pbf',
  'huninn-18.pbf',
  'huninn-18-bold.pbf',
  'huninn-24.pbf',
  'huninn-24-bold.pbf',
  'huninn-28.pbf',
  'huninn-28-bold.pbf',
]

for res in ress:
    with open(res, 'rb') as f:
        pack.add_resource(f.read())

for _ in range(RES_SLOT_NUM - len(ress)):
    pack.add_resource(b'')

with open('huninn.pbl', 'wb') as out:
    pack.serialize(out)
