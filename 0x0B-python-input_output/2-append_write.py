#!/usr/bin/python3
"""
define a function that open file
"""


def append_write(filename="", text=""):
    """
    read from file and print it to the stdout
    """

    with open(filename, "a", encoding="utf-8") as fd:
        fd.write(text)
        return len(text)
