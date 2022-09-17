#!/usr/bin/python3
"""Converts a Roman numeral to an integer."""


def roman_to_int(roman_string):
    if roman_string is None or isinstance(roman_string, int):
        return 0

    dic = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    decimal = 0
    
    for i in range(len(roman_string)):
        condition1 = i + 1 < len(roman_string)
        condition2 = dic[roman_string[i]] < dic[roman_string[i+1]]
        if condition1 and condition2:
            decimal -= dic[roman_string[i]]
        else:
            decimal += dic[roman_string[i]]
    return decimal
