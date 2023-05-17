#!/usr/bin/python3
def uniq_add(my_list=[]):
    dlist = set(my_list)
    add = 0

    for i in dlist:
        add += i

    return add
