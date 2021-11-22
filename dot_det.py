import numpy as np
x = np.random.rand(1000, 1)
y= np.random.rand(1000, 1)


np.dot(x.T,y, out=None)


# Replicate with for loop

prod = 0
for i in range(len(x)):
    prod += x[i] * y[i]

print((prod))


# Mtarix Determinant

matrix =[[-2,2,-3],[-1,1,3], [2,4, 3]]


np.linalg.det(matrix)



len(matrix)


def factor(r1, r2, r3):
    return [row[: r3] + row[r3+1:] for row in (r1[: r2] + r1[r2+1:])]

def Matrixdet(n):
 
    if(len(n) == 2):
        det = n[0][0] * n[1][1] - n[1][0] * n[0][1]
        return det
    add = 0

    for col in range(len(n)):
        matcofac = (-1) ** (col)
        submatdet = Matrixdet(factor(n, 0, col))
        add += (matcofac * n[0][col] * submatdet)
    return add


# This code is based on the code from Amit Mangal.[2]


Matrixdet(matrix)


# Reference:
# [1] https://www.kaggle.com/yushg123/for-loops-vs-vectorized-who-wins-and-by-how-much
# 
# [2] https://www.geeksforgeeks.org/determinant-of-a-matrix/
