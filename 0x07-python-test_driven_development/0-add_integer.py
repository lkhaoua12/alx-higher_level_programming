#!/usr/bin/python3
"""
this module define a function that add two numbers
"""


def add_integer(a, b=98):
    """
    this funtion add two numbers
    Args: a, b
    Return: a + b
    """

    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return a + b
