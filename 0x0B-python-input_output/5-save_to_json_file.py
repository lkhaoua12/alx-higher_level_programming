#!/usr/bin/python3
"""
define a function that open file
"""


import json


def save_to_json_file(my_obj, filename):
    """
    return the JSON string of an object
    """

    with open(filename, "w", encoding="utf-8") as fd:
        json.dump(my_obj, fd)

