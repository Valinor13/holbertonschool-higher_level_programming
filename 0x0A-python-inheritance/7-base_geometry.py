#!/usr/bin/python3
"""A module containing an class called base geometry"""


class BaseGeometry:
    """A class with a func that raises an exception"""

    def area(self):
        """A function that raises an exception"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """A function that validates the value parameter"""

        if type(value) is not int:
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")
