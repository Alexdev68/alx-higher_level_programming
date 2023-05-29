#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    j = 0

    try:
        for m in range(x):
            if type(my_list[m]) != int:
                continue
            print("{:d}".format(my_list[m]), end='')
            j += 1
        print()
    except OSError:
        raise IndexError("list index out of range")

    return j
