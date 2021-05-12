#!/usr/bin/python3
"""A module with a function that saves json to a file"""


import json


def save_to_json_file(my_obj, filename):
    """A function that saves json to a file"""

    with open(filename, 'w') as f:
        bytecount = f.write(json.dumps(my_obj))
        f.close()
    return bytecount
