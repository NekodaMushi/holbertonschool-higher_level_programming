#!/usr/bin/python3
"""BaseGeometry Function"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


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

    def area(self):
        """Method returning area of Rectangle"""

        return self.__width * self.__height

    def __str__(self):
        """Method representing the rectangle"""

        return (f"[Rectangle] {self.__width}/{self.__height}")
