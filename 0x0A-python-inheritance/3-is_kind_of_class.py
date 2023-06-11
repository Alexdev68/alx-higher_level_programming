#!/usr/bin/python3
"""This module contains a function that return bool based on a condition.
"""


def is_kind_of_class(obj, a_class):
    """ This function returns True if obj is an instance of a_class else False.
    """
    return isinstance(obj, a_class)
