#!/usr/bin/python3
"""function that prints a matrix of integers."""


def print_matrix_integer(matrix=[[]]):
    for line in matrix:
        print(' '.join("{:d}".format(row) for row in line))
