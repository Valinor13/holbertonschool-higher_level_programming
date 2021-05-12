#!/usr/bin/python3
"""A module that stores a function built to read a text file"""


def read_file(filename=""):
    """A function to read a text file"""

    with open(filename) as f:
        print("".join(f.readlines()), end="")
        f.close()
