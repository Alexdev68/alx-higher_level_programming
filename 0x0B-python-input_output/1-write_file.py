#!/usr/bin/python3
"""This module contains a function the writes into a file.
"""


def write_file(filename="", text=""):
    """This function write into a file and returns the number of characters \
            written.
    """
    with open(filename, 'w', encoding="UTF8") as b:
        no_chars = b.write(text)

    return no_chars
