#!/usr/bin/python3
"""This module contains a function that returns bool based on some conditions.
"""


def is_same_class(obj, a_class):
    """This function returns true if obj is an instance of class a_class.
    
    if a_class == object:
        return False
    if isinstance(obj, a_class):
        return True
    else:
        return False
    """
    return type(obj) is a_class
