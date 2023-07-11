#!/usr/bin/python3
"""
define a function that open file
"""


from typing import List
import json
import sys


def add_arguments_to_list(args: List[str]):
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file =\
        __import__('6-load_from_json_file').load_from_json_file

    try:
        existing_data = load_from_json_file('add_item.json')
        my_list = existing_data + args
    except FileNotFoundError:
        my_list = args

    save_to_json_file(my_list, 'add_item.json')


arguments = sys.argv[1:]
add_arguments_to_list(arguments)
