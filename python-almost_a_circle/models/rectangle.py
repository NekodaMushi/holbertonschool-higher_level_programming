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

