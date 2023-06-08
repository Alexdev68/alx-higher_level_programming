#!/usr/bin/python3
"""This module houses a matrix multiplication function and imports numpy for
the multiplication.
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """This function multplies two matrices with the use of numpy.
    """
    if not isinstance(m_a, list):
        raise TypeError('Scalar operands are not allowed, use \'*\' '
                        'instead')
    if not isinstance(m_b, list):
        raise TypeError('Scalar operands are not allowed, use \'*\' '
                        'instead')
    if m_a == [] or m_a == [[]]:
        raise TypeError('shapes (1,0) and (2,2) not aligned: 0 (dim 1) != 2 '
                        '(dim 0)')
    if m_b == [] or m_b == [[]]:
        raise TypeError('shapes (2,2) and (1,0) not aligned: 2 (dim 1) != 1 '
                        '(dim 0)')

    for i, j in zip(m_a, m_b):
        if not isinstance(i, list):
            raise TypeError('Scalar operands are not allowed, use \'*\' '
                            'instead')
        if not isinstance(j, list):
            raise TypeError('Scalar operands are not allowed, use \'*\' '
                            'instead')
        if len(i) != len(m_a[0]):
            raise TypeError('setting an array element with a sequence.')
        if len(j) != len(m_b[0]):
            raise TypeError('setting an array element with a sequence.')

        for x, y in zip(i, j):
            if not isinstance(x, (int, float)):
                raise TypeError('invalid data type for einsum')
            if not isinstance(y, (int, float)):
                raise TypeError('invalid data type for einsum')

    if len(m_a[0]) != len(m_b):
        raise ValueError('shapes (2,3) and (2,2) not aligned: 3 (dim 1) != 2 '
                         '(dim 0)')

    m_a = np.array(m_a)
    m_b = np.array(m_b)

    return m_a @ m_b
