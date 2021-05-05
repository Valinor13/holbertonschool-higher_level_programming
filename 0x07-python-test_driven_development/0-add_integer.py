#!/usr/bin/python3
"""
A module to store simple functions for testing

...

Functions
---------
add_integer(a, b=98)
    Returns two integers or floats added together

Exceptions
----------
raise : TypeError
    Raises a TypeError if a or b are not int or float

"""


def add_integer(a, b=98):
    """A function to safely add two integers

    If the argument b isn't passed in, the default 98 is used

    Parameters
    ----------
    a : int, float
        the first number to add
    b : int, float
        the second number to add (default is 98)
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return a + b
