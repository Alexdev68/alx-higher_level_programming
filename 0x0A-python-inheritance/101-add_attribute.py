#!/usr/bin/python3
"""This module contains a function that add a new attribute to a class.
"""


def add_attribute(sh_cls, name, value):
    """This function checks if sh_cls is of any normal type then it raises an \
            exception.
        If it's type is not a normal type from that tuple then it adds the new\
                 attribute.
    """
    if type(sh_cls) in (int, str, type(None), tuple, list, bool, float, dict,
                        set, complex, bytes, bytearray, memoryview, range,
                        frozenset, type):
        raise TypeError('can\'t add new attribute')

    else:
        setattr(sh_cls, name, value)
