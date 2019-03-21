"""
Author : Giovanni Rasera
Revision : 0.0.1
Data : 2019 03 20
License : GNU Open Sourse

TESTING
"""
from mat import Mat

if __name__ == "__main__":
    n = [
        [4, 5, 3],
        [5, 7, 5],
        [2, 6, 6],
        [1, 3, 5]
    ]

    a = [
        [1,1],
        [1,0]
    ]
    b = [
        [2,1],
        [-1,1]
    ]
    c = [
        [0,2],
        [-2,1]
    ]
    d = [
        [2,1,3],
        [-2,0,1],
        [-2,0,1]
    ]

    N = Mat(n)
    A = Mat(a)
    B = Mat(b)
    C = Mat(c)
    D = Mat(d)

    print(A.scalar(-2) + B + C.scalar(2) - B.scalar(2))
    print(A ** 2)

    print(Mat.identity(2) * A)

    


    #print(A == A)
    
   # print(Mat.identity(30))