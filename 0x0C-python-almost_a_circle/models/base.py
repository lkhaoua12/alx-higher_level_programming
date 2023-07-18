#!/usr/bin/python3
"""
    this module define the base class
"""

import json


class Base():
    """
        this is the base class that
        keeps track of all classes ids
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """method to initiate a new object"""

        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """return json representtion of objct"""

        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """write json represention to a file"""

        if list_objs is None:
            list_objs = []

        classname = cls.__name__
        filename = classname + ".json"

        jsonString = cls.to_json_string(
            [obj.to_dictionary() for obj in list_objs]
        )
        with open(filename, "w") as file:
            file.write(jsonString)

    @classmethod
    def create(cls, **dictionary):
        """create a new instance from kwargs"""

        insc = cls(1, 1) if cls.__name__ == "Rectangle" else cls(1)
        insc.update(**dictionary)
        return insc

    @staticmethod
    def from_json_string(json_string):
        """get representaion from json string"""

        if not json_string or json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def load_from_file(cls):
        """return list of instances from a file"""

        file_name = cls.__name__ + ".json"
        try:
            with open(file_name, "r") as file:
                json_string = file.read()
            instances_data = cls.from_json_string(json_string)
            instances_list = [cls.create(**data) for data in instances_data]
            return instances_list
        except FileNotFoundError:
            return []
