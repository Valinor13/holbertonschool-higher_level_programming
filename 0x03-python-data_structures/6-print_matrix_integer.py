#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix == [[]]:
        print()
    else:
        for x in matrix:
            length = len(x) - 1
            for y in range(length):
                print("{:d}".format(x[y]), end=" ")
            print("{:d}".format(x[length]))
