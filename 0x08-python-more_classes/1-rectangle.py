#!/usr/bin/python3
"""
this modules define a class with methods and attribute
"""


class Rectangle:
    """
    this is the definittin of the class Rectangle
    Attribute: width
    Methods: none
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(int, value):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

