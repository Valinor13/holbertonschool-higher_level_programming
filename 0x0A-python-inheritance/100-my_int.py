#!/usr/bin/python3
"""A module containing MyInt inherited from int"""


class MyInt(int):
    """A class that reverses bool checks"""

    def _init__(self, value):

        self.value = value

    def __eq__(self, other):

        return not other

    def __ne__(self, other):

        return not self.__eq__(other)
