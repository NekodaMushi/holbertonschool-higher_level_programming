#!/usr/bin/python3
"""First fct defining a rectangle"""


class Rectangle:
    """Rectangle Class"""

    number_of_instances = 0
    print_symbol = ("#")
    
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
        Rectangle.number_of_instances += 1

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

    def area(self):
        """
        Calcul area of the rectangle
        Returns: The area of the rectangle
        """
        return int(self.__height) * int(self.__width)

    def perimeter(self):
        """
        Calcul perimeter of the rectangle
        Returns: The perimeter of the rectangle
        """
        if self.width == 0 or self.height == 0:
            return 0
        return int(self.__height) * 2 + int(self.__width) * 2

    def __str__(self):
        """Prints Rectangle"""
        string = ""
        if self.width == 0 or self.height == 0:
            return ""
        for char in range(self.__height):
                string += str(self.print_symbol) * self.__width + "\n"

        return string[:-1]

    def __repr__(self):
        """method that returns an official
        string representation of an instance """

        return ("Rectangle({}, {})".format(self.width, self.height))

    def __del__(self):
        """method deleting rectangle"""

        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
