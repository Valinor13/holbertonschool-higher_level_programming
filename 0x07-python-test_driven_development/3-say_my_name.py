#!/usr/bin/python3
"""
A module to store a basic person profile
...

Functions
---------
say_my_name(first_name, last_name="")
    Prints the name of the person

Exceptions
----------
raise : TypeError
    Raises an error if arguments do not meet expected types
"""


def say_my_name(first_name, last_name=""):
    """A function to print the name of the person
    If last_name is not given it will be assigned an empty str

    Parameters
    ----------
    first_name : str
        First name of person
    last_name : str
        Last name of person (default empty str)
    """

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
