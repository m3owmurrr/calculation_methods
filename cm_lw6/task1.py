from random import *
from numpy import *
from matplotlib.pyplot import *

n = 8
a, b = 25, 25 # высота, ширина
N = 1000
Narr =  [(randint(0, b*10000)/10000, randint(0, a*10000)/10000) for i in range(N)]


def f(x):
    if (x >= 0 and x < n):
        return (10*x)/n
    elif (x >= n and x < 20):
        return 10*((x-20)/(n - 20))
    else:
        return 0

M = 0
for dot in Narr:
    x, y = dot[0], dot[1]
    if (y < f(x)):
        M += 1

S = (M/N)*a*b

print(S)

x1 = linspace(0, a, 100)
y1 = []
for x in x1:
    y1.append(f(x))

for dot in Narr:
    x, y = dot[0], dot[1]
    scatter(x, y)
plot(x1, y1)
legend(['f(x)'])
show()


# график работает при примерно 1000 точек, но тогда падает точность