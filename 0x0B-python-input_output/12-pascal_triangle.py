#!/usr/bin/python3
"""This module contains a function that creates pascal's triangle based on n.
"""


def pascal_triangle(n):
    """This function creates pascal's triangle based on n.
    """
    dlist = []
    for i in range(n):
        row = [1]

        if i > 0:
            last_row = dlist[i - 1]

            for j in range(len(last_row) - 1):
                row.append(last_row[j] + last_row[j + 1])

            row.append(1)
        dlist.append(row)
    return dlist
