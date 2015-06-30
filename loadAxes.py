import os
import json
from .readMeta import readMeta

def loadAxes(path):

    metafile = os.path.join(path, 'meta.json')
    metaDatafile = os.path.join(path, 'data.json')
    jsonfile = os.path.join(path, 'data.json')

    meta = readMeta(path)

    # datafile = os.path.join(path, 'data.dat')

    # data = pd.read_csv(datafile,index_col = False, delimiter='\t',names = names)

    try:
        metaDatafile = os.path.join(path, 'data.json')
        with open(metaDatafile) as json_data:
            names = [x['name'] for x in json.load(json_data)]
    except IOError:
        metaDatafile = os.path.join(path, 'forward.json')
        with open(metaDatafile) as json_data:
            names = [x['name'] for x in json.load(json_data)]


    sweeps = [x['chan'] for x in meta['sweeps']]
    measures = names[len(sweeps):]
    # print(sweeps, measures)


    return sweeps, measures, sweeps+measures

