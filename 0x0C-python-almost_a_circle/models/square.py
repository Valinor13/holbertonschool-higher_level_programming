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
        s += "{} - {}".format(self.id, self.x)
        return s

    @property
    def size(self):
        """The size getter function"""

        return self.__size

    @size.setter
    def size(self, value):
        """The size setter function"""

        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__size = value
