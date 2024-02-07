#!/usr/bin/python3
"""Module to add two integers"""


def add_integer(a, b=98):
    """Function to add two integers"""
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
