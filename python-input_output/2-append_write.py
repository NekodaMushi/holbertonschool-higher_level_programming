#!/usr/bin/python3
"""Function reading file
Returns: Nb of characters"""


def append_write(filename="", text=""):
    """Open file and display nb of char"""
    with open(filename, mode='a', encoding="UTF8") as testa:
        testa.write(text)
        return len(text)
