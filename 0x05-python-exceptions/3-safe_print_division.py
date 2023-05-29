#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        return None
    finally:
        if b == 0:
            print("Inside result: None")
        else:
            print("Inside result: {}".format(result))

    return result
