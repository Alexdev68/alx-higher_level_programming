#!/usr/bin/python3
"""This module contains a functions that appends text to file.
"""


def append_write(filename="", text=""):
    """This function appends a text to a file and returns the number of \
            characters appended.
    """
    with open(filename, 'a', encoding="UTF8") as io:
        no_chars = io.write(text)

    return no_chars
