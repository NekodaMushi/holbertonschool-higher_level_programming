#!/usr/bin/python3
"""Divides 2 integers and prints the result"""


def safe_print_division(a, b):
    try:
        res = a / b
    except:
        res = None
    finally:
        print("Inside result: {}".format(res))
    return res
