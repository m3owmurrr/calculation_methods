import math
from numpy import *

def gaussMethod(A, b):
    numOfEq = len(A)   #number of equations
    ATemp = A[:]
    bTemp = b[:]

    for i in range(0, numOfEq-1):
        maxEl = abs(ATemp[i][i])
        maxElNum = i
        for j in range(i+1, numOfEq):
            if (abs(ATemp[j][i]) > maxEl):
                maxEl = abs(ATemp[j][i])
                maxElNum = j

        temp = ATemp[i]
        ATemp[i] = ATemp[maxElNum]
        ATemp[maxElNum] = temp

        temp = bTemp[i]
        bTemp[i] = bTemp[maxElNum]
        bTemp[maxElNum] = temp

        for j in range(i+1, numOfEq):
            coef = ATemp[j][i] / ATemp[i][i]
            for k in range(0, numOfEq):
                ATemp[j][k] -= ATemp[i][k] * coef
            bTemp[j] -= bTemp[i] * coef

    for i in range(numOfEq-1, -1, -1):
        for j in range(i + 1, numOfEq):
            bTemp[i] -= ATemp[i][j]*bTemp[j]
        bTemp[i] /= ATemp[i][i]

    return bTemp

def residual(b, A, x0):
    numOfEq = len(A)
    res = [0 for i in range(numOfEq)]
    for i in range(numOfEq):
        for j in range(numOfEq):
            res[i] += A[i][j]*x0[j]
    for i in range(numOfEq):
        res[i] = b[i] - res[i]
    return res


A = [
      [0.0001, 1],
      [1, 2]
    ]
ab = [1, 4]


B = [
      [2.34, -4.21, -11.61],
      [8.04, 5.22, 0.27],
      [3.92, -7.99, 8.37]
    ]
bb = [14.41, -6.44, 55.56]


C = [
      [4.43, -7.21, 8.05, 1.23, -2.56],
      [-1.29, 6.47, 2.96, 3.22, 6.12],
      [6.12, 8.31, 9.41, 1.78, -2.88],
      [-2.57, 6.93, -3.74, 7.41, 5.55],
      [1.46, 3.62, 7.83, 6.25, -2.35]
    ]
cb = [2.62, -3.97, -9.12, 8.11, 7.23]


print(f'\nAnswer = {gaussMethod(A, ab)};')
print(f'Residual = {residual(ab, A, gaussMethod(A, ab))}')

print(f'\nAnswer = {gaussMethod(B, bb)};')
print(f'Residual = {residual(bb, B, gaussMethod(B, bb))}')

print(f'\nAnswer = {gaussMethod(C, cb)};')
print(f'Residual = {residual(cb, C, gaussMethod(C, cb))}')