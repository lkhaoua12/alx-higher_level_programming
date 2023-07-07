#!/usr/bin/python3
"""
this module define a function that print a text
"""


def text_indentation(text):
    """
    this function takes a text and re-formate it.
    Args: text(string)
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    punctuation_marks = ['.', '?', ':']
    result = ""
    line = ""

    for char in text:
        line += char

        if char in punctuation_marks:
            result += line.strip() + "\n\n"
            line = ""

    if line:
        result += line.strip()

    print(result)
