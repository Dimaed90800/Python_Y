def transpose(matrix):
    matrix1=[]
    if matrix:
        for i in range(len(matrix[0])):
            matrix1.append([])
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                matrix1[j].append(matrix[i][j])
    matrix.clear()
    for elem in matrix1:
        matrix += [elem]