#!/usr/bin/python3
import sys
argv = sys.argv
in_add = 0

if __name__ == "__main__":
    for i in range(1, len(argv)):
        in_add += int(argv[i])
    
    print("{}".format(in_add))
