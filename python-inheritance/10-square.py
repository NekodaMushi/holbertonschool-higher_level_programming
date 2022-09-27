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

        super().__init__(size, size)
