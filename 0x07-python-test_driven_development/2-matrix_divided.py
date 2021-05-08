#!/usr/bin/python3
"""
A module to store simple functions for testing

...

Functions
---------
matrix_divided(matrix, div)
    Returns a matrix of all the numbers in the original
    matrix divided by the div argument

Exceptions
----------
raise : TypeError
    Raises an error if arguments do not meet expected types
raise : ZeroDivisionError
    Raises an error if number to divide by is 0
"""


def matrix_divided(matrix, div=1):
    """A function to safely divide a matrix by a number

    Parameters
    ----------
    matrix : list
        a list containing lists contaning ints or floats
    div : int, float
        an int or float that the matrix will be divided by
    """

    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix (list of lists"
                        ") of integers/floats")
    for items in matrix:
        if type(items) is not list:
            raise TypeError("matrix must be a matrix "
                            "(list of lists) of integers/floats")
        for num in items:
            if not isinstance(num, (int, float)):
                raise TypeError("matrix must be a matrix "
                                "(list of lists) of integers/floats")
    control_item = matrix[0]
    for item in matrix:
        if len(item) is not len(control_item):
            raise TypeError("Each row of the matrix must have the same size")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    a = list(map(lambda x: list(map(lambda y: round(y / div, 2), x)), matrix))
    return a
