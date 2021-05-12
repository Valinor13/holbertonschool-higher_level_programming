#!/usr/bin/python3
"""A module containing a function to append to a file"""


def append_write(filename="", text=""):
    """A function that appends text to filename"""

    with open(filename, 'a') as f:
        bytecount = f.write(text)
        f.close()
    return bytecount
