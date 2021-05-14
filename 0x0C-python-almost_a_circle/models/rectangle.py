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

    @property
    def width(self):
        """The width getter function"""

        return self.__width

    @width.setter
    def width(self, value):
        """The width setter function"""

        self.__width = value

    @property
    def height(self):
        """The height getter function"""

        return self.__height

    @height.setter
    def height(self, value):
        """The height setter function"""

        self.__height = value

    @property
    def x(self):
        """The x getter function"""

        return self.__x

    @x.setter
    def x(self, value):
        """The x setter function"""

        self.__x = value

    @property
    def y(self):
        """The y getter function"""

        return self.__y

    @y.setter
    def y(self, value):
        """The y setter function"""

        self.__y = value
