import os
import json


def scanDir(scanPath):
    folderData = []
    for path, subFolders, files in os.walk(scanPath):
        # for i in subFolders:
        # if subFolders == []:
        #     subFolders = [path]
        for d in subFolders:
            # print d
            tmppath = os.path.join(path, d)

            if '.ignore' in os.listdir(tmppath):
                subFolders.remove(d)
                continue
            if '.ignore.txt' in os.listdir(tmppath):
                subFolders.remove(d)
                continue
            if 'ignore' in os.listdir(tmppath):
                subFolders.remove(d)
                continue

            if 'data.dat' and 'data.json' and 'meta.json' in os.listdir(tmppath):
                metafile = os.path.join(tmppath, 'meta.json')
                tmpmeta = []
                with open(metafile) as json_data:
                    tmpmeta = json.load(json_data)
                name = tmpmeta["name"]

                folderData.append({'name': name, 'dir': d, 'path': tmppath})
            elif 'forward.dat' and 'forward.json' and 'backward.dat' and 'backward.json' and 'meta.json' in os.listdir(tmppath):
                metafile = os.path.join(tmppath, 'meta.json')
                tmpmeta = []
                with open(metafile) as json_data:
                    tmpmeta = json.load(json_data)
                name = tmpmeta["name"]

                folderData.append({'name': name, 'dir': d, 'path': tmppath})

    if True:  # Reverse list
        folderData = folderData[::-1]
    return folderData