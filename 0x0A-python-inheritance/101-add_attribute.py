#!/usr/bin/python3
"""This module contains a function that add a new attribute to a class.
"""


def add_attribute(sh_cls, sh_nam, sh_val):
    """This function checks if sh_cls is of any normal type then it raises an \
            exception.
        If it's type is not a normal type from that tuple then it adds the new\
                 attribute.
    """
    if not hasattr(sh_cls, "__dict__"):
        raise TypeError('can\'t add new attribute')

    setattr(sh_cls, sh_nam, sh_val)
