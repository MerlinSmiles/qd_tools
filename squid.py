import scipy.constants as sc
import lmfit
from lmfit.model import Model
import numpy as np


def SQUID_line(x, x_shift = 0, critical_current = 300, radius = 280, offset = 0):
    """Little Parks lineshape:
    SQUID(field[mT], critical_current[nA], radius[nm], offset)"""
    critical_current = critical_current * 1e-3
    radius = radius * 1e-9
    field  = abs(np.array(x)+x_shift) * 1e-3 #/ 10000
    f0 = sc.h / (2 * sc.e)
    f = np.pi * radius**2 * field

    d = 2*critical_current * np.abs(np.cos(np.pi*(f/f0)))

    return d + offset

class SQIDModel(Model):
    __doc__ = SQUID_line.__doc__
    def __init__(self, *args, **kwargs):
        super(SQIDModel, self).__init__(SQUID_line, *args, **kwargs)
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


