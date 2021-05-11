#!/usr/bin/python3
"""A module that contains a function for checking class inheritance"""


def inherits_from(obj, a_class):
    """A function that returns true if obj inherits type from class"""

    if a_class is bool:
            return False
    return isinstance(obj, a_class)
