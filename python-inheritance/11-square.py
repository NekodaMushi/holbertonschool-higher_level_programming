#!/usr/bin/python3
"""BaseGeometry Function"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Daughter of Rectangle
    Type: Square
    """

    def __init__(self, size):
        """
        Init: Square
        Args: Size
        Returns: Nothing
        """

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """Method representing the square"""

        return (f"[Square] {self.__size}/{self.__size}")
