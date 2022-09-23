#!/usr/bin/python3
"""Prints a Square"""


def print_square(size):
    """ Function checking if size is a integer
    
    Raises exception if:
    not a integer
    value is less than 0
    size is a float
    
    
    Print Square using '#'
    
    Returns: Nothing """

    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float):
        raise TypeError("size must be an integer")
    print(("#" * size + "\n") * size, end="")
