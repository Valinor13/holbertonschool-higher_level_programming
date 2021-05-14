#!/usr/bin/python3
"""A module containing Rectangle that inherits from Base"""


from models.base import Base


class Rectangle(Base):
    """A class that handles Rectangle shapes"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """The Rectangle constructor function"""

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def display(self):
        """A function that displays the rectangle in #"""

        for row in range(self.height):
            for col in range(self.width):
                print("#", end="")
            print()

    def area(self):
        """A function that calculates the area of the rectangle"""

        return self.width * self.height

    @property
    def width(self):
        """The width getter function"""

        return self.__width

    @width.setter
    def width(self, value):
        """The width setter function"""

        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """The height getter function"""

        return self.__height

    @height.setter
    def height(self, value):
        """The height setter function"""

        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """The x getter function"""

        return self.__x

    @x.setter
    def x(self, value):
        """The x setter function"""

        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """The y getter function"""

        return self.__y

    @y.setter
    def y(self, value):
        """The y setter function"""

        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
