from math import *
def sumOp(x):
    res = 0
    for xi in x:
        res += xi
    return res

def arrMult(x, y):
    res = []
    for i in range(len(x)):
        res.append(round(x[i] * y[i], 2))
    return res

def arrLn(x):
    res = []
    for xi in x:
        res.append(log(xi))
    return res

def powForArr(x,n):
    res = []
    for xi in x:
        res.append(xi ** n)
    return res

def matrixDet2(x):
    res = x[0][0] * x[1][1] - x[0][1] * x[1][0]
    return res

def matrixDet3(x):
    res = x[0][0] * x[1][1] * x[2][2] + x[0][1] * x[1][2] * x[2][0] + x[0][2] * x[1][0] * x[2][1] - x[0][2] * x[1][1] * x[2][0] - x[0][0] * x[1][2] * x[2][1] - x[0][1] * x[1][0] * x[2][2]
    return res