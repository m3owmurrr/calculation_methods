from matplotlib.pyplot import *
from numpy import *
from myMathFuncs import *

# variant 8
x = [i for i in range(2, 18, 3)]
x_len = len(x)
y = [2.1, 1.3, 1.0, 0.9, 0.8, 0.72]

# example
# x = [i for i in range(1, 7)]
# x_len = len(x)
# y = [1.0, 1.5, 3.0, 4.5, 7.0, 8.5]

crutch = 0

# linear function method y = ax + b:
def linFunc(xGr):
    global crutch
    coef = [[sumOp(powForArr(x, 2)), sumOp(x)], [sumOp(x), x_len]]
    freePar = [sumOp(arrMult(x, y)), sumOp(y)]

    matrixA = coef[::1]
    matrixA[0] = freePar[::1]
    a = round(matrixDet2(matrixA) / matrixDet2(coef), 2)

    matrixB = coef[::1]
    matrixB[1] = freePar[::1]
    b = round(matrixDet2(matrixB) / matrixDet2(coef), 2)

    if (crutch > 3) :
        print(f'y = ({a})x + ({b})')
    crutch += 1

    answ = []
    for xi in xGr:
        answ.append(a*xi+b)
    return answ

# power function method y = b*x^a
def powFunc(xGr):
    global crutch
    X = arrLn(x)
    Y = arrLn(y)

    coef = [[sumOp(powForArr(X, 2)), sumOp(X)], [sumOp(X), x_len]]
    freePar = [sumOp(arrMult(X, Y)), sumOp(Y)]

    matrixA = coef[::1]
    matrixA[0] = freePar[::1]
    alpha = round(matrixDet2(matrixA) / matrixDet2(coef), 2)

    matrixB = coef[::1]
    matrixB[1] = freePar[::1]
    b = round(matrixDet2(matrixB) / matrixDet2(coef), 2)
    beta = round(exp(b), 2)

    if (crutch > 3):
        print(f'y = ({beta}) * x^({alpha})')
    crutch += 1

    answ = []
    for xi in xGr:
        answ.append(beta * xi**alpha)
    return answ

# exponential function method
def expFunc(xGr):
    global crutch
    Y = arrLn(y)

    coef = [[sumOp(powForArr(x, 2)), sumOp(x)], [sumOp(x), x_len]]
    freePar = [sumOp(arrMult(x, Y)), sumOp(Y)]

    matrixA = coef[::1]
    matrixA[0] = freePar[::1]
    alpha = round(matrixDet2(matrixA) / matrixDet2(coef), 2)

    matrixB = coef[::1]
    matrixB[1] = freePar[::1]
    b = round(matrixDet2(matrixB) / matrixDet2(coef), 2)
    beta = round(exp(b), 2)
    if (crutch > 3):
        print(f'y = ({beta}) * e^({alpha}x)')
    crutch += 1

    answ = []
    for xi in xGr:
        answ.append(beta * exp(alpha * xi))
    return answ


# quadratic function method
def quadFunc(xGr):
    global crutch
    coef = [[sumOp(powForArr(x, 4)), sumOp(powForArr(x, 3)), sumOp(powForArr(x, 2))], [sumOp(powForArr(x, 3)), sumOp(powForArr(x, 2)), sumOp(x)], [sumOp(powForArr(x, 2)), sumOp(x), x_len]]
    freePar = [sumOp(arrMult(powForArr(x, 2), y)), sumOp(arrMult(x, y)), sumOp(y)]

    matrixA = coef[::1]
    matrixA[0] = freePar[::1]
    a = round(matrixDet3(matrixA) / matrixDet3(coef), 2)

    matrixB = coef[::1]
    matrixB[1] = freePar[::1]
    b = round(matrixDet3(matrixB) / matrixDet3(coef), 2)

    matrixC = coef[::1]
    matrixC[2] = freePar[::1]
    c = round(matrixDet3(matrixC) / matrixDet3(coef), 2)

    if (crutch > 3):
        print(f'y = ({a})x^2 + ({b})x + ({c})')
    crutch += 1

    answ = []
    for xi in xGr:
        answ.append(a * xi**2 + b * xi + c)
    return answ


def check(yn):
    res = 0
    for i in range(len(y)):
        res += (y[i] - yn[i])**2
    return res



print(f'linFunc error = {check(linFunc(x))}')
print(f'powFunc error = {check(powFunc(x))}')
print(f'expFunc error = {check(expFunc(x))}')
print(f'quadFunc error = {check(quadFunc(x))}')
print()

xGraph = linspace(2, 17, 10000)

y1 = linFunc(xGraph)
y2 = powFunc(xGraph)
y3 = expFunc(xGraph)
y4 = quadFunc(xGraph)

scatter(x, y)
plot(xGraph, y1)
plot(xGraph, y2)
plot(xGraph, y3)
plot(xGraph, y4)
legend(['experimental points', 'linFunc', 'powFunc', 'expFunc', 'quadFunc'])
show()