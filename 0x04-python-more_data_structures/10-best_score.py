#!/usr/bin/python3
def best_score(a_dictionary):
    result = None
    for key in a_dictionary.keys():
        if a_dictionary[key] > a_dictionary[result]:
            result = key
    return result
