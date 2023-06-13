#!/usr/bin/python3
"""This function imports json and decodes the data read from the file.
"""
import json


def load_from_json_file(filename):
    """This function returns decoded data read from the file.
    """
    with open(filename, 'r', encoding="UTF8") as f:
        return json.loads(f.read())
