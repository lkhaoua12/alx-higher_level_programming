#!/usr/bin/python3
"""
this module define a function that print a text
"""


def text_indentation(text):
    """
    this function takes a text and re-formate it.
    Args: text(string)
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    for i in range(len(text)):
        if text[i] == "." or text[i] == "?" or text[i] == ":":
            print(text[i])
            print()
        else:
            print(text[i], end="")
