import os
import json


def readMeta(path):
    metafile = os.path.join(path, 'meta.json')
    with open(metafile) as json_data:
        meta = json.load(json_data)
    if 'sweep' in meta:
        meta['sweeps'] = [meta['sweep']]
    return meta
