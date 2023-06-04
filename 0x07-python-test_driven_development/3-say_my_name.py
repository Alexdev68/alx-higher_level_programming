#!/usr/bin/python3
"""This module houses a function that prints a person's name.
"""


def say_my_name(first_name, last_name=""):
    """This prints first nam and last name depending on input
    """
    if not isinstance(first_name, str):
        raise TypeError('first_name must be a string')
    if not isinstance(last_name, str):
        raise TypeError('last_name must be a string')

    print("My name is {} {}".format(first_name, last_name))
