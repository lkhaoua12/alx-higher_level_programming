#!/usr/bin/python3
"""
this module define a function
"""


def inherits_from(obj, a_class):
    """
    this function check if an obj in an instance
    of a_class
    """

    return issubclass(type(obj), a_class) and type(obj) != a_class

