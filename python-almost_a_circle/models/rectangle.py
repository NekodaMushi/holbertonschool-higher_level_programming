#!/usr/bin/python3
"""Class inheriting from Base"""


from models.base import Base


class Rectangle(Base):
    """Daughter of Base
    Type: Rectangle
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Init a Rectangle
        Args:
        width: width of Rectangle
        height: height of Rectangle
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Getter of width"""
        return self.__width

    @property
    def height(self):
        """Getter of height"""
        return self.__height

    @property
    def x(self):
        """Getter of x"""
        return self.__x

    @property
    def y(self):
        """Getter of y"""
        return self.__y

    @height.setter
    def height(self, value):
        """Defining height of Rectangle
        Checking if input is not integer
        if sides < 0
        Returning error if so"""
        self.valid_attribs("height", value)
        self.__height = value

    @width.setter
    def width(self, value):
        """Defining width of Rectangle
        Checking if input is not integer
        if sides < 0
        Returning error if so"""

        self.valid_attribs("width", value)
        self.__width = value

    @x.setter
    def x(self, value):
        """Defining x of Rectangle
        Checking if value < 0
        Returning error if so"""
        self.valid_attribs("x", value)
        self.__x = value

    @y.setter
    def y(self, value):
        """Defining y of Rectangle
        Checking if value < 0
        Returning error if so"""
        self.valid_attribs("y", value)
        self.__y = value

    def valid_attribs(self, name, value):
        """Validates value
        args:
            name: always a string
            value: an integer
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if name == "width" or name == "height":
            if value <= 0:
                raise ValueError("{} must be > 0".format(name))
        if name == "x" or name == "y":
            if value < 0:
                raise ValueError("{} must be >= 0".format(name))

    def area(self):
        """Return Area of Rectangle"""
        return self.__width * self.__height

    def display(self):
        """Prints in stdout Rectangle
        instance with the character '#'
        """
        print('\n'.join((self.__width * '#') for i in range(self.__height)))
