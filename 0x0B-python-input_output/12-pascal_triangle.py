#!/usr/bin/python3
"""A module containing a function that returns pascal's triangle"""


def pascal_triangle(n):
    """A function that returns pascal's triangle"""

    my_matrix = []
    if n <= 0:
        return my_list
    for i in range(n):
        row_list = []
        for j in range(i + 1):
            if j == i:
                row_list.append(1)
                my_matrix.append(1)
            elif j == 0:
                row_list.append(1)
            else:
                row_list.append(my_matrix[i - 1][j - 1] + my_matrix[i - 1][j])
    return my_list
