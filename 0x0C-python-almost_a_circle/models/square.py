#!/usr/bin/python3
"""A module containing Square which inherits from Rectangle"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """A class that handles a rectangle with equal sides"""

    def __init__(self, size, x=0, y=0, id=None):
        """The square constructor class"""

        self.size = size
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """A function to overload __str__"""

        s = "[Square] ({}) {}/".format(self.id, self.x)
        s += "{} - {}".format(self.y, self.size)
        return s

    @property
    def size(self):
        """The size getter function"""

        return self.__size

    @size.setter
    def size(self, value):
        """The size setter function"""

        super().integer_validator("width", value)
        self.__size = value
