#!/usr/bin/python3
"""
A module that holds geometric shapes in classes
...
Classes
-------
Rectangle
    Holds attributes of a rectangle
"""


class Rectangle:
    """
    A class used to represent rectangles
    ...
    Methods
    -------
    pass
    """

    def __init__(self, width=0, height=0):
        """The constructor function"""

        self.width = width
        self.height = height

    @property
    def width(self):
        """The width attribute getter function"""

        return self.__width

    @width.setter
    def width(self, value):
        """The width attribute setter function"""

        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """The height attribute getter function"""

        return self.__height

    @height.setter
    def height(self, value):
        """The height attribute setter function"""

        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """A function that returns the area of the rectangle"""

        return (self.width * self.height)

    def perimeter(self):
        """A function that returns the perimeter of the rectangle"""

        if self.width == 0 or self.height == 0:
            return 0
        return ((self.width * 2) + (self.height * 2))
