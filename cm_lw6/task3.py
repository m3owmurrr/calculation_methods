from numpy import *
from matplotlib.pyplot import *
from random import *

n = 8
R = n
N = 100000
Narr = [(randint(0, 2*R*10000)/10000, randint(0, 2*R*10000)/10000) for i in range(N)]

M = 0
for dot in Narr:
    x, y = dot[0], dot[1]
    if ((x-R)**2 + (y-R)**2 < R**2):
        M += 1

pi = 4*(M/N)
print(pi)


# Работает до +-1000 точек
# x1 = linspace(0, 2*R, 100)
# y1_plus = []
# y1_minus = []
# for x in x1:
#     y1_plus.append(sqrt(R**2 - (x-8)**2)+8)
#     y1_minus.append(-1*sqrt(R**2 - (x-8)**2)+8)
#
#
# for dot in Narr:
#     x, y = dot[0], dot[1]
#     scatter(x, y)
# plot(x1, y1_plus)
# plot(x1, y1_minus)
# legend(['f(x)'])
# show()