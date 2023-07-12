#!/usr/bin/python3
"""
Module contains class Student
"""


class Student:
    """
    represents a student
    """

    def __init__(self, first_name, last_name, age):
        """initiates the class student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retreives dict rep of student"""
        return self.__dict__
