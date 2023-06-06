#!/usr/bin/python3
"""
print numbers from 0 - 98 in 2 digit int.
"""
for i in range(0, 99):
    print("{:02d}, ".format(i), end='')

print("{:02d}".format(99))
