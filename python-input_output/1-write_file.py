#!/usr/bin/python3
"""Function reading file
Returns: Nb of characters"""



def write_file(filename="", text=""):
    """Open file and display nb of char"""
    with open(filename, 'w', encoding="utf-8") as file:
        return len(text)
