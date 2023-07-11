#!/usr/bin/python3
"""
define a function that open file
"""


import json


def from_json_string(my_str):
    """
    return the JSON string of an object
    """

    return json.loads(my_str)
