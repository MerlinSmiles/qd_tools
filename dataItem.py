from .readMeta import readMeta
from .loadAxes import loadAxes
from .readData import readData


class dataItem():
    def __init__(self, path):
        self.path = path
        self.cols = []
        self.readMeta()
        self.name = self.meta['name']
        self.loadAxes()
        self.data = None
        self.loaded = False

    def axNum(self, label):
        if label != '':
            self.cols = [c[0]['label'] for c in self.axes]
            labelnum = self.cols.index(label)
            return labelnum
        else:
            return None

    def readMeta(self):
        self.meta = readMeta(self.path)
        return self.meta

    def loadAxes(self):
        self.sweeps, self.measures, self.axes = loadAxes(self.path)
        return self.axes

    def loadData(self):
        self.data = readData(self.path, self.cols)
        return self.data

    def groupby(self, key):
        if self.loaded is False:
            self.loadData()
            self.loaded = True
        return self.data.groupby(key)

    def __getitem__(self, arg):
        if any((True for x in arg if x in self.cols)):
            if self.loaded is False:
                self.loadData()
                self.loaded = True
            return self.data[arg]
        return None
