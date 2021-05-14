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

    def to_json_string(list_dictionaries):
        """A function that converts a dictionary to a json string"""

        if list_dictionaries is None or list_dictionaries[0] is {}:
            return "[]"
        my_string = ""
        for item in list_dictionaries:
            my_string += json.dumps(list_dictionaries)
        return my_string
