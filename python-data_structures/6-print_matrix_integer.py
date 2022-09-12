#!/usr/bin/python3
"""function that prints a matrix of integers."""


def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for val in row:
            if val != 0:
                print('', end="")
            print("{:d}".format(val), end=" ")
        print('')
