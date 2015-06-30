from .dataItem import dataItem
from .scanDir import scanDir
import os

class getFolder():
    def __init__(self, path, cleanup = False, st = None, ed = None):
        self.path = path
        self.cleanup = cleanup
        self.st = st
        self.ed = ed
        self.itemList = []
        self.folderList = []
        self.getFolderList()
        self.getItemList()

    def getItemList(self):
        self.itemList = []
        for i in self.folderList:
            # if '.ignore' in os.listdir(i['path']):
            #     self.folderList
            #     continue
            item = dataItem(i['path'])

            # if type(item.data) == type(None):
            #     print('continue')
            #     continue

            if self.cleanup:
                item.loadData()
                if type(item.data) == type(None):
                    print('continue')
                    continue
                self.cleanupItem(item)
            # print(item.data.columns)
            self.itemList.append(item)
        return self.itemList

    def getFolderList(self):
        self.folderList = scanDir(self.path)[self.st:self.ed]

    def item(self, num):
        return self.itemList[num]

    def cleanupItem(self, item):
        # print(item.data)
        columns = item.data.columns

        cAmp = item.meta['setup']['meta']['cAmp']
        if 'magnet/fld_as_amps' in columns:
            item.data.rename(columns=lambda x: x.replace('magnet/fld_as_amps', 'field'), inplace=True)
        if 'magnet/fld' in columns:
            item.data.rename(columns=lambda x: x.replace('magnet/fld', 'field'), inplace=True)
        if 'triton/MC' in columns:
            item.data.rename(columns=lambda x: x.replace('triton/MC', 'MC'), inplace=True)
        if 'Idc' in columns:
            item.data['Idc'] *= -cAmp
            item.data['dI'] = item.data['Idc'].diff()
        if 'Iac' in columns:
            item.data['Iac'] *= -cAmp
        if 'Vdc' in columns:
            item.data['Vdc'] /= 102.25
            item.data['dV'] = item.data['Vdc'].diff()
        if 'Vac' in columns:
            item.data['Vac'] /= 102.25
        if 'Vdc' and 'Idc' in columns:
            item.data['V/I']   = item.data['Vdc'] / item.data['Idc']
            item.data['I/V']   = 1.0/item.data['V/I']
        if 'Vac' and 'Iac' in columns:
            item.data['dV/dI'] = item.data['Vac'] / item.data['Iac']
            item.data['dI/dV'] = 1.0/item.data['dV/dI']

        # return item



    def __len__(self):
        return len(self.itemList)

    def __getitem__(self, arg):
            return self.itemList[arg]
