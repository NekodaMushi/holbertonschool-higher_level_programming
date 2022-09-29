#!/usr/bin/python3
"""Train to create class"""


class Student:
    """Student class
    Type Humanoide
    Attributes : 
    First Name
    Last Name
    Age
    """

    def __init__(self, first_name, last_name, age):
        """Initialization of basic attributs of Object"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieves Dictionary Representation"""

        return vars(self)
