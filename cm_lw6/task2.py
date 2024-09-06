from numpy import *
from matplotlib.pyplot import *
from random import *

n = 8
a, b = 4, 5 # высота, ширина
N = 100
Narr =  [(randint(0, b*10000)/10000, randint(0, a*10000)/10000) for i in range(N)]

f = lambda x: sqrt(11-n*((sin(x))**2))

M = 0
for i in Narr:
    if (i[1] < f(i[0])):
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