from numpy import *
from scipy import *


def sumOp(begin, limit, x, step, func):
    res = 0
    for i in range(begin, limit, step):
        res += func(x[i], 0)
    return res


def trapezoidMethod(func, a, b, n):
    h = (b - a) / n
    xarr = [round(i, 10) for i in arange(a, b, h)]
    xarr.append(b)
    return h * ((func(xarr[0], 0) + func(xarr[n], 0)) / 2 + sumOp(1, n, xarr, 1, func))


def middleRectangleMethod(func, a, b, n):
    h = (b - a) / n
    xarr = [round(i, 10) for i in arange(a, b, h)]
    return h * sumOp(0, n, [x + (h / 2) for x in xarr], 1, func)


def simpsonMethod(func, a, b, n):
    N = 2 * n
    h = (b - a) / N
    xarr = [round(i, 10) for i in arange(a, b, h)]
    xarr.append(b)
    return (h / 3) * (
            func(xarr[0], 0) + 2 * sumOp(2, N - 1, xarr, 2, func) + 4 * sumOp(1, N, xarr, 2, func) + func(xarr[n],
                                                                                                          0))


def splineMethods(func, a, b, n):
    h = 1 / n
    xarr = [round(i, 10) for i in arange(a, b, h)]
    farr = [round(func(x, 0), 10) for x in xarr]
    fansw = (interpolate.interp1d(xarr, farr, kind='cubic'))
    sum = 0
    for x in fansw(xarr):
        sum += x
    sum /= len(fansw(xarr))
    return sum


# для диффур
# считает дольше, но ооочень точный
def rungeKuttaMethod(func, x0, y0, X, n):
    x, y = x0, y0
    h = X / n
    for i in range(n):
        k1 = func(x, y)
        k2 = func(x + (h / 2), y + (h / 2) * k1)
        k3 = func(x + (h / 2), y + (h / 2) * k2)
        k4 = func(x + h, y + h * k3)

        y += (h / 6) * (k1 + 2 * k2 + 2 * k3 + k4)
        x += h
        x = round(x, 5)

    return x, y


def eulerMethod_forSystem(func1, func2, y10, y20, X, n):
    y1, y2 = [y10], [y20]
    h = X / n
    for i in range(n - 1):
        y1.append(y1[i] + h * func1(y1[i], y2[i]))
        y2.append(y2[i] + h * func2(y1[i], y2[i]))
    return y1, y2


def rungeKuttaMethod_forSystem(func1, func2, y10, y20, X, n):
    y1, y2 = [y10], [y20]
    h = X / n
    for i in range(n - 1):
        k11 = func1(y1[i], y2[i])
        k21 = func2(y1[i], y2[i])

        k12 = func1(y1[i] + (h / 2)*k11, y2[i] + (h / 2) * k21)
        k22 = func2(y1[i] + (h / 2)*k11, y2[i] + (h / 2) * k21)

        k13 = func1(y1[i] + (h / 2)*k21, y2[i] + (h / 2) * k22)
        k23 = func2(y1[i] + (h / 2)*k21, y2[i] + (h / 2) * k22)

        k14 = func1(y1[i] + h*k13, y2[i] + h * k23)
        k24 = func2(y1[i] + h*k13, y2[i] + h * k23)


        y1.append(y1[i] + (h / 6) * (k11 + 2 * k12 + 2 * k13 + k14))
        y2.append(y2[i] + (h / 6) * (k21 + 2 * k22 + 2 * k23 + k24))
    return y1, y2

