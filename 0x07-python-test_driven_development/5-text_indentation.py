#!/usr/bin/python3
"""This module houses a function tha indents a text.
"""


def text_indentation(text):
    """This function indents a text due to the appearance of some characters.
    """
    if not isinstance(text, str):
        raise TypeError('text must be a string')

    if len(text) == 0:
        raise TypeError("text must not be empty")

    for no, i in enumerate(text):
        if i == '.':
            print(".")
            print()
            continue
        if i == '?':
            print("?")
            print()
            continue
        if i == ':':
            print(":")
            print()
            continue
        if text[no - 1] in ('.', '?', ':') and i == " " or i == "   ":
            continue
        print("{}".format(i), end='')
