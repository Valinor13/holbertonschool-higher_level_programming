#!/usr/bin/python3
"""A module for storing geometric shapes and their attributes"""


class Square:
    """A class to store the square shape and its size safely"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialization of self and size + position of square"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        if type(position) is not tuple or len(position) < 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(position[0]) is not int or type(position[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.size = size
        self.position = position

    def size(self):
        """square size getting function"""

        if type(self.size) is not int:
            raise TypeError("size must be an integer")
        if self.size < 0:
            raise ValueError("size must be >= 0")
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

    def my_print(self):
        """A function to print the area of a square with #"""

        if type(self.size) is not int:
            raise TypeError("size must be an integer")
        if self.size < 0:
            raise ValueError("size must be >= 0")
        if self.size == 0:
            print()
        else:
            lon, lat, *scrap = self.position
            for newline in range(lat):
                print()
            for row in range(self.size):
                for spaces in range(lon):
                    print(" ", end="")
                for col in range(self.size):
                    print("#", end="")
                print()

    def position(self):
        """A function to retrieve the value of the position variable"""

        return self.position

    def position(self, value):
        """A function to set the value of the position variable"""

        if type(value) is not tuple or len(value) < 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[0]) is not int or type(value[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.position = value

    def __repr__(self):
        """A built-in function to print the square class with its objects"""

        retstr = ""
        if self.size == 0:
            return ""
        else:
            lon, lat, *scrap = self.position
            for newline in range(lat):
                retstr += "\n"
            for row in range(self.size):
                for spaces in range(lon):
                    retstr += " "
                for col in range(self.size):
                    retstr += "#"
                if row is not self.size - 1:
                    retstr += "\n"
            return retstr
