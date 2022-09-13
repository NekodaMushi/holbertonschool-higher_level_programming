#!/usr/bin/python3
"""Replaces all occurrences of an element by another in a new list."""


def search_replace(my_list, search, replace):
    new_list = my_list.copy()
    for i in range(len(my_list)):
        if my_list[i] == search:
            new_list[i] = replace
    return new_list
