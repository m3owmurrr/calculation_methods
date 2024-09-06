from numpy import *

s = lambda n : 1/(n**2+1)
s1 = lambda n : 1/((n**4)*(n**2+1))


e = 1 * 10**-10
ans = 1.07667404746858117413405079475

n = 1
sum1 = 0
sum2 = s(n)
while abs(sum2 - sum1) > e:
    n += 1
    sum1 = sum2
    sum2 += s(n)

print(f'n = {n}; s = {sum2};')

n = 1
sum1 = 0
sum2 = s1(n)
while abs(sum2 - sum1) > e:
    n += 1
    sum1 = sum2
    sum2 += s1(n)

print(f'n = {n}; s = {sum2 + pi**2/6 - pi**4/90};')

#если считать ошибку по элементам, то результат будет менее точный