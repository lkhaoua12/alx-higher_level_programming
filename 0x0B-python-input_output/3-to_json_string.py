#!/usr/bin/python3
"""
define a function that open file
"""


import json


def to_json_string(my_obj):
    """
    return the JSON string of an object
    """

    return json.dumps(my_obj)
