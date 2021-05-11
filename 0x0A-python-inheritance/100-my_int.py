#!/usr/bin/python3
"""A module containing MyInt inherited from int"""


class MyInt(int):
    """A class that reverses bool checks"""

    def __init__(self, value=0):
        self.value = value

    def __eq__(self, other):

        if self.value is 0:
            return False
        return not other

    def __ne__(self, other):

        return not self.__eq__(other)
