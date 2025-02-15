from numpy import pi

f = lambda k,x : 1.0/(k*(k+x))
f1 = lambda k : 1.0/k - 1.0/(k+1.0)

x = [i/10 for i in range(0, 11)]
answ = [pi*pi/6,
        1.53460724490456065438295871072,
        1.44087884154672282529652063816,
        1.36008258678244401658450305348,
        1.28957780079104178718959152009,
        1.22741127776021876233107151417,
        1.17210519612501518752085801324,
        1.12251934253575259612353753442,
        1.07775887274424300151901807116,
        1.03711091785065842203471019335,
        1]

e = 0.5 * 10**-8

for i in x:
    k = 1
    sum1 = 0
    sum2 = f(k, i)
    while abs(sum2 - sum1) > e:
        k += 1
        sum1 = sum2
        sum2 += f(k, i)
    print(f'x = {i}; k = {k}; f(x) = {sum2};')

print()

for i in x:
    k = 1
    sum1 = 0
    sum2 = f(k, i) - f1(k)
    while abs(sum2 - sum1) > e:
        k += 1
        sum1 = sum2
        sum2 += f(k, i) - f1(k)
    sum2 += 1.0
    print(f'x = {i}; k = {k}; f(x) = {sum2};')