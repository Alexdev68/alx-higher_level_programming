#!/usr/bin/python3
"""This module writes to a file and encodes the text to be written using json.
"""
import json


def save_to_json_file(my_obj, filename):
    """This function writes a json encoding my_obj to a file as text due to \
            the encoding.
    """
    with open(filename, 'w', encoding="UTF8") as fp:
        fp.write(json.dumps(my_obj))
