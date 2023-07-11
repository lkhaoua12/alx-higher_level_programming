#!/usr/bin/python3
"""
this module define a class with a public method
"""


class MyList(list):
    """
    this calls inherite from the list class
    """

    def print_sorted(self):
        """
        this function pritn the list sorted in
        ascending order
        """

        sorted_list = sorted(self)
        print(sorted_list)
