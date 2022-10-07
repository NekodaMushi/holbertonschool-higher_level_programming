#!/usr/bin/python3
"""Second file: Base Class """
from genericpath import exists
import json
import csv


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

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation"""
        if json_string is None:
            empty_list = []
            return empty_list
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        if cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        filename = cls.__name__+".json"
        lsdt = []
        try:
            with open(filename, "r") as fp:
                temp_list = cls.from_json_string(fp.read())
            for i in range(len(temp_list)):
                lsdt.append(cls.create(**temp_list[i]))
            return lsdt
        except FileNotFoundError:
            return lsdt
