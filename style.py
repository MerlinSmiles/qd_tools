import seaborn as sb
def style(mod = None):
    sb.set(font_scale=0.8)
    # sb.set_style("white")
    # sns.set_style("ticks")
    sb.set_style({'lines.linewidth': 0.3,
                   'axes.labelcolor': '.0',
                   'axes.linewidth': 0.5,
                   'axes.edgecolor': '.2',
                   'axes.facecolor': 'white',
                   'axes.grid': True,
                   'font.family': ['sans-serif'],
                   'font.sans-serif': ['Arial'],
                   'grid.linewidth': 0.5,
                   'grid.color': '.9',
                   'text.color': '.0',
                   'savefig.dpi': 100,
                   'xtick.color': '.0',
                   'ytick.color': '.0',
                   'xtick.color': '.0',
                   'xtick.direction': 'in',
                   'xtick.major.size': 3.0,
                   'xtick.minor.size': 1,
                   'xtick.major.width': 0.5,
                   'xtick.minor.width': 0.5,
                   'xtick.major.pad':3,
                   'ytick.color': '.0',
                   'ytick.direction': 'in',
                   'ytick.major.size': 3.0,
                   'ytick.minor.size': 1,
                   'ytick.major.width': 0.5,
                   'ytick.minor.width': 0.5,
                   'ytick.major.pad':3,
                   # 'axes.labelpad': 0.3,
                   'savefig.transparent': True,
                  })
    # sb.set_style( mod )
