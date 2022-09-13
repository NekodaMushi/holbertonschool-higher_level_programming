#!/usr/bin/python3
"""adds all unique integers in a list (only once for each integer)"""


def uniq_add(my_list=[]):
    sum = 0
    new_list = []
    for i in my_list:
        if i not in new_list:
            new_list.append(i)

    for a in new_list:
        sum += a
    return sum
