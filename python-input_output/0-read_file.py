#!/usr/bin/python3
"""Function reading file and printing to stdout"""


def read_file(filename=""):
    with open(filename, 'r', encoding="utf-8" ) as file:
        file = file.read()
        for fi in file:
            print(fi, end="")
