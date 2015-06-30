import numpy as np
import pandas as pd
import types


def read_blocks(f, i=0, j=-1, columns=None):
    """
    http://stackoverflow.com/questions/10512026/reading-data-blocks-from-a-file-in-python
    """
    # # def myfunc(a,b, *args, **kwargs):
    # i = kwargs.get('i', 0)
    # j = kwargs.get('j', 1)

    if (type(f) == types.StringType or type(f) == types.UnicodeType ):
        fo = open(f, 'r')
        matrix = read_blocks(fo,i,j,columns=columns)
        fo.close()
        return matrix

    elif type(f) == types.FileType:
        # print i,j
        new_block = False
        blocks = [[]]
        blockcount = 0
        for line in f:
            line = line.replace('\r\n', '')
            line = line.replace('\n', '')
            line = line.replace('\r', '')
            # Check for empty/commented lines
            if not line or line.startswith('#'):
                new_block = True
                if blockcount == j:
                    break
                blockcount += 1
            # Non empty line: add line in current(last) block
            else:
                # If 1st one: new block
                if new_block == True and blocks[-1] != []:
                    blocks.append([])
                    new_block = False
                # print line.split()
                newline = map(float,line.split())
                # print(np.shape(newline))
                blocks[-1].append(np.array(newline))

        blocks = np.array(blocks)

        if blocks[-1] == []:
            np.delete(block,-1)
        frames = []
        for i in blocks:
            frames.append(pd.DataFrame(i,columns=columns))

        return pd.concat(frames)

    raise TypeError('f must be a file object or a file name.')