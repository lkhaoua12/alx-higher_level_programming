#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    uniq_set = {elem for elem in set_1 if elem not in set_2}
    uniq_set = uniq_set.union({elem for elem in set_2 if elem not in set_1})
    return uniq_set
