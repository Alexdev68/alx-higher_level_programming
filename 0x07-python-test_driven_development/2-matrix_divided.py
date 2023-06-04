#!/usr/bin/python3
"""This module houses a function that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """This function divides all members of a matrix and stores them in a new
     matrix.

     Raises:
        TypeError: If the matrix is not a list of lists of integers or floats.
        It also raises if each row isn't the same size and if div isn't int.
        ZeroDivisionError: If div is equals to zero

    Returns:
        A new matrix with the calculated values
    """
    if not isinstance(matrix, list):
        raise TypeError('matrix must be a matrix (list of lists) '
                        'of integers/floats')

    for i in matrix:
        if not isinstance(i, list):
            raise TypeError('matrix must be a matrix (list of lists) '
                            'of integers/floats')
        if len(i) != len(matrix[0]):
            raise TypeError('Each row of the matrix must have the same size')
        for j in i:
            if not isinstance(j, (int, float)):
                raise TypeError('matrix must be a matrix (list of lists) '
                                'of integers/floats')
    new_mat = [[0] * len(matrix[0]) for b in range(len(matrix))]
    if not isinstance(div, (int, float)):
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')

    for g in range(len(matrix)):
        for h in range(len(matrix[0])):
            new_mat[g][h] = round((matrix[g][h] / div), 2)

    return new_mat
