#!/usr/bin/python3
"""A module that stores a function to convert to JSON"""


import json


def to_json_string(my_obj):
    """Returns a string converted to json"""

    return json.dumps(my_obj)
