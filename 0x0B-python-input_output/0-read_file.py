#!/usr/bin/python3
"""
define a function that open file
"""

def read_file(filename=""):
    """
    read from file and print it to the stdout
    """

    with open(filename, "r", encoding="utf-8") as fd:
        for line in fd:
            print(line, end="")
