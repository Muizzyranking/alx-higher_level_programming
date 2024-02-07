#!/usr/bin/python3
"""Module for add_integer
    can only add integers or floats
    otherwise raise a TypeError
    return the sum of a and b
"""


def add_integer(a, b=98):
    """adds two integers
    @a: first integer
    @b: second integer"""
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
