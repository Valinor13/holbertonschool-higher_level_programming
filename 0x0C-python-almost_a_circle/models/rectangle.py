#!/usr/bin/python3
"""A module containing Rectangle that inherits from Base"""


from models.base import Base
import inspect


class Rectangle(Base):

    """A class that handles Rectangle shapes"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """The Rectangle constructor function"""

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def update(self, *args, **kwargs):
        """A function that assigns arguments to attributes"""

        if args is None or args is ():
            for key in kwargs:
                setattr(self, key, kwargs[key])
        else:
            lattrs = ["id", "width", "height", "x", "y"]
            for value in range(len(args)):
                setattr(self, lattrs[value], args[value])

    def __str__(self):
        """A function that overloads the __str__ built-in function"""

        my_string = "[Rectangle] ({}) {}/".format(self.id, self.x)
        my_string += "{} - {}/{}".format(self.y, self.width, self.height)
        return my_string

    def to_dictionary(self):
        """A function that returns the dictionary rep of Rectangle"""

        my_dict = {}
        for item in inspect.getmembers(self):
            if not item[0].startswith('_'):
                if not inspect.ismethod(item[1]) \
                   and not inspect.isfunction(item[1]):
                    my_dict[item[0]] = item[1]
        return my_dict

    def display(self):
        """A function that displays the rectangle in #"""

        for newline in range(self.y):
            print()
        for row in range(self.height):
            for spaces in range(self.x):
                print(" ", end="")
            for col in range(self.width):
                print("#", end="")
            print()

    def area(self):
        """A function that calculates the area of the rectangle"""

        return self.width * self.height

    def integer_validator(self, attr, value):
        """A function that validates integers and values"""

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(attr))
        if attr is "x" or attr is "y":
            if value < 0:
                raise ValueError("{} must be >= 0".format(attr))
        else:
            if value <= 0:
                raise ValueError("{} must be > 0".format(attr))

    @property
    def width(self):
        """The width getter function"""

        return self.__width

    @width.setter
    def width(self, value):
        """The width setter function"""

        self.integer_validator("width", value)
        self.__width = value

    @property
    def height(self):
        """The height getter function"""

        return self.__height

    @height.setter
    def height(self, value):
        """The height setter function"""

        self.integer_validator("height", value)
        self.__height = value

    @property
    def x(self):
        """The x getter function"""

        return self.__x

    @x.setter
    def x(self, value):
        """The x setter function"""

        self.integer_validator("x", value)
        self.__x = value

    @property
    def y(self):
        """The y getter function"""

        return self.__y

    @y.setter
    def y(self, value):
        """The y setter function"""

        self.integer_validator("y", value)
        self.__y = value
