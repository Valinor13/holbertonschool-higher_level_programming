#!/usr/bin/python3
"""A module to store functions that perform basic math actions"""


def matrix_divided(matrix, div):
    """A function to divide a matrix by a given divisor"""

    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix (list of lists"
                        ") of integers/floats")
    for items in matrix:
        if type(items) is not list:
            raise TypeError("matrix must be a matrix "
                            "(list of lists) of integers/floats")
    control_item = matrix[0]
    for item in matrix:
        if len(item) is not len(control_item):
            raise TypeError("Each row of the matrix must have the same size")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    return list(map(lambda x: list(map(lambda xx: round(xx / div, 2), x)), matrix))
