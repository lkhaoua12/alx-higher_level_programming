#!/usr/bin/python3
"""
    this module define the base class
"""


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
