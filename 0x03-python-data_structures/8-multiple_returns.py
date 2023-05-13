#!/usr/bin/python3
def multiple_returns(sentence):
    a = len(sentence)
    b = sentence[0]

    if a == 0:
        sentence = None

    tuple_weird = (a, b)
    return tuple_weird
