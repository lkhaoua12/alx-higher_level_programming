#!/usr/bin/python3
"""
this module declare a class and set it attribute
"""

class LockedClass:
    """
    a locked class from dynamicaly changing attribute
    """

    def __setattr__(self, name, value):
        if not hasattr(self, name) and name != 'first_name':
            raise AttributeError("'LockedClass' object has no attribute '{}'".format(name))
        else:
            object.__setattr__(self, name, value)
