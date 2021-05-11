#!/usr/bin/python3
"""A module containing the square class inherited from Rectangle"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A class inherited from rectangle that deals with squares"""

    def __init__(self, size):

        super().integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):

        return self.__size * self.__size
