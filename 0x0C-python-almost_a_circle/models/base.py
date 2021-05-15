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

    @classmethod
    def save_to_file(cls, list_objs):
        """A function that writes json to file"""

        filename = cls.__name__ + ".json"
        my_string = ""
        if list_objs:
            for item in list_objs:
                my_dict = cls.to_dictionary(item)
                j_string = cls.to_json_string(my_dict)
                my_string += j_string
        with open(filename, "w") as f:
            bytecount = f.write(my_string)
        return bytecount

    @staticmethod
    def to_json_string(list_dictionaries):
        """A function that converts a dictionary to a json string"""

        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)
