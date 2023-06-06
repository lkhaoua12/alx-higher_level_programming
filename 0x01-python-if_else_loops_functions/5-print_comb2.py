#!/usr/bin/python3
"""
print numbers from 0 - 99 in 2 digit int.
"""
for i in range(100):
    print("{:02d}".format(i), end=', ' if i < 99 else '\n')
