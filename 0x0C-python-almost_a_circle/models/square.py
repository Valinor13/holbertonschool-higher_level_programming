#!/usr/bin/python3
"""A module containing Square which inherits from Rectangle"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """A class that handles a rectangle with equal sides"""

    def __init__(self, size, x=0, y=0, id=None):
        """The square constructor class"""

        super().__init__(size, size, x, y, id)

    def __str__(self):
        """A function to overload __str__"""

        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)
