#!/usr/bin/python3
"""Second file: Base Class """
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

    def from_json_string(json_string):
        """Returns the list of the JSON string representation"""
        if json_string is None:
            empty_list = []
            return empty_list
        return json.loads(json_string)

    @classmethod
    def save_to_file_csv(cls, list_objs):

        rect= [idxself.id, idxself.width, idxself.height, idxself.x, idxself.y]
        sqre= [idxself.id, idxself.size, idxself.x, idxself.y]
        with open(cls.__name__+".csv", "w") as fp:
            writer = csv.writer(fp)
            for idxself in list_objs:
                if cls.__name__ == "Rectangle":
                    writer.writerows(rect)
                if cls.__name__ == "Square":
                    writer.writerows(sqre)
