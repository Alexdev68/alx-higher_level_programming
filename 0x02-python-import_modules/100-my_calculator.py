#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv
no_args = len(argv)

if __name__ == "__main__":

    operators = "+-*/"
    a = int(argv[1])
    sign = argv[2]
    b = int(argv[3])

    if no_args != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    if sign not in operators:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    if sign == '+':
        print(f"{a} + {b} = {add(a, b)}")
    if sign == '-':
        print(f"{a} - {b} = {sub(a, b)}")
    if sign == '*':
        print(f"{a} * {b} = {mul(a, b)}")
    if sign == '/':
        print(f"{a} / {b} = {div(a, b)}")
