#!/usr/bin/python3
"""First time defining a class"""


class Square:
    """Square Class"""

    def __init__(self, size=0):
        """
        Init a square
        Args:
            size: the size of square
        Return: None
        """
        self.__size = size

    @property
    def size(self):
        """
        A getter
        Return: self.__size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square
        Args:
            value (int): The new value of the size
        Raises:
            TypeError: Error if not an int
            ValueError: Error if not positiv
        Returns: None
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Calcul area of the square
        Returns: The area of the square
        """
        return int(self.__size ** 2)

    def my_print(self):
        """
        Print in stdout
        Returns: Square with #
        """
        if self.__size == 0:
            print()
        for i in range(self.__size):
            for j in range(self.__size):
                print('#', end="")
            print()
