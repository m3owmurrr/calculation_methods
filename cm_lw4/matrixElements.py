def NotNullDiagonal(A, b):
    numOfEq = len(A)  # number of equations

    for i in range(0, numOfEq - 1):
        maxEl = abs(A[i][i])
        maxElNum = i
        for j in range(i + 1, numOfEq):
            if (abs(A[j][i]) > maxEl):
                maxEl = abs(A[j][i])
                maxElNum = j

        temp = A[i]
        A[i] = A[maxElNum]
        A[maxElNum] = temp

        temp = b[i]
        b[i] = b[maxElNum]
        b[maxElNum] = temp

def MatrixDiagonal(A):
    numOfEq = len(A)
    answ = [[0 for i in range(numOfEq)] for i in range(numOfEq)]
    for i in range(numOfEq):
        answ[i][i] = A[i][i]
    return answ

def MatrixDownTriangle(A):
    numOfEq = len(A)
    answ = [[0 for i in range(numOfEq)] for i in range(numOfEq)]
    for i in range(1, numOfEq):
        for j in range(0, i):
            answ[i][j] = A[i][j]
    return answ

def MatrixUpTriangle(A):
    numOfEq = len(A)
    answ = [[0 for i in range(numOfEq)] for i in range(numOfEq)]
    for i in range(0, numOfEq - 1):
        for j in range(i + 1, numOfEq):
            answ[i][j] = A[i][j]
    return answ