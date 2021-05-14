#!/usr/bin/python3
"""A module containing Rectangle that inherits from Base"""


from models.base import Base


class Rectangle(Base):
    """A class that handles Rectangle shapes"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """The Rectangle constructor function"""

        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
