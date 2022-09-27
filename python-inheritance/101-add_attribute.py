#!/usr/bin/python3
"""Adds new attribute to an object
if it is possible"""


def add_attribute(ob, name, value):
    """Adds new attribute"""

    if not hasattr(ob, "__dict__"):
        raise TypeError("can't add new attribute")
    else:
        setattr(ob, name, value)
