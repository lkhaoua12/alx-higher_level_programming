#!/usr/bin/python3
"""
this module contains class_to_json function
"""


def class_to_json(obj):
    """
    this function takes an object and return it 
    dict desription of data
    """

    return obj.__dict__
