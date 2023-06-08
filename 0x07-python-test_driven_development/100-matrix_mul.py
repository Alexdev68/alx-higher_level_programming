#!/usr/bin/python3
"""This function houses a function that multiplies all members of a matrix.
"""


def matrix_mul(m_a, m_b):
    """This function performs various checks in order to get the best output.
    """
    if not isinstance(m_a, list):
        raise TypeError('m_a must be a list')
    if not isinstance(m_b, list):
        raise TypeError('m_b must be a list')
    if m_a == [] or m_a == [[]]:
        raise TypeError('m_a can\'t be empty')
    if m_b == [] or m_b == [[]]:
        raise TypeError('m_b can\'t be empty')

    for i, j in zip(m_a, m_b):
        if not isinstance(i, list):
            raise TypeError('m_a must be a list of lists')
        if not isinstance(j, list):
            raise TypeError('m_b must be a list of lists')
        if len(i) != len(m_a[0]):
            raise TypeError('each row of m_a must be of the same size')
        if len(j) != len(m_b[0]):
            raise TypeError('each row of m_b must be of the same size')

        for x, y in zip(i, j):
            if not isinstance(x, (int, float)):
                raise TypeError('m_a should contain only integers or floats')
            if not isinstance(y, (int, float)):
                raise TypeError('m_b should contain only integers or floats')

    if len(m_a[0]) != len(m_b):
        raise ValueError('m_a and m_b can\'t be multiplied')

    new_mat = [[0] * len(m_b[0]) for _ in range(len(m_a))]

    for a in range(len(m_a)):
        for b in range(len(m_b[0])):
            store = 0
            for r in range(len(m_b)):
                store += m_a[a][r] * m_b[r][b]
            new_mat[a][b] = store

    return new_mat
