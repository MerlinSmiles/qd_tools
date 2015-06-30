import numpy as np
from .scanDir import scanDir
from .readMeta import readMeta
from .loadAxes import loadAxes
from .getAxesNum import getAxesNum

def getData(path, label='', sort='', group=''):
    collection = []
    grouplist = []
    for index, i in enumerate(scanDir(path)):
        tmpmeta = readMeta(i['path'])
        tmpaxes = loadAxes(i['path'])
        # tmpdata = readData(i['path'])
        labelnum = getAxesNum(tmpaxes, label)

        sortval = None
        ignoreme = False
        if sort != '':
            if sort == 'Vbg':
                for j in tmpmeta["register"]["instruments"]:
                    if j["registered_name"] == "k1":
                        sortval = float(j['config']["sour_volt_lev"])

            if sort == 'phi' or sort == 'phiX':
                for j in tmpmeta["register"]["instruments"]:
                    if j["registered_name"] == "bsphere":
                        sortval = float(j['cached_values']["phi"]) * 180 / np.pi
                        theta = float(j['cached_values']["theta"])
                        if sort == 'phi' and abs(theta) == (90 or 270):
                            # print 'Now this is PhiX-data!'
                            ignoreme = True
                        if sort == 'phiX' and abs(theta) == (0 or 180):
                            # print 'Now this is Phi-data!'
                            ignoreme = True
                        # print sortval

            if sort == 'theta':
                for j in tmpmeta["register"]["instruments"]:
                    if j["registered_name"] == "bsphere":
                        sortval = float(j['cached_values']["theta"]) * 180 / np.pi
                        # print sortval
        else:
            sortval = '-'
        if ignoreme:
            continue
        if group != '':
            if group == 'Vbg':
                for j in tmpmeta["register"]["instruments"]:
                    if j["registered_name"] == "k1":
                        groupval = float(j['config']["sour_volt_lev"])

            if group == 'phi' or group == 'phiX':
                for j in tmpmeta["register"]["instruments"]:
                    if j["registered_name"] == "bsphere":
                        groupval = float(j['cached_values']["phi"]) * 180 / np.pi
                        theta = float(j['cached_values']["theta"])
                        if group == 'phi' and abs(theta) == 90:
                            # print 'Now this is PhiX-data!'
                            ignoreme = True
                        if group == 'phiX' and abs(theta) == 0:
                            # print 'Now this is Phi-data!'
                            ignoreme = True
                        # print groupval

            if group == 'theta':
                for j in tmpmeta["register"]["instruments"]:
                    if j["registered_name"] == "bsphere":
                        groupval = float(j['cached_values']["theta"]) * 180 / np.pi
                        # print groupval
        else:
            groupval = '-'

        if ignoreme:
            continue

        tmp = {'index': index,
               'sort': sort,
               'sortval': sortval,
               'groupval': groupval,
               'label': label,
               'labelnum': labelnum,
               'name': i['name'],
               'dir': i['dir'],
               'path': i['path'],
               'meta': tmpmeta,
               'axes': tmpaxes}
               # 'data': tmpdata}
        collection.append(tmp)
        if groupval not in grouplist:
            grouplist.append(groupval)
    collection = sorted(collection, key=lambda k: k['sortval'])
    if group != '':
        grouplist.sort()
        # grouplist = str(int(grouplist))
        collection = sorted(collection, key=lambda k: k['groupval'])

        returndata = collections.OrderedDict()
        for i in grouplist:
            returndata[i] = []

        for k, kk in enumerate(collection[::]):
            i = kk['groupval']
            returndata[i].append(kk)

        return returndata

    return collection
