#!/usr/bin/python3
"""A module containing a function for writing to a file"""


def write_file(filename="", text=""):
    """A function that writes to a file"""

    with open(filename, 'w') as f:
        bytecount = f.write(text)
        f.close()
    return bytecount
