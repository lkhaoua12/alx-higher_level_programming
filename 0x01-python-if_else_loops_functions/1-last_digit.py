#!/usr/bin/python3
"""
Get the last digit of a number and check its range.
"""
import random

number = random.randint(-10000, 10000)
original_number = number  # Store the original number

last_digit = abs(number) % 10

if last_digit > 5:
    if original_number > 0:
        print(f"Last digit of {original_number} is {last_digit} and is greater than 5")
    else:
        print(f"Last digit of {original_number} is -{last_digit} and is less than 6 and not 0")
elif last_digit == 0:
    print(f"Last digit of {original_number} is {last_digit} and is zero")
else:
    if original_number > 0: 
        print(f"Last digit of {original_number} is {last_digit} and is less than 6 and not 0")
    else:
        print(f"Last digit of {original_number} is -{last_digit} and is less than 6 and not 0")
