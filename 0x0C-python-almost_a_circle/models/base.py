#!/usr/bin/python3
"""A module containing the class Base"""


import json


class Base:

    """The class Base"""

    __nb_objects = 0

    def __init__(self, id=None):
        """The Base constructor function"""

        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """A function that converts a dictionary to a json string"""

        if list_dictionaries is None or list_dictionaries is {}:
            return "[]"
        my_string = ""
        for item in list_dictionaries:
            j_string = json.dumps(item)
            my_string += j_string
        return [my_string]
