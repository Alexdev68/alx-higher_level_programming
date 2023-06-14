#!/usr/bin/python3
"""This module gets line from standard input and print modified output.
"""
from sys import stdin

try:
    count = 0
    tot_size = 0
    all_stats = ("200", "301", "400", "401", "403", "404", "405", "500")
    my_dict = {}
    for line in stdin:
        if count == 10:
            print(f"File size: {tot_size}")
            for key in sorted(my_dict.keys()):
                print(f"{key}: {my_dict[key]}")
            count = 0
        count += 1
        lst_line = line.split()
        try:
            tot_size += int(lst_line[8])
            if lst_line[7] in all_stats:
                my_dict[lst_line[7]] = my_dict.get(lst_line[7], 0) + 1
        except Exception as ex:
            pass
    print(f"File size: {tot_size}")
    for key in sorted(my_dict.keys()):
        print(f"{key}: {my_dict[key]}")
except KeyboardInterrupt:
    print(f"File size: {tot_size}")
    for key in sorted(my_dict.keys()):
        print(f"{key}: {my_dict[key]}")
    raise
