#!/usr/bin/python3
"""Functions printing string"""


def say_my_name(first_name, last_name=""):
    """ Function checking if variables
    are strings
    
    Raises exception if not a string
    
    Print string
    
    Returns: Nothing """
    
    if type(first_name) is not str:
        raise("first_name must be a string")
    if type(last_name) is not str:
        raise("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))

