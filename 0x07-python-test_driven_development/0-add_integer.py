#!/usr/bin/python3
"""
    This module contains a function that adds two integers.
    Example:
        add_integer(4, 5) returns 9
"""


def add_integer(a, b=98):
    """This function adds two integers.
        Returns:
            int: The addition of a and b."""
    if not isinstance(a, (int, float)):
        raise TypeError('a must be an integer')
    if not isinstance(b, (int, float)):
        raise TypeError('b must be an integer')
    if a > 1000000 or b > 1000000:
        raise ValueError('Float overflow')
    if not a > 0 and not a < 0 and type(a) is float:
        raise ValueError('cannot convert float NaN to integer')
    if not b > 0 and not b < 0 and type(b) is float:
        raise ValueError('cannot convert float NaN to integer')
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)

    return a + b
