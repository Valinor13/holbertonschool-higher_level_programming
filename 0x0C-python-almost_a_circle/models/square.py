#!/usr/bin/python3
"""A module containing Square which inherits from Rectangle"""


from models.rectangle import Rectangle
import inspect


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

    def to_dictionary(self):
        """A function that returns the dictionary rep of Square"""

        my_dict = {}
        for item in inspect.getmembers(self):
            if not item[0].startswith('_'):
                if not inspect.ismethod(item[1]):
                    if item[0] is 'width' or item[0] is 'height':
                        continue
                    else:
                        my_dict[item[0]] = item[1]
        return my_dict

    def update(self, *args, **kwargs):
        """A function that assigns arguments to attributes"""

        if args is None or args is ():
            for key in kwargs:
                setattr(self, key, kwargs[key])
        else:
            lattrs = ["id", "size", "x", "y"]
            for value in range(len(args)):
                setattr(self, lattrs[value], args[value])

    @property
    def size(self):
        """The size getter function"""

        return self.__width

    @size.setter
    def size(self, value):
        """The size setter function"""

        super().integer_validator("width", value)
        self.__width = value
        self.__height = value
