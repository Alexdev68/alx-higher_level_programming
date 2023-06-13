#!/usr/bin/python3
"""This module imports json and decodes json encoded strings.
"""
import json


def from_json_string(my_str):
    """This function decodes json encoded strings.
    """
    return json.loads(my_str)
