#!/usr/bin/python3
"""A module containing Rectangle inherited from BaseGeometry"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A class with functions that handle arguments for a rectangle"""

    def __init__(self, width, height):

        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
