#!/usr/bin/python3

def remove_char_at(str, n):
    mod_str = ''
    for i in range(len(str)):
        if i != n:
            mod_str += str[i]
    return mod_str
