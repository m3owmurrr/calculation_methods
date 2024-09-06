from time import *
from math import *
from numMethods import *
import matplotlib.pyplot as plt

print("Select task: ", end="")
ch = "2"
if (ch == "1"):
    print("\n\n===== TASK 1 =====")

    n = 10

    f = lambda x, y: (2 / sqrt(pi)) * exp(-1 * (x ** 2))


    def erf_my_integr(x):
        if (x == 0.0):
            return 0.0
        a, b = 0.0, x
        return simpsonMethod(f, a, b, n)


    def erf_my_diff(x):
        if (x == 0.0):
            return 0.0
        x0, y0 = 0, 0
        return rungeKuttaMethod(f, x0, y0, x, n)[1]


    xarr = [round(i, 10) for i in arange(0.0, 2.1, 0.1)]

    startTime = time()
    for x in xarr:
        erf_my_diff(x)
    endTime = time()
    print("diff time = ", endTime - startTime)

    startTime = time()
    for x in xarr:
        erf_my_integr(x)
    endTime = time()
    print("integr time = ", endTime - startTime)

    print()

    for x in xarr:
        print(erf_my_diff(x), erf_my_integr(x), erf(x))


else:

    print("\n\n===== TASK 2 =====")

    c = 2
    d = 1
    alpha = 0.01

    t0 = 0
    r0 = 10 # Начальная численность жертв
    f0 = 10 # Начальная численность хищников
    X = 1


    t = 100
    n = 100*t
    time = [i for i in arange(0, t, t/n)]

    difR = lambda r, f: 1 * r - alpha * r * f
    difF = lambda r, f: -2 * f + alpha * r * f

    r, f = rungeKuttaMethod_forSystem(difR, difF, r0, f0, t, n)
    # r, f = eulerMethod_forSystem(difR, difF, r0, f0, t, n)

    plt.figure(figsize=(12, 6))
    plt.plot(time, r, label='Численность кроликов (r)')
    plt.plot(time, f, label='Численность лис (f)')
    plt.xlabel('Время')
    plt.ylabel('Численность')
    plt.title('Модель Лотки-Вольтерры с изменениями')
    plt.legend()
    plt.grid(True)
    plt.show()