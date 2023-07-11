#!/usr/bin/python3
"""
this module define a function
"""


class BaseGeometry:
    """
    this function check if an obj in an instance
    of a_class
    """

    def area(self):
        raise Exception("area() is not implemented")

    
    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
