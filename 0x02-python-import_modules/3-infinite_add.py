#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    result = 0
    args_num = len(argv)
    for i in range(1, args_num):
        result += int(argv[i])
    print("{:d}".format(result))
