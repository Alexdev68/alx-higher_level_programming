#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_mat = []

    for i in range(len(matrix)):
        mat = list(map(lambda x: x**2, matrix[i]))
        new_mat.append(mat)

    return (new_mat)
