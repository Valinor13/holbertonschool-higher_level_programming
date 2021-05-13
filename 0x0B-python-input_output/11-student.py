#!/usr/bin/python3
"""A module with the class Student"""


class Student:
    """A class that stores student with their records"""

    def __init__(self, first_name, last_name, age):

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):

        a = {}
        if attrs is None:
            return vars(self)
        if type(attrs) is str:
            try:
                a[attrs] = getattr(self, attrs)
                return a
            except:
                pass
        for item in attrs:
            try:
                a[item] = getattr(self, item)
            except:
                pass
        return a

    def reload_from_json(self, json):

        for k in json:
            setattr(self, k, json[k])
