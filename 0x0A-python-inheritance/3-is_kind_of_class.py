#!/usr/bin/python3
"""A module containing a function for class kind checks"""


def is_kind_of_class(obj, a_class):
    """A function that returns True if obj is instance of class or subclass"""

    return isinstance(obj, a_class)
