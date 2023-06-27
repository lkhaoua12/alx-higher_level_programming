#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    boal = True
    try:
        print("{:d}".format(value))
    except ValueError as ve:
        print(ve, file=sys.stderr)
        boal = False

    return boal


if __name__ == "__main__":
    value = 89
    has_been_print = safe_print_integer_err(value)
    if not has_been_print:
        print("{} is not an integer".format(value))

    value = -89
    has_been_print = safe_print_integer_err(value)
    if not has_been_print:
        print("{} is not an integer".format(value))

    value = "School"
    has_been_print = safe_print_integer_err(value)
    if not has_been_print:
        print("{} is not an integer".format(value))
