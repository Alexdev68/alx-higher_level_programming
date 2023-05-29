#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    length = 0
    j = 0

    try:
        for i in my_list:
            length += 1
            if j < x:
                print(f"{my_list[j]}", end='')
                j += 1
        print()

    except IndexError:
        for m in range(length):
            print(f"{my_list[m]}", end='')
        print()

    return j
