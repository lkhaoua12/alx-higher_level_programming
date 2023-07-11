#!/usr/bin/python3
"""
this module define a function
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """
    this calss define a Rectangle that inherite
    from BaseGeometry
    """

    def __init__(self, width, height):
        """
        this function initialize the instance
        """

        self.__width = self.integer_validator("width", width)
        self.__height = self.integer_validator("height", height)
