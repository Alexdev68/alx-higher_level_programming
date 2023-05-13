#!/usr/bin/python3
def multiple_returns(sentence):
    a = len(sentence)

    if a == 0:
        b = None
    else:
        b = sentence[0]

    tuple_weird = (a, b)
    return tuple_weird
