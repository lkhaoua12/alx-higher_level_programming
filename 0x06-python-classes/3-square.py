#!/usr/bin/python3
"""
define class with instance att size
"""


class Square:
    """
    define a square with instance att size
    Attribute: size
    method: none
    """
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
    def area(self):
        return self.__size ** 2
