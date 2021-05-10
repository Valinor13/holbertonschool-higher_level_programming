#!/usr/bin/python3
"""A module storing a locked class"""


class LockedClass:
    """A class that only creates instances called first_name"""

    @property
    def first_name(self):
        return self.__first_name

    @first_name.setter
    def first_name(self, value):
        self._first_name = value
