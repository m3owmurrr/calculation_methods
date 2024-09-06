# 19cos^2(Ф) + 2sin^2(Ф) = p^2

from numpy import *
from matplotlib.pyplot import *
from random import *

n = 8
A, B = 11 + n, 11 - n
a, b = 30, 30
N = 1000
Narr = [(randint(-1*a*10000, a*10000)/10000, randint(-1*b*10000, b*10000)/10000) for i in range(N)]

def p(f):
    return sqrt(A*((cos(f))**2) + B*((sin(f))**2))

def F(x, y):
    if x > 0:
        return arctan(y/x)
    elif x < 0:
        return arctan(y/x) + pi
    elif (x == 0 and y > 0):
        return pi/2
    elif (x == 0 and y < 0):
        return -1*(pi/2)
    elif (x == 0 and y == 0):
        return 0
M = 0
for dot in Narr:
    x, y = dot[0], dot[1]
    r = sqrt(x**2 +y**2)
    f = arctan(y/x)
    if (r < p(f)):
        M += 1

print((M/N)*4*a*b)
print(M)

f1 = linspace(0, 2*pi, 100)
r1_plus = []
for f in f1:
    r1_plus.append(p(f))

ax = subplot(111, projection='polar')
for dot in Narr:
    x, y = dot[0], dot[1]
    r = sqrt(x**2 + y**2)
    f = F(x, y)
    ax.scatter(r, f)

ax.plot(f1, r1_plus)
ax.grid(True)
legend(['f(x)'])
show()

# для повышения точности уеличиваем N, но график работать не будет