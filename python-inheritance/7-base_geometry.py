#!/usr/bin/python3
"""BaseGeometry Function"""


class BaseGeometry:
    """Mother class for Geometric Object"""

    def area(self):
        """Raises Exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value
        args:
            name: always a string
            value: an integer
        """
        if not isinstance(value, int):
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")
        