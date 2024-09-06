from math import *
from numMethods import *

print("====== TASK 1 ======\n")


f = lambda x, y: (2 / sqrt(pi)) * (exp(-1 * (x ** 2)))
n = 10000


def erf_my(x):
    if (x == 0.0):
        return 0.0
    a, b = 0.0, x
    return simpsonMethod(f, a, b, n)


xarr = [round(i, 10) for i in arange(0.0, 2.1, 0.1)]
for x in xarr:
    print(erf_my(x), erf(x))


print("\n====== TASK 2======\n")

f = lambda x, y: 4 / (1 + x ** 2)
n = 128


def pi_trapezoid():
    a, b = 0, 1
    return trapezoidMethod(f, a, b, n)


def pi_rectangle():
    a, b = 0, 1
    return middleRectangleMethod(f, a, b, n)


def pi_spline():
    a, b = 0, 1
    return splineMethods(f, a, b, n)




print(
    f'pi = {pi},\npi_spline() = {pi_spline()},\npi_rectangle() = {pi_rectangle()},\npi_trapezoid() = {pi_trapezoid()}')



print("\n====== TASK 3 ======\n")
n = 10000
a, b = 0, 4


def f(x, y = 0):
    if (x >= 0 and x <= 2):
        return e ** (x ** 2)
    elif (x > 2 and x <= 4):
        return 1 / (4 - sin(16 * pi * x))
    else:
        print('Out of range')
        return 0.0


corrAnsw = 16.969025545
print(
    f'correct answer = {corrAnsw},'
    f'\nsimpsonMethod = {simpsonMethod(f, a, b, n)}\tabs error = {abs(corrAnsw - simpsonMethod(f, a, b, n))},'
    f'\nmiddleRectangleMethod = {middleRectangleMethod(f, a, b, n)}\tabs error = {abs(corrAnsw - middleRectangleMethod(f, a, b, n))},'
    f'\ntrapezoidMethod = {trapezoidMethod(f, a, b, n)}\t\t\tabs error = {abs(corrAnsw - trapezoidMethod(f, a, b, n))}')
print('\nmost accurate is middleRectangleMethod')
