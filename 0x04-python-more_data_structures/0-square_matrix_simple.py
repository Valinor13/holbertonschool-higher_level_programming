#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    neo = []
    if matrix == []:
        return None
    else:
        for i in range(len(matrix)):
            column = []
            for x in range(len(matrix[i])):
               column.append(matrix[i][x] * matrix[i][x])
            neo.append(column) 
        return neo
