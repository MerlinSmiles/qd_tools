import os
import json


def scanFolder(scanPath):
    scanPath = str(scanPath)
    # print scanPath
    if '.ignore' in os.listdir(scanPath):
        return False

    if 'ignore.txt' in os.listdir(scanPath):
        return False

    if 'ignore' in os.listdir(scanPath):
        return False

    if 'data.dat' and 'data.json' and 'meta.json' in os.listdir(scanPath):
        metafile = os.path.join(scanPath, 'meta.json')
        tmpmeta = []
        with open(metafile) as json_data:
            tmpmeta = json.load(json_data)
        name = tmpmeta["name"]
        folderData = {'name': name, 'path': scanPath}
    elif 'forward.dat' and 'forward.json' and 'backward.dat' and 'backward.json' and 'meta.json' in os.listdir(scanPath):
        metafile = os.path.join(scanPath, 'meta.json')
        tmpmeta = []
        with open(metafile) as json_data:
            tmpmeta = json.load(json_data)
        name = tmpmeta["name"]

        folderData = {'name': name, 'path': scanPath}
    else:
        return False

    return folderData
