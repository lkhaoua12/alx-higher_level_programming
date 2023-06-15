#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string:
        return 0
    result = 0
    prev_value = 0
    a_dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M':1000}
    for value in roman_string:
        if value not in a_dic.keys():
            return 0
        elif a_dic[value] > prev_value:
            result += a_dic[value] - prev_value * 2 
        else:
            result += a_dic[value] 
        prev_value = a_dic[value]
    return result

if __name__ == "__main__":
    roman_number = "X"
    print("{} = {}".format(roman_number, roman_to_int(roman_number)))

    roman_number = "VII"
    print("{} = {}".format(roman_number, roman_to_int(roman_number)))

    roman_number = "IX"
    print("{} = {}".format(roman_number, roman_to_int(roman_number)))

    roman_number = "LXXXVII"
    print("{} = {}".format(roman_number, roman_to_int(roman_number)))

    roman_number = "DCCVII"
    print("{} = {}".format(roman_number, roman_to_int(roman_number)))
