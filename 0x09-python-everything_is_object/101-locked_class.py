#!/usr/bin/python3
"""A module storing a locked class"""


class LockedClass:
    """A class that only creates instances called first_name"""

    __slots__ = 'first_name'
