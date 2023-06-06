#!/usr/bin/python3
"""
print all ascii alphebt in lower case except e and q.
"""
for i in range(97, 123):
    if chr(i) == 'q' or chr(i) == 'e':
        continue
    else:
        print("{}".format(chr(i)), end='')
