#!/usr/bin/python3
"""A module containing a function that appends to a file"""


def append_after(filename="", search_string="", new_string=""):
    """A function to append to a file in a certain location"""

    with open(filename, "w+") as f:
        my_list = f.readlines()
        my_string = ""
        for item in my_list:
            my_string += item
            if item is search_string:
                my_string += new_string
        f.write(my_string)
        f.close()
