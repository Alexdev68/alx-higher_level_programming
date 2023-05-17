#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sort = sorted(a_dictionary.items())
    my_dict = dict(sort)

    for i in my_dict:
        print(i, ':', my_dict[i])
