#!/usr/bin/python3
"""A module that contains a function for checking class"""


def is_same_class(obj, a_class):
    """A function that returns True if types match"""

    if a_class is object or a_class is True or a_class is False:
        return False
    return isinstance(obj, a_class)
