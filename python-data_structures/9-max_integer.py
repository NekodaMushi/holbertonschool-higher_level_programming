#!/usr/bin/python3
"""function that finds the biggest integer of a list."""


def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    maxi = my_list[0]
    for i in my_list:
        if my_list[i] > maxi:
            maxi = my_list[i]
        return maxi

#You could get the same result by sorting 
# the list then retrieve the last element of list
