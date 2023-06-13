#!/usr/bin/python3
"""This module contains a function that reads from a file.
"""


def read_file(filename=""):
    """This function reads from a file and prints out it's content.
    """
    with open(filename, 'r', encoding="UTF8") as d:
        read_info = d.read()

    print(read_info, end='')
