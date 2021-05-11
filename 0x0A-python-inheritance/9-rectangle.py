#!/usr/bin/python3
"""A module containing an class called Rectangle"""


class BaseGeometry:
    """A class with a func that raises an exception"""

    def area(self):
        """A function that raises an exception"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """A function that validates the value parameter"""

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """A class with functions that handle arguments for a rectangle"""

    def __init__(self, width, height):

        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):

        return self.__width * self.__height

    def __str__(self):

        return "[Rectangle] {}/{}".format(self.__width, self.__height)
