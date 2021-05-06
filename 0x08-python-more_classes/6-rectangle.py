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
    __init__(self, width=0, height=0)
        The constructor function
    width(self)
        The width getter function
    width(self, value)
        The width setter function
    height(self)
        The height getter function
    height(self, value)
        The height setter function
    area(self)
        Returns the area of the rectangle
    perimeter(self)
        Returns the perimeter of the rectangle
    __str__(self)
        Returns a string of # in rectangle shape
    __repr__(self)
        Returns a string of Class(attributes)
    __del__(self)
        Prints a message after deleting an instance of rectangle

    Attributes
    ----------
    nummber_of_instances : int
        initialized as 0, keeps count of the instances of Rectangle
    """

    number_of_instances = 0

    def __del__(self):
        """A function to print a message when delete is called"""

        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    def __init__(self, width=0, height=0):
        """The constructor function
        If width is not assigned it defaults to 0
        If height is not assigned it defaults to 0
        """

        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def __str__(self):
        """A function to return the rectangle in #"""

        string = ""
        if self.width == 0:
            return string
        for i in range(self.height):
            for j in range(self.width):
                string += "#"
            if i is not self.height - 1:
                string += "\n"
        return string

    def __repr__(self):
        """A function to return the class with its attributes"""

        return "Rectangle({}, {})".format(self.width, self.height)
