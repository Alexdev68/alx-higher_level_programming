#!/usr/bin/python3

def uppercase(str):
    lower = "abcdefghijklmnopqrstuvwxyz"
    complete_str = ''
    for i in str:
        if i not in lower:
            complete_str += i
        else:
            x = ord(i)
            convert = x - 32
            upper = chr(convert)
            complete_str += upper
    print("{}".format(complete_str))
