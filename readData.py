import os
import json
import pandas as pd
# from .read_blocks import read_blocks


def readData(path, columns=None):

    try:
        datafile = os.path.join(path, 'data.dat')
        jsonfile = os.path.join(path, 'data.json')
        with open(jsonfile) as json_data:
            names = [x['name'] for x in json.load(json_data)]

        data = pd.read_csv(datafile, index_col=False, delimiter='\t', names=names)

        # with open(metaDatafile) as json_data:
            # data = read_blocks(datafile)[0]
    except IOError:
        datafile = os.path.join(path, 'forward.dat')
        jsonfile = os.path.join(path, 'forward.json')
        with open(jsonfile) as json_data:
            names = [x['name'] for x in json.load(json_data)]

        data = pd.read_csv(datafile, index_col=False, delimiter='\t', names=names)
        # with open(metaDatafile) as json_data:
            # data = read_blocks(datafile)[0]

    # datafile = os.path.join(path,'data.dat')
    # data = read_blocks(datafile)[0]
    return data
