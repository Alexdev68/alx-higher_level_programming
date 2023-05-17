#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    change = sorted(a_dictionary.items())
    my_dict = dict(change)

    for i in my_dict:
        print("{}: {}".format(i, my_dict[i]))
