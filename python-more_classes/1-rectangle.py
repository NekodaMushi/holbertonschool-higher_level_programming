#!/usr/bin/python3
"""First fct defining a rectangle"""


class Rectangle:
    """Rectangle Class"""

    def __init__(self, width=0, height=0):
        """
        Init a rectangle
        Args:
            width: the width of rectangle
            height: the height of rectangle
        Return: None
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        A getter
        Return: self.__width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the width of a rectangle
        Args:
            value (int): The new value of the width
        Raises:
            TypeError: Error if not an int
            ValueError: Error if not positive
        Returns: None
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
        A getter
        Return: self.__height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the height of a rectangle
        Args:
            value (int): The new value of the height
        Raises:
            TypeError: Error if not an int
            ValueError: Error if not positive
        Returns: None
        """

        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
