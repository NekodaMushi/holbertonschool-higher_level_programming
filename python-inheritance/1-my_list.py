#!/usr/bin/python3
"""First time creating class which inherits"""


class MyList(list):
    """Class Inheriting from list"""

    def print_sorted(self):
        """Method printing a sorted list"""
        print(sorted(self))
