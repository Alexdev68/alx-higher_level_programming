#!/usr/bin/python3

for i in range(0, 9):
    for x in range(1, 10):
        if i == 8 and x == 9:
            continue
        print("{}{}, ".format(i, x), end='')
print("{}{}".format(8, 9))
