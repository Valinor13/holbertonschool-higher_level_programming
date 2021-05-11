#!/usr/bin/python3
"""A module that contains a function for checking class inheritance"""


def inherits_from(obj, a_class):
    """A function that returns true if obj inherits type from class"""

    if type(obj) is a_class:
        return False
    return issubclass(type(obj), a_class)
