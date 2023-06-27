#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    result = 0
    try:
        result = fct(*args)
        print(result)
    except Exception as e:
        result = None
        print("Exception: ", end="", file=sys.stderr)
        print(e, file=sys.stderr)
    return result


if __name__ == "__main__":
    def my_div(a, b):
        return a / b

    result = safe_function(my_div, 10, 2)
    print("result of my_div: {}".format(result))
    result = safe_function(my_div, 10, 0)
    print("result of my_div: {}".format(result))

    def print_list(my_list, len):
        i = 0
        while i < len:
            print(my_list[i])
            i += 1
        return len

    result = safe_function(print_list, [1, 2, 3, 4], 10)
    print("result of print_list: {}".format(result))
