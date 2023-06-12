#!/usr/bin/pydoc3

def divisible_by_2(my_list=[]):
    new_list = []
    for num in my_list:
        new_list.append(num % 2)
    return new_list
