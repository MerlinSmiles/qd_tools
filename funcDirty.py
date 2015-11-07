import scipy.constants as sc
import lmfit
from lmfit.model import Model
import numpy as np

# lphi    = params['lphi_%i' % i].value
# lso     = params['lso_%i' % i].value
# broad   = params['broad_%i' % i].value
# xoffset = params['xoffset_%i' % i].value
# yoffset = params['yoffset_%i' % i].value
# width   = params['width_%i' % i].value
# length  = params['length_%i' % i].value





def dirty_line(x, lphi, lso, broad, xoffset, yoffset, width, length):
    """Dirty Limit lineshape:
    lphi, lso, broad, xoffset, yoffset, width, length"""

    x = np.array(broad * (x + xoffset))

    lphi = lphi * 1E-9
    lso = lso * 1E-9

    dtb = (width ** 2 * sc.e ** 2 * x ** 2) / (3 * sc.hbar ** 2)

    br1 = (1.0 / (lphi ** 2) + 4.0 / (3.0 * (lso ** 2)) + dtb) ** (-0.5)
    br2 = (1.0 / (lphi ** 2) + dtb) ** (-0.5)

    dg = -((1.0) / (length)) * ((3.0 / 2.0) * br1 - (1.0 / 2.0) * br2)

    model = dg + yoffset
    return model


class DirtyModel(Model):
    __doc__ = dirty_line.__doc__
    def __init__(self, *args, **kwargs):
        super(DirtyModel, self).__init__(dirty_line, *args, **kwargs)
#         self.name = 'test'
#         self.set_param_hint('field', 0)
#         self.set_param_hint('fwhm', expr=fwhm_expr(self))

    def guess(self, data, x=None, **kwargs):
        if x is None:
            return
        ymin, ymax = min(data), max(data)
        xmin, xmax = min(x), max(x)
        offset = xmax - xmin
        pars = self.make_params()
        pars['%soffset' % self.prefix].set(value=np.mean(data))

        return lmfit.models.update_param_vals(pars, self.prefix, **kwargs)


#         pars = Model.make_params(self, )
#         return update_param_vals(pars, self.prefix, **kwargs)


