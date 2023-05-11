#!/usr/bin/python3
def magic_calculation(a, b):
    from math import pow
    add, sub = magic_calculation_102.add, magic_calculation_102.sub

    if a < b:
        c = add(a, b)
        for i in range(4, 7):
            c = add(c, pow(sub(a, b), i))
        return c
    else:
        return sub(a, b)
