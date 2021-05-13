#!/usr/bin/python3
"""A module containing a function that appends to a file"""


def append_after(filename="", search_string="", new_string=""):
    """A function to append to a file in a certain location"""

    with open(filename) as f:
        read_line = f.readline()
        read_string = ""
        while read_line:
            if search_string in read_line:
                read_string += read_line + new_string
            else:
                read_string += read_line
            read_line = f.readline()
        f.close()
    with open(filename, "w") as f:
        f.write(read_string)
        f.close()
