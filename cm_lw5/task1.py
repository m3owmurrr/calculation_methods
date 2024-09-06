from matplotlib.pyplot import *
from numpy import *

f = lambda x: 1 / (1 + 25 * (x ** 2))

n = 100
x0 = -1

xi = [(x0 + i * (2 / n)) for i in range(0, n + 1)]
xi_cheb = [-cos(((2 * i - 1) / (2 * n)) * pi) for i in range(1, n + 1)]  # ?????????? почему -

yi = [f(xi[i]) for i in range(0, n + 1)]
yi_cheb = [f(xi_cheb[i]) for i in range(0, n)]

# print(xi, len(xi))
# print(xi_cheb, len(xi_cheb))
# print(yi, len(yi))
# print(yi_cheb, len(yi_cheb))

# Lagrange Interpolation Polynomial - LIP
def LIP_cheb(x):
    Lx = 0
    for i in range(0, n):
        lix = 1
        for j in range(0, n):
            if (i != j):
                lix *= (x - xi_cheb[j]) / (xi_cheb[i] - xi_cheb[j])
        Lx += lix * yi_cheb[i]
    return Lx

def LIP(x):
    Lx = 0
    for i in range(0, n + 1):
        lix = 1
        for j in range(0, n + 1):
            if (i != j):
                lix *= (x - xi[j]) / (xi[i] - xi[j])
        Lx += lix * yi[i]
    return Lx


Lxi = [LIP(xi[i]) for i in range(0, n + 1)]
Lxi_cheb = [LIP_cheb(xi_cheb[i]) for i in range(0, n)]

for i in range(0, n):
    print(xi_cheb[i], yi_cheb[i], Lxi_cheb[i])

for i in range(0, n + 1):
    print(xi[i], yi[i], Lxi[i])

plot(xi_cheb, Lxi_cheb, label='Lagrange Interpolation Polynomial')
plot(xi, Lxi, label='Lagrange Interpolation Polynomial')
legend()
show()


# opt = int(input())
# if (opt == 0):
#     plot(xi_cheb, Lxi_cheb, label='Lagrange Interpolation Polynomial')
#     plot(xi_cheb, yi_cheb, label='f(x)')
#     legend()
#     show()
# else:
#     plot(xi, Lxi, label='Lagrange Interpolation Polynomial')
#     plot(xi, yi, label='f(x)')
#     legend()
#     show()