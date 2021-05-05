#!/usr/bin/python3
""" """


def print_square(size):
    """ """

    if type(size) is not int and type(size) is not float:
        raise TypeError("size must be an integer")
    if type(size) is float:
        if size < 0:
            raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for row in range(size):
        for col in range(size):
            print("#", end="")
        print()
