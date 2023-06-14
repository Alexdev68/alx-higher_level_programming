#!/usr/bin/python3
"""This module gets line from standard input and print modified output.
"""
import sys
import signal


def interrupter(signal, frame):
    print(f"File size: {tot_size}")
    for key in sorted(my_dict.keys()):
        print(f"{key}: {my_dict[key]}")
    sys.exit(0)


signal.signal(signal.SIGINT, interrupter)

count = 0
tot_size = 0
my_dict = {}
for line in sys.stdin:
    lst_line = line.split()
    count += 1
    tot_size += int(lst_line[8])
    my_dict[lst_line[7]] = my_dict.get(lst_line[7], 0) + 1
    if count == 10:
        print(f"File size: {tot_size}")
        for key in sorted(my_dict.keys()):
            print(f"{key}: {my_dict[key]}")
    if count == 10:
        count = 0
