#!/usr/bin/python3
"""A module containing a class called MyList"""


class MyList(list):
    """A class that inherits list objects and attributes"""

    def print_sorted(self):
        """A function that prints the sorted list"""

        print(sorted(self))
