#!/usr/bin/python3
"""
define a function that open file
"""


def write_file(filename="", text=""):
    """
    read from file and print it to the stdout
    """
    
    with open(filename, "w") as fd:
        fd.write(text)
        return len(text)
