
def getAxesNum(axes, label):
    labelnum = -1
    if label != '':
        for kindex, k in enumerate(axes):
            if k[0]['label'] == label:
                labelnum = kindex
    return labelnum