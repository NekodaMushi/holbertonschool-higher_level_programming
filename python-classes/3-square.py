#!/usr/bin/python3
"""First time defining a class"""


class Square:
    """class Square that defines a square"""

    def __init__(self, size=0):
        """Size of square initialized"""

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Field of Square"""
        return int(self.__size) * int(self.__size)
