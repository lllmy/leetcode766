def isToeplitzMatrix(matrix):
    m = len(matrix)
    n = len(matrix[0])
    for i in range(m-1):
        for j in range(n-1):
            if matrix[i][j] != matrix[i+1][j+1]:
                return False
    return True



print(isToeplitzMatrix([[1, 2, 3, 4], [5, 1, 2, 3], [9, 5, 1, 2]]))
print(isToeplitzMatrix([[1, 2], [2,2]]))
