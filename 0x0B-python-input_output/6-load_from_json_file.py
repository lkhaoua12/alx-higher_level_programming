#!/usr/bin/python3
"""
define a function that open file
"""


import json


def load_from_json_file(filename):
    """
    return the JSON string of an object
    """

    with open(filename, "w", encoding="utf-8") as fd:
        return json.load(fd)
