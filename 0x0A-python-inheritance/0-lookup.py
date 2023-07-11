#!/usr/bin/python3
"""
this module define a function that return a list
"""


def lookup(obj):
    """
    this function takes an object and return it methods
    and attribute as a list
    """

    return dir(obj)
