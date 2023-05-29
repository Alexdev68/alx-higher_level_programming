#!/usr/bin/python3
from sys import stderr


def safe_function(fct, *args):
    try:
        result = fct(*args)
        return result
    except (ZeroDivisionError, IndexError) as r:
        print("Exception: {}".format(str(r)), file=stderr)
        return None
