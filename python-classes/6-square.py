#!/usr/bin/python3
"""First time defining a class"""


class Square:
    """Square Class"""

    def __init__(self, size=0, position=(0, 0)):
        """
        Init a square
        Args:
            size: the size of square
        Return: None
        """
        self.__size = size
        self.position = position

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

    @property
    def position(self):
        """Get position
        Returns: The position of square"""

        return self.__position

    @position.setter
    def position(self, value):
        """Position of the square to the space"""

        if isinstance(value, tuple) and len(value) == 2 and\
            type(value[0]) is int and value[0] >= 0 and \
                type(value[1]) is int and value[1] >= 0:
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def my_print(self):
        """Print Square
        Returns : Nothing"""

        if self.__size == 0:
            print()
        else:
            for i in range(self.position[1]):
                print()
            for i in range(self.__size):
                print("".join([" " for k in range(self.position[0])]), end="")
                print("".join(["#" for h in range(self.__size)]))
