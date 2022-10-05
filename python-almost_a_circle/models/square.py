#!/usr/bin/python3
"""Class inheriting from Base"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Daughter of Base through Rectangle
    Type: Square
    """

    def __init__(self, size, x=0, y=0, id=None):
        """Init a Square
        Args:
        Size, x, y, id"""
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        """String description of object"""
        return(f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}")
