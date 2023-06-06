#!/usr/bin/python3
"""
Get the last digit of a number and check its range.
"""
import random

number = random.randint(-10000, 10000)
original_number = number

if number < 0:
    number = number * -1

last_digit = number % 10

if last_digit > 5:
    print(f"Last digit of {original_number} is {last_digit} and is greater than 5")
elif last_digit == 0:
    print(f"Last digit of {original_number} is {last_digit} and is zero")
else:
    print(f"Last digit of {original_number} is {last_digit} and is less than 6 and not 0")

