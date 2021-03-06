#!/usr/bin/python3
"""A module with a function to load a json file and convert to python"""


import json


def load_from_json_file(filename):
    """A function that loads a json file as python"""

    with open(filename) as f:
        my_obj = json.loads(f.read())
        f.close()
    return my_obj
