from numpy import *

s1 = lambda k,x : 1/((k**3 + x)**(0.5))
s2 = lambda k,x : 1/((k**3 - x)**(0.5))
def s(x):
    k = 1
    sum1Plus = 0
    sum2Plus = s1(k, x)
    sum1Minus = 0
    sum2Minus = s2(k, x)
    while ((abs(sum2Plus - sum1Plus) > e) and (abs(sum2Minus - sum1Minus) > e)):
        k += 1
        sum1Plus = sum2Plus
        sum2Plus += s1(k, x)
        sum1Minus = sum2Minus
        sum2Minus += s2(k, x)
    print(f'x = {x};   s(x) = {sum2Plus - sum2Minus};   k = {k}')
def sFaster(x):
    k = 1
    sum1 = 0
    sum2 = s1(k, x) - s2(k, x)
    while (abs(sum2 - sum1) > e):
        k += 1
        sum1 = sum2
        sum2 += s1(k, x) - s2(k, x)
    print(f'x = {x};   s(x) = {sum2};   k = {k}')

e = 3*(10**(-8))
x = [x/10 for x in range(-9, 10)]

for i in x:
    s(i)
print('\n')

for i in x:
   sFaster(i)
print('\n')

s(0.5)
sFaster(0.5)
s(0.999999999)
sFaster(0.999999999)

# С помощью невероятных умственных процессов, было доказано, что ряды сходятся, честно честно
# С помощью эксперемента было получено 103575 для исходного метода и примерно 40 для ускоренного
# 500*2*103575 = 103575000мКс или 103575мс или 103с или 1,5мин
# Чтобы ускорить вычисление нужно объеденить вычисление рядов в 1 ряд