from numpy import *
from matrixElements import *
from matplotlib.pyplot import *

def Jacobi(x, b, L, U, revD):
    flag = True
    answ = x[::1]
    numOfEq = len(A)
    while (flag):
        xTemp = answ
        answ = revD.dot(b - (L + U).dot(answ))
        d = answ[0] - xTemp[0]
        for i in range(numOfEq):
            if ((answ[i] - xTemp[i] > d)):
                d = answ[i] - xTemp[i]
        if (d > err):
            flag = True
        else:
            flag = False
    return answ

def Jacobi_second(x, b, notD, D):
    numOfEq = len(A)
    xTemp = x[::1]
    answ = x[::1]
    flag = True
    counter = 1
    darr = []
    while (flag):
        for i in range(numOfEq):
            answ[i] = b[i]/D[i][i]
            for j in range(numOfEq):
                answ[i] -= (notD[i][j]/D[i][i])*xTemp[j]

        d = answ[0] - xTemp[0]
        for i in range(numOfEq):
            if ((answ[i] - xTemp[i] > d)):
                d = answ[i] - xTemp[i]

        if (d > err):
            flag = True
        else:
            flag = False

        xTemp = answ[::1]
        print(counter, d)
        darr.append(d)
        counter += 1
    print(answ)
    return darr

def Seidel(x, b, notD, D):
    numOfEq = len(A)
    answ = x[::1]
    xTemp = x[::1]
    flag = True
    counter = 1
    darr = []
    while (flag):
        for i in range(numOfEq):
            answ[i] = b[i] / D[i][i]
            for j in range(numOfEq):
                answ[i] -= (notD[i][j] / D[i][i]) * answ[j]

        d = answ[0] - xTemp[0]
        for i in range(numOfEq):
            if ((answ[i] - xTemp[i] > d)):
                d = answ[i] - xTemp[i]


        if (d > err):
            flag = True
        else:
            flag = False

        xTemp = answ[::1]
        print(counter, d)
        darr.append(d)
        counter += 1
    print(answ)
    return darr


err = 0.0001
A = [
    [12.14, 1.32, -0.78, -2.75],
    [-0.89, 16.75, 1.88, -1.55],
    [2.65, -1.27, -15.64, -0.64],
    [2.44, 1.52, 1.93, -11.43]
]
b = [14.78, -12.14, -11.65, 4.26]
x = [b[i] for i in range(len(A))]
# x = [1 for i in range(len(A))]

D = array(MatrixDiagonal(A))
revD = array(linalg.inv(D))
L = array(MatrixDownTriangle(A))
U = array(MatrixUpTriangle(A))


print(Jacobi(x, b, L, U, revD))
print("\n")

dJac = Jacobi_second(x, b, L+U, D)
print("\n")
dSeid = Seidel(x, b, L+U, D)
step1 = [i for i in range(1, len(dJac)+1)]
step2 = [i for i in range(1, len(dSeid)+1)]




plot(step1, dJac)
plot(step2, dSeid)
legend(['Jacobi', 'Seidel'])
show()
