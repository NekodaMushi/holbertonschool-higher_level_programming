#!/usr/bin/python3
"""function that finds the biggest integer of a list."""


def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    for i in my_list:
        maxi = my_list[0]
        if my_list[i] > maxi:
            maxi = my_list[i]
        return maxi
