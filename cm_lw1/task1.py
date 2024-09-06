import math
from numpy import *

erfSum = lambda x, n: ((-1)**n)*(x**(2*n+1))/(math.factorial(n)*(2*n+1))
def erf(x):
    n = 0
    sum1 = 0
    sum2 = erfSum(x, n)
    while (sum1 != sum2):
        n += 1
        sum1 = sum2
        sum2 += erfSum(x, n)
    return sum2 * 2/sqrt(pi)

x = [0.5, 1.0, 5.0]
for i in x:
    print(f'x = {i};   erf(x) = {erf(i)}')

#для 10 вычислить не получается, т.кк слишком большое значение