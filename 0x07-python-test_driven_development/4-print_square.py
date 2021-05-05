#!/usr/bin/python3
"""
A module to store simple functions for testing

...

Functions
---------
print_square(size)
    Prints a square based on the input size

Exceptions
----------
raise : TypeError
    Raises an error if arguments do not meet expected types
raise : ValueError
    Raises an error if the input value is out of range
"""


def print_square(size):
    """A function to print a square based on input size

    Parameters
    ----------
    size : int, float
        Input number to determine size of # square
    """

    if not isinstance(size, (int, float)):
        raise TypeError("size must be an integer")
    if type(size) is float:
        if size < 0:
            raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for row in range(int(size)):
        for col in range(int(size)):
            print("#", end="")
        print()
