#!/usr/bin/python3
"""A module for storing geometric shapes and their attributes"""


class Square:
    """A class to store the square shape and its size safely"""

    def __init__(self, __size=0):
        """Initialization of self and size of square"""

        self.__size = __size
        if type(__size) is not int:
            raise TypeError("size must be an integer")
        if __size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """A function that returns area of square"""

        return self.__size ** 2
