#!/usr/bin/python3
"""A module that contains a function for checking class"""


def is_same_class(obj, a_class):
    """A function that returns True if types match"""

    if isinstance(obj, a_class):
        return True
    return False
