#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):

    for i in matrix:
        for j, el in enumerate(i):
            if j == len(i) - 1:
                print("{:d}".format(el), end='')
            else:
                print("{:d} ".format(el), end='')
        print()
