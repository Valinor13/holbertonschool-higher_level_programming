#!/usr/bin/python3
"""A module to store a basic person profile"""


def say_my_name(first_name, last_name=""):
    """A function to print the name of the person"""

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
