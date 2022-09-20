#!/usr/bin/python3
"""First time defining a class"""


class Square:
    """class Square that defines a square"""

    def __init__(self, size=0):
        """Initiate square"""
        self.__size= size

    @property 
    def size(self):
        """retrieve size"""
        return self.__size
    @size.setter
    def size(self, value):
        if type(value) and not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
    def area(self):
        return int(self.__size**2)
