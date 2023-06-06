#!/usr/bin/python3
"""This module houses a class ``LockedClass``.
"""


class LockedClass:
    """This class produces an AttributeError for every instance attribute \
            except first_name
    """

    __slots__ = ['first_name']
