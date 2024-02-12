#!/usr/bin/python3
"""Module for my_list"""


class MyList(list):
    """Class that inherits from list and
    prints sorted list
    """

    def print_sorted(self):
        """Prints sorted list"""
        print(sorted(self))
