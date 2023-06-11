#!/usr/bin/python3
"""This module contains a function that returns bool based on conditions.
"""


def inherits_from(obj, a_class):
    """This fuction returns True if is an instance of a class that inherited \
            (directly or indirectly) from the specified class.
    """
    if a_class is type(obj):
        return False
    return isinstance(obj, a_class)
