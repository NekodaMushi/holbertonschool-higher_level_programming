#!/usr/bin/python3
"""prints the first x elements of a list and only integers."""


def safe_print_list_integers(my_list=[], x=0):
    nb = 0
    for x in range(x):
        try:
            print("{:d}".format(my_list[x]), end="")
            nb += 1
        except (ValueError, TypeError):
            continue
    print()
    return nb
