#!/usr/bin/python3
"""This module contains a function that returns a dictionary description of \
        a class.
"""
import json


def class_to_json(obj):
    """This is the function that returns a dictionary description of a class.
    """
    return vars(obj)
