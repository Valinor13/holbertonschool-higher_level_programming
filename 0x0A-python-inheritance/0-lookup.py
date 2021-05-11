#!/usr/bin/python3
"""
A module containing a function call to
lookup object attributes and methods
"""


def lookup(obj):
    """A function that returns a list of the object directory"""

    return [dir(obj)]
