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
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
        