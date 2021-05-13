#!/usr/bin/python3
"""A module with the class Student"""


class Student:
    """A class that stores student with their records"""

    def __init__(self, first_name, last_name, age):

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):

        return vars(self)
