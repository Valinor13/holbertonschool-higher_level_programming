#!/usr/bin/python3
"""A module containing a function that converts a json string to python"""


import json


def from_json_string(my_str):
    """A function that loads a json string into python code"""

    return json.loads(my_str)
