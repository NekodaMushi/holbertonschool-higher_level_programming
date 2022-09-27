#!/usr/bin/python3
"""Check if object is an instance 
of a class that inherited"""


def inherits_from(obj, a_class):
    """Method checking if object is instance"""
    return issubclass(type(obj), a_class) and type(obj) is not a_class
