#!/usr/bin/python3
"""This module gets line from standard input and print modified output.
"""
import sys
import signal


def handle_interrupt(signal, frame):
    print(f"File size: {tot_size}")
    for key in sorted(my_dict.keys()):
        print(f"{key}: {my_dict[key]}")
    raise KeyboardInterrupt
    sys.exit(0)


signal.signal(signal.SIGINT, handle_interrupt)

count = 0
tot_size = 0
all_stats = ("200", "301", "400", "401", "403", "404", "405", "500")
my_dict = {}
for line in sys.stdin:
    lst_line = line.split()
    count += 1
    tot_size += int(lst_line[8])
    if lst_line[7] in all_stats:
        my_dict[lst_line[7]] = my_dict.get(lst_line[7], 0) + 1
    if count == 10:
        print(f"File size: {tot_size}")
        for key in sorted(my_dict.keys()):
            print(f"{key}: {my_dict[key]}")
    if count == 10:
        count = 0
