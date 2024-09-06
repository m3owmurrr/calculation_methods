import math
from numpy import *

erfSum = lambda x, n: ((-1) ** n) * (x ** (2 * n + 1)) / (math.factorial(n) * (2 * n + 1))
def erf(x):
    n = 0
    sum1 = 0
    sum2 = erfSum(x, n)
    while (sum1 != sum2):
        n += 1
        sum1 = sum2
        sum2 += erfSum(x, n)
    return sum2 * (2 / sqrt(pi))

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


A = [
        [1.00, 0.80, 0.64],
        [1.00, 0.90, 0.81],
        [1.00, 1.10, 1.21]
       ]
b = [erf(0.8), erf(0.9), erf(1.1)]
x = gaussMethod(A, b)

print(f'x1, x2, x3 = {x}')
print(f'x1 + x2 + x3 = {x[0] + x[1] + x[2]};   erf(1.0) = {erf(1.0)}\n')

print("\nОбусловленность матрицы - это мера того, насколько изменения входных данных (правых частей)\nсистемы линейных уравнений приводят к изменениям в решении. Если матрица плохо обусловлена,\nмаленькие изменения во входных данных могут привести к большим изменениям в выходных данных,\nчто делает решение неустойчивым.\n")
AСond = array(A)
print(f'Число обусловленности матрицы A = {linalg.cond(AСond)}\n\n')


A2 = [
    [0.1,0.2,0.3],
    [0.4,0.5,0.6],
    [0.7,0.8,0.9]
     ]
b2 = [0.1,0.3,0.5]
print("Если домножить первую строку на -2 и прибавить ко второй и домножить первую на -3 и прибавить к третьей, то получим, что 2 и 3 строки пропорциональны")
print("x2 = 2*x1, где x1 - любой коэффициент из R" + "   " + "x3 = (-x1 - 2*x2)/3")
print("Пример решения: " + str(gaussMethod(A2,b)))