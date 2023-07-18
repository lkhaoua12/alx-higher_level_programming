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
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
