#!/usr/bin/python3
"""A module with a function to load a json file and convert to python"""


import json


def load_from_json_file(filename):
    """A function that loads a json file as python"""

    with open(filename) as f:
        string = json.loads("".join(f.readlines()))
        f.close()
    return string
