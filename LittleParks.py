import scipy.constants as sc
import lmfit
from lmfit.model import Model
import numpy as np


def LP_line(x, x_shift = 0, critical_temperature = 350, coherence_length = 700, radius = 280,
                width = 20, offset = 0):
    """Little Parks lineshape:
    LP_line(critical_temperature[mK], coherence_length[nm], radius[nm], field[mT], width[nm], offset)"""
    max_oscillations = 20
    critical_temperature = critical_temperature * 1e-3
    coherence_length = coherence_length * 1e-9
    radius = radius * 1e-9
    field  = abs(np.array(x)+x_shift) * 1e-3 #/ 10000
    width  = width * 1e-9
    a  = width / (2 * radius)

    pts = len(field)
    dd = np.zeros((pts,max_oscillations+1))
    dd[:,-1]=np.NaN
    for n in range(max_oscillations):
        nn = n / (1 + a**2)
        f0 = sc.h / (2 * sc.e)
        f = np.pi * radius**2 * field
        p1 = coherence_length**2 / radius**2
        p2 = (nn - f / f0)**2
        p3 = (1 + a**2)
        p4 = ((4/3) * nn**2 * a**2)
        d = critical_temperature * p1 * ( p2 * p3 + p4  )

        dd[:,n] = d
    for n in range(pts):
        dd[n,-1] = min(dd[n])

    return dd[:,-1] + offset

class LPModel(Model):
    __doc__ = LP_line.__doc__
    def __init__(self, *args, **kwargs):
        super(LPModel, self).__init__(LP_line, *args, **kwargs)
#         self.name = 'test'
#         self.set_param_hint('field', 0)
#         self.set_param_hint('fwhm', expr=fwhm_expr(self))

    def guess(self, data, x=None, **kwargs):
        if x is None:
            return
        ymin, ymax = min(data), max(data)
        xmin, xmax = min(x), max(x)
        offset = xmax - xmin
        pars = self.make_params(radius = 280,
                                width = 20)
        pars['%soffset' % self.prefix].set(value=np.mean(data))

        return lmfit.models.update_param_vals(pars, self.prefix, **kwargs)


#         pars = Model.make_params(self, )
#         return update_param_vals(pars, self.prefix, **kwargs)


