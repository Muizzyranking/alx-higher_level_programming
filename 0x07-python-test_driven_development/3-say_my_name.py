#!/usr/bin/python3
"""Module containing a function to print first and last name"""


def say_my_name(first_name, last_name=""):
    """prints first and last name
    Arguments:
        @first_name: first name to be printed
        @second_name: last_name to be printed
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
