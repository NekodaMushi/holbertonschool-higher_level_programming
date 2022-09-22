#!/usr/bin/python3


def add_integer(a, b=98):
    """ Function checking if variables
    are integers or floats
    
    Casting variable to integers if they are float
    
    Returns an integer:
    Addition of a and b"""

    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    if not isinstance(a, int):
        raise TypeError("a must be an integer")
    if not isinstance(b, int):
        raise TypeError("b must be an integer")

    return a + b
