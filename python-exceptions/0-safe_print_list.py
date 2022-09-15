#!/usr/bin/python3
"""function that prints x elements of a list"""


def safe_print_list(my_list=[], x=0):
    nb = 0
    for x in range(x):
        try:
            print(f"{my_list[x]}", end="")
            nb += 1
        except IndexError:
            break
    print("")
    return nb
