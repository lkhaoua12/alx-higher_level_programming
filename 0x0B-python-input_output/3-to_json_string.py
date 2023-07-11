#!/usr/bin/python3
import json
"""
define a function that open file
"""

def to_json_string(my_obj):
    """
    return the JSON string of an object
    """

    return json.dump(my_obj)
