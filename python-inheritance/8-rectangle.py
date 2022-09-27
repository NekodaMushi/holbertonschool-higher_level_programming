#!/usr/bin/python3
"""BaseGeometry Function"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


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

class Rectangle(BaseGeometry):
    """Daughter of BaseGeometry
    Type: Rectangle
    """

    def __init__(self, width, height):
        """
        Init a Rectangle
        Args:
            width: width of Rectangle
            height: height of Rectangle
        Return: None
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
