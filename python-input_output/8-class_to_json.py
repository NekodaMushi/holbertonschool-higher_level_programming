#!/usr/bin/python3
"""Learn to Play With Json File"""


def class_to_json(obj):
    """returns the dictionary description
    with simple data structure
    for JSON serialization of an object
    """

    return vars(obj)
