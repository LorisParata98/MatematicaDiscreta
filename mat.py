"""
Author : Giovanni Rasera
Revision : 0.0.1
Data : 2019 03 20
License : GNU Open Sourse

Implementation 0.0.0:
    scalar,
    __sub__,
    __pow__
    __add__,
    __mul__,
    get_elem,
    __str__,
    __eq__ ( == )
    STATIC:
        identity

SOLVED:
    0.0.1:
        Problem with switched indexes
"""
class Mat:
    #Matrix operations
    def __init__(self, mat):
        self.mat = mat        #Matrix

    #Return a new Matrix multiplied for the scalar
    #@Param scalar : int 
    def scalar(self, scalar):
        #Data
        m = len(self.mat)
        n = len(self.mat[0])
        newMatrix = []
        #Moltiplication Loop
        for i in range(0, m):
            row = []
            for j in range(0, n):
                #Scalr moltiplication operation
                row.append(self.mat[i][j]*scalar)
            newMatrix.append(row)
        return Mat(newMatrix)

    def __pow__(self, power):
        #Data
        m = len(self.mat)
        n = len(self.mat[0])
        #Checking data
        if m != n:
            raise Exception("EXC -- m and n must be the same")
        else:
            newMatrix = self.scalar(1)
            for i in range(0, power):
                newMatrix = self * newMatrix
            return newMatrix


    #SUB Matrix
    #@Param otherMatrix : mat class
    #Return Sub of matrices
    #Trows exception if indices do not match
    def __sub__(self, otherMatrix):
        return self + otherMatrix.scalar(-1)

    #ADD Matrix
    #@Param otherMatrix : mat class
    #Return the sum of matrix
    #Trows exception if indices do not match
    def __add__(self, otherMatrix):
        #Data
        m = len(self.mat)
        n = len(self.mat[0])
        other_m = len(otherMatrix.mat)
        other_n = len(otherMatrix.mat[0])
        newMatrix = []
        #Checking data
        if m == other_m and n == other_n:
            #Sum Loop
            for i in range(0, m):
                row = []
                for j in range(0, n):
                    #Sum
                    row.append(self.mat[i][j]+otherMatrix.mat[i][j])
                newMatrix.append(row)
            return Mat(newMatrix)
        else:
            raise Exception("EXC - Indices do not match (For a sum matrices must have same indices)")

    #Get element by id
    #@Param i, j : int
    #Return the value at i j : int
    #Trows Exceptions if i or j out of reange
    def get_elem(self,i, j):
        #Data
        m = len(self.mat)
        n = len(self.mat[0])
        #Checking data
        if i not in range(0, m) or j not in range(0, n):
            raise Exception("EXC - Indices are out of range")
        else:
            #Get element
            return self.mat[i][j]

    #Matrices multiplications
    #@Param otherMatrix : Matrix
    #Return : new Matrix that is the multiplication of the two
    #Trows : Exception if n not match with the other_m
    def __mul__(self, otherMatrix):
        #Data
        m = len(self.mat)
        n = len(self.mat[0])
        other_m = len(otherMatrix.mat)
        other_n = len(otherMatrix.mat[0])
        newMatrix = []
        #Checking data
        if n != other_m:
            raise Exception("EXC - n and other_m not matching")
        else:
            #Creating Empty Matrix
            for i in range(0, m):
                row = []
                for j in range(0, other_n):
                    #Inizialization
                    row.append(0)
                newMatrix.append(row)
            print(Mat(newMatrix))
            #Moltiplication
            for i in range(0, m):
                for j in range(0, other_n):
                    value_sum = 0
                    for k in range(0, n):
                        value_sum += (self.mat[i][k] * otherMatrix.mat[k][j])
                    newMatrix[i][j] = value_sum
            return Mat(newMatrix)

    #Return String Rappresentation
    def __str__(self):
        ret = ""
        m = len(self.mat)
        n = len(self.mat[0])
        for i in range(0, m):
            for j in range(0, n):
                ret += str(self.mat[i][j])+"  "
            ret+="\n"
        return ret

    #Equal? mothod
    #Use it with == 
    def __eq__(self, otherMatrix):
        #Data
        m = len(self.mat)
        n = len(self.mat[0])
        other_m = len(otherMatrix.mat)
        other_n = len(otherMatrix.mat[0])
        #Checking data
        if m != other_m or n != other_n:
            return False
        else:
            #Checking values
            for i in range(0, m):
                for j in range(0, n):
                    if self.mat[i][j] != otherMatrix.mat[i][j]:
                        return False
            return True

    # --- STATIC Methods:

    #Identity
    #@Param n : int dimensios
    #All 1 in the middle row
    #Return Mat Identity
    def identity(n):
        newMatrix = []
        for i in range(0, n):
            row = []
            for j in range(0, n):
                if j == i:
                    row.append(1)
                else:
                    row.append(0)
            newMatrix.append(row)
        return Mat(newMatrix)
    