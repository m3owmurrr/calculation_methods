# Нерабочая хуйня
from matplotlib.pyplot import *

f = lambda x: 1 / (1 + 25 * (x ** 2))

n = 100
x0 = -1
a, b, c, d = [],[],[],[]

x = [(x0 + i * (2 / n)) for i in range(0, n+1)]
y = [f(x[i]) for i in range(0, n+1)]

# Cubic Spline Coefficients
def CSC(x, y, n):
    h = [x[i+1] - x[i] for i in range(n)]
    a = [0] * n
    b = [0] * n
    c = [0] * (n + 1)
    for i in range(0, n):
        a[i] = y[i]
    l = [1] * n
    mu = [0] * n
    z = [0] * n
    for i in range(1, n):
        l[i] = 2.0 * (x[i+1] - x[i-1]) - h[i-1] * mu[i-1]
        mu[i] = h[i] / l[i]
        z[i] = (a[i] - h[i-1] * z[i-1]) / l[i]
    for i in range(n - 1, -1, -1):
        c[i] = z[i] - mu[i] * c[i+1]
        b[i] = (c[i+1] - c[i]) / (3.0 * h[i])
    d = [0] * n
    b = [0] * n
    a = [0] * n
    for i in range(n):
        d[i] = (c[i+1] - c[i]) / (3.0 * h[i])
        b[i] = (y[i+1] - y[i]) / h[i] - h[i] * (2.0 * c[i] + c[i+1]) / 3.0
        a[i] = y[i]
    return a, b, c, d

a, b, c, d = [],[],[],[]

# Cubic Spline Interpolation
def CSI(x_val, n):
    idx = 0
    while idx < n and x_val > x[idx + 1]:
        idx += 1
    dx = x_val - x[idx]
    y_val = a[idx] + b[idx] * dx + c[idx] * dx ** 2 + d[idx] * dx ** 3
    return y_val

a, b, c, d = CSC(x, y, n)
Sxi = [CSI(x[i], n) for i in range(0, n + 1)]

# for i in range(-100, 101):
#     print(i/100, f(i/100), CSI(i/100))
#
# plot(x, y, label='f(x)')
# plot(x, Sxi, label='Cubic Spline Interpolation')
# legend()
# show()


x = [2, 3, 5, 7]
y = [4, -2, 6, -3]
n = len(x) - 1

nn = 100
xx = [(2 + (7-2)/n*i) for i in range(0, nn)]
a, b, c, d = CSC(x, y, n)
Sxi = [CSI(xx[i], n) for i in range(0, nn-1)]

print(xx)

plot(x, y, label='y')
plot(xx, Sxi, label='Cubic Spline Interpolation')
legend()
show()