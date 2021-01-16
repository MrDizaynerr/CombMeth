import matplotlib.pyplot as mat
import random as r
import math
import numpy as np
import interpolation as inter
from matplotlib.widgets import Slider

a = int(input('a = '))
b = int(input('b = '))
x0 = [x1 for x1 in np.arange(a, b, (b-a)/100)]
y = [math.tan(i) for i in x0]

y0 = [i + r.uniform(-(max(y)-min(y)), (max(y)-min(y))) for i in y]


# Find canonical form for line with two points got
def line_eq(x1, y1, x2, y2):
    return y1 - y2, x2 - x1, x1 * y2 - x2 * y1


# Find cross point for two lines, line:(x1,y1,x2,y2)
def cross_coords(line1, line2):
    A1, B1, C1 = line_eq(line1[0], line1[1],
                         line1[2], line1[3])
    A2, B2, C2 = line_eq(line2[0], line2[1],
                         line2[2], line2[3])
    A = np.array([[A1, B1], [A2, B2]])
    B = np.array([[-C1], [-C2]])
    C = np.linalg.inv(A) @ B
    return C[0][0], C[1][0]


def aver_method(x0, y0, k, n=1) -> [(float, float)]:
    result = []
    for i in range(0, len(x0) - k, n):
        x1 = sum(x0[i:i + k]) / k
        y1 = sum(y0[i:i + k]) / k
        result.append((x1, y1))
    return result


aver_res = aver_method(x0, y0, 6, 4)
x1 = [k[0] for k in aver_res]
y1 = [k[1] for k in aver_res]

fig, ax = mat.subplots()
mat.subplots_adjust(left=0.1, bottom=0.35)
p, = mat.plot(x0, y0, 'o')
d_default, = mat.plot(x0, y)
p2 = mat.plot(x1, y1, 'o')[0]
p3 = mat.plot(x0, y0)[0]
mat.axis([a-(b-a)/4, b+(b-a)/4, min(y0) - max(y0)/4, max(y0) + max(y0)/4])

axSliderK = mat.axes([0.1, 0.2, 0.8, 0.05])
slderk = Slider(axSliderK, 'K-value', valmin=2, valmax=len(x0), valstep=1, valinit=6)

axSliderN = mat.axes([0.1, 0.1, 0.8, 0.05])
sldern = Slider(axSliderN, 'N-value', valmin=1, valmax=len(x0), valstep=1, valinit=4)


def update_data(val):
    aver_res = aver_method(x0, y0, int(slderk.val), int(sldern.val))
    x1 = [k[0] for k in aver_res]
    y1 = [k[1] for k in aver_res]
    p2.set_xdata(x1)
    p2.set_ydata(y1)

    x3 = np.arange(x0[0]-x0[-1]//5, x0[-1]+x0[-1]//5, 0.1)
    y3 = inter.lagranzh(x3, x1, y1)
    p3.set_xdata(x3)
    p3.set_ydata(y3)


slderk.on_changed(update_data)
sldern.on_changed(update_data)

mat.show()
