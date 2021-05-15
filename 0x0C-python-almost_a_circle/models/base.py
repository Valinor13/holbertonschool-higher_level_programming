#!/usr/bin/python3
"""A module containing the class Base"""


import json
import os


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
    def load_from_file(cls):
        """A function that loads a list of class instances from a json file"""

        filename = cls.__name__ + ".json"
        if os.path.exists(filename):
            with open(filename) as f:
               my_string = cls.from_json_string(f.read())
            print(my_string)
            my_obj = cls.create(**my_string)
            return my_obj
        else:
            return []


    @classmethod
    def create(cls, **dictionary):
        """A function that creates and updates a class instance"""

        if len(dictionary) == 1:
            dum1 = cls(1)
            dum1.update(**dictionary)
            return dum1
        else:
            dum3 = cls(3, 2)
            dum3.update(**dictionary)
            return dum3

    @classmethod
    def save_to_file(cls, list_objs):
        """A function that writes json to file"""

        filename = cls.__name__ + ".json"
        if list_objs:
            my_list = []
            for item in list_objs:
                my_dict = cls.to_dictionary(item)
                my_list.append(my_dict)
            j_string = cls.to_json_string(my_list)
        else:
            j_string = "[]"
        with open(filename, "w") as f:
            bytecount = f.write(j_string)
        return bytecount

    @staticmethod
    def from_json_string(json_string):
        """A function that converts a json string to a list"""

        if not json_string or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @staticmethod
    def to_json_string(list_dictionaries):
        """A function that converts a dictionary to a json string"""

        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)
