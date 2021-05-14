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

    def update(self, *args):
        """A function that assigns arguments to attributes"""

        lst = list(args)
        if len(lst) is 5:
            self.y = lst[4]
            lst.pop()
        if len(lst) is 4:
            self.x = lst[3]
            lst.pop()
        if len(lst) is 3:
            self.height = lst[2]
            lst.pop()
        if len(lst) is 2:
            self.width = lst[1]
            lst.pop()
        if len(lst) is 1:
            self.id = lst[0]

    def __str__(self):
        """A function that overloads the __str__ built-in function"""

        my_string = "[Rectangle] ({}) {}/".format(self.id, self.x)
        my_string += "{} - {}/{}".format(self.y, self.width, self.height)
        return my_string

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
