#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    print("{:d} arguments.".format(len(argv) - 1))
    for i in range(1, len(argv)):
        print("{}: {}".format(i, argv[i]))
