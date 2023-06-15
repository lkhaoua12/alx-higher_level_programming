#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    result = None
    for key in a_dictionary.keys():
        if result is None or a_dictionary[key] > a_dictionary[result]:
            result = key
    return result
