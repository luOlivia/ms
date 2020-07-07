import os
import fnmatch
from evtxtoelk import EvtxToElk

matches = []
for root, dirnames, filenames in os.walk('EVTX-ATTACK-SAMPLES'):
    for filename in fnmatch.filter(filenames, '*.evtx'):
        matches.append(os.path.join(root, filename))

for file in matches:
    EvtxToElk.evtx_to_elk(file, "http://172.18.0.2:9200")
