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

    def __str__(self):
        """String description of object"""
        return(f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}")

    def update(self, *args, **kwargs):
        """Assigns attributes"""
        try:
            self.id = args[0]
            self.size = args[1]
            self.x = args[2]
            self.y = args[3]
        except IndexError:
            pass

        for key, value in kwargs.items():
            setattr(self, key, value)

    def to_dictionary(self):
        """Dictionnary rep of Square"""
        return {'id' : self.id, 'Size' : self.size, 'x' : self.x, 'y' : self.y}
