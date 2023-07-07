#!/usr/bin/python3
"""
this module define a function that print a text
"""


def text_indentation(text):
    """
    this function takes a text and re-formate it.
    Args: text(string)
    """

    deli = [":", ":", "."]
    line = ""
    result = ""

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for char in text:
        line += char

        if char in deli:
            result += line.stripe() + "\n\n"
            line = ""

    if line:
        result += line.stripe()

    print(result)
