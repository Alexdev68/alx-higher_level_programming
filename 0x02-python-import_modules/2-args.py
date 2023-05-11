#!/usr/bin/python3
import sys
argv = sys.argv
no_args = len(argv)

if __name__ == "__main__":
    if len(argv) - 1 > 1:
        print("{} arguments:".format(no_args - 1))
    if len(argv) - 1 == 0:
        print("{} arguments.".format(no_args - 1))
    if len(argv) - 1 == 1:
        print("{} argument:".format(no_args - 1))

    for i in range(1, no_args):
        print("{}: {}".format(i, argv[i]))
