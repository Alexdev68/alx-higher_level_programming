#!/usr/bin/python3
"""This module imports json and encodes an object.
"""
import json


def to_json_string(my_obj):
    """This function encodes my_obj with json encoder.
    """
    return json.dumps(my_obj)
