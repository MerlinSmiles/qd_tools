from . import Map
import pandas as pd
import numpy as np
from scipy.interpolate import griddata

def imGrid(df,p,ny=1000,method='nearest'):
#     p = qd.Map(x='field', x_n='B [mT]', y='Idc', y_n='I [nA]', z='Vdc', z_n='4p Voltage [mV]', xm = 1e3, ym = 1e9, zm=1e3)
    if type(p)!=Map:
        raise

    grouped = df.groupby(p.x)
    nx = len(grouped)
    y_points = np.linspace(df[p.y].min(),df[p.y].max(),ny)
    grid = np.zeros((ny,nx))

    i = -1
    for label, data in grouped:
        i+=1
        dz = np.array(data[p.z])
        dy = data[p.y]
        interp = griddata(dy, dz, y_points, method=method)
        grid[:,i] = interp


    extent = [df[p.x].min()*p.xm, df[p.x].max()*p.xm,df[p.y].min()*p.ym,df[p.y].max()*p.ym]
    return grid*p.zm, extent

