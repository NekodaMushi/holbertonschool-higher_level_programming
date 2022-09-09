#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys

if __name__ == "__main__":
        
    n = len(sys.argv)

    if n != 3:
        print("Usage: {} <a> <operator> <b>".format(sys.argv[0]))
        sys.exit(1)

    elif sys.argv[2] not in ['+', '-', '*', '/']:
        print("Unknown operator. Available operators: +, -, * and /")

    else:
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        if sys.argv[2] == '+':
            print("{} {} {} = {}".format(a, sys.argv[2], b, add(a, b)))
        elif sys.argv[2] == '-':
            print("{} {} {} = {}".format(a, sys.argv[2], b, sub(a, b)))
        elif sys.argv[2] == '*':
            print("{} {} {} = {}".format(a, sys.argv[2], b, mul(a, b)))
        elif sys.argv[2] == '/':
            print("{} {} {} = {}".format(a, sys.argv[2], b, div(a, b)))
