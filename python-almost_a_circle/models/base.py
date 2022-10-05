#!/usr/bin/python3
"""Second file: Base Class """
import json


class Base:
    """Mother Class for Geometrical Object"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Init a Geometrical Object"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return string representation of list_dictionaries"""
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        if list_objs is None:
            list_objs = []
        output_dict = []

        for objs in list_objs:
            output_dict.append(objs.to_dictionary())

        with open(cls.__name__+".json", "w",) as f:
            f.write(cls.to_json_string(output_dict))
