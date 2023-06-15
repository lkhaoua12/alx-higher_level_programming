#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    result = 0
    prev_value = 0
    a_dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    for value in roman_string:
        if value not in a_dic.keys():
            return 0
        elif a_dic[value] > prev_value:
            result += a_dic[value] - prev_value * 2
        else:
            result += a_dic[value]
        prev_value = a_dic[value]
    return result
