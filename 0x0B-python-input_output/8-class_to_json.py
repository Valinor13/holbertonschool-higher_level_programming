#!/usr/bin/python3
"""A module containing a function that returns dict of a class"""

def class_to_json(obj):
    """A function that returns the dir in a string"""

    return vars(obj)
