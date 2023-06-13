#!/usr/bin/python3
"""This module contains a function the inserts a string after every instance \
        of the search string.
"""


def append_after(filename="", search_string="", new_string=""):
    """This function inserts a string after every instance of the search \
            string.
    """
    with open(filename, 'r', encoding="UTF8") as f:
        lines = f.readlines()

    with open(filename, 'w', encoding="UTF8") as b:
        for line in lines:
            b.write(line)

            if search_string in line:
                b.write(new_string)
