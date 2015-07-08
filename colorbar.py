import mpltools#.color as color
import matplotlib.colors as mcolors
import matplotlib#.cm as cm
import matplotlib.pyplot as plt
import numpy as np

def colorbar(nvalues,nticks=None,cmap='gnuplot', start=0.1, stop=0.8,strmap = '%.3f', shrink=1, aspect=20):
    ncolors = len(nvalues)
    if nticks==None:
        nticks = ncolors
    colors = mpltools.color.colors_from_cmap(ncolors, cmap=cmap, start=start, stop=stop)
    cmap, norm = mcolors.from_levels_and_colors(range(ncolors + 1), colors)
    mappable = matplotlib.cm.ScalarMappable(cmap=cmap)
    mappable.set_array([])
    mappable.set_clim(-0.5, ncolors+0.5)
    colorbar = plt.colorbar(mappable,shrink=shrink,aspect=aspect)
    tickpos = np.linspace(0, ncolors,nticks)
    tickvalues = np.linspace(min(nvalues), max(nvalues), nticks)
    tickvalues = [strmap%f for f in tickvalues]
    colorbar.set_ticks(tickpos)
    colorbar.set_ticklabels(tickvalues)
    return colorbar
