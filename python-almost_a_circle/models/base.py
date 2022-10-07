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

    @classmethod
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
        except TypeError:
            return lsdt

    @classmethod
    def save_to_file_csv(cls, list_objs):

        from models.rectangle import Rectangle
        from models.square import Square

        with open(cls.__name__+".csv", "w") as fp:
            writer = csv.writer(fp)
            if cls.__name__ == Rectangle:
                writer.writerow(Rectangle)
            if cls.__name__ == Square:
                writer.writerow(Square)


    @classmethod
    def load_from_file_csv(cls):
        """
        Load instance from csv file
        Args:
        Returns: A list of all instances
        """
        filename = cls.__name__ + ".csv"
        listOfObjs = []
        try:
            with open(filename, "r") as f:
                reader = csv.reader(f)
                for elem in reader:
                    if cls.__name__ == "Rectangle":
                        newObj = {
                            "id": int(elem[0]),
                            "width": int(elem[1]),
                            "height": int(elem[2]),
                            "x": int(elem[3]),
                            "y": int(elem[4]),
                        }
                    else:
                        newObj = {
                            "id": int(elem[0]),
                            "size": int(elem[1]),
                            "x": int(elem[2]),
                            "y": int(elem[3]),
                        }
                    newObj = cls.create(**newObj)
                    listOfObjs.append(newObj)
            return listOfObjs
        except FileExistsError:
            return []
