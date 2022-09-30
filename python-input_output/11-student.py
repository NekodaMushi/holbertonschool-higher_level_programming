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

    def to_json(self, attrs=None):
        """Retrieves Dictionary Representation"""

        if type(attrs) is list:
            lis = {}
            for attribut in attrs:
                if hasattr(self, attribut):
                    lis[attribut] = getattr(self, attribut)
            return lis
        return vars(self)

    def reload_from_json(self, json):
        """Replaces all attributes of the Student"""

        for key, value in json.items():
            setattr(self, key, value)
