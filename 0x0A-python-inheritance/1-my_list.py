#!/usr/bin/python3
"""Module for my_list"""


class MyList(list):
    """Class that inherits from list and
    prints sorted list
    """

    def print_sorted(self):
        """Prints sorted list"""
        sorted_list = sorted(self)
        print(sorted_list)


my_list_instance = MyList([3, 1, 4, 1, 5, 9, 2, 6, 5])
sorted_list = my_list_instance.print_sorted()
sorted_list
