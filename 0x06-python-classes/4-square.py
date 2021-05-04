#!/usr/bin/python3
"""A module for storing geometric shapes and their attributes"""


class Square:
    """A class to store the square shape and its size safely"""

    def __init__(self, size=0):
        """Initialization of self and size of square"""

        self.size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def size(self):
        """square size getting function"""

        return self.size

    def size(self, value):
        """square size setter function"""

        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.size = value

    def area(self):
        """A function that returns area of square"""

        if type(self.size) is not int:
            raise TypeError("size must be an integer")
        if self.size < 0:
            raise ValueError("size must be >= 0")

        return self.size ** 2
