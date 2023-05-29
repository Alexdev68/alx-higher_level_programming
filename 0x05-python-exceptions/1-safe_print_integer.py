#!/usr/bin/python3
def safe_print_integer(value):

    try:
        int_val = int(value)
    except ValueError:
        return False

    print("{:d}".format(int_val))
    return True
