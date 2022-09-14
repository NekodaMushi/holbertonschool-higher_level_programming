#!/usr/bin/python3
"""returns a new dictionary with all keys multiplied by 2"""


def multiply_by_2(a_dictionary):
    for key in a_dictionary:
        return {key: a_dictionary[key] * 2}
