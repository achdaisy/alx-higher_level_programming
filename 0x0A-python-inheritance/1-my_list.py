#!/usr/bin/python3
"""Defines class Mylist that inherits from list"""


class MyList(list):
    """defines a class that inherits from the built in list"""

    def print_sorted(self):
        """prints the list in acsending order"""
        print(sorted(self))
