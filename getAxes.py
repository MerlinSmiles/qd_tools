import os
import json

class getAxes():
    def __init__(self,path):
        self.path = path
        self.loadAxes()

    def loadAxes():
        pat = self.pathj
        metafile = os.path.join(path, 'meta.json')
        metaDatafile = os.path.join(path, 'data.json')
        with open(metafile) as json_data:
            meta = json.load(json_data)

        try:
            metaDatafile = os.path.join(path, 'data.json')
            with open(metaDatafile) as json_data:
                metaData = json.load(json_data)
        except IOError:
            metaDatafile = os.path.join(path, 'forward.json')
            with open(metaDatafile) as json_data:
                metaData = json.load(json_data)

        axes = []
        columnnumber = 0
        if 'sweeps' in meta:
            for i in meta['sweeps']:
                axes.append([{'label': i['chan'], 'from':i['from'], 'to':i['to'], 'points':i['points'], 'type':'sweep', 'id':columnnumber}])
                columnnumber += 1
        elif 'sweep' in meta:
            i = meta['sweep']
            axes.append([{'label': i['chan'], 'from':i['from'], 'to':i['to'], 'points':i['points'], 'type':'sweep', 'id':columnnumber}])
            columnnumber += 1

        for i in metaData[len(axes):]:
            axes.append([{'label': i['name'], 'type':'measure', 'id':columnnumber}])
            columnnumber += 1

        return axes
