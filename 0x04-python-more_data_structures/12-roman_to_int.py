#!/usr/bin/python3
numerals = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
}


def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) != str:
        return 0

    i = 0
    integer = 0
    st = roman_string

    while i < len(st):
        ch1 = numerals[st[i]]
        if i + 1 < len(st):
            ch2 = numerals[st[i + 1]]
            if (ch1 >= ch2):
                integer += ch1
                i += 1
            else:
                integer -= ch1
                i += 1
        else:
            integer += ch1
            i += 1

    return integer
