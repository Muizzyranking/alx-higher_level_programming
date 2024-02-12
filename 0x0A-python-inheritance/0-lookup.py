#!/usr/bin/python3
"""Module for lookup function."""


def lookup(obj):
    """Function that returns the list of available attributes
    and methods of an object.

    args:
    obj: object to look up

    returns:
    list of available attributes and methods of an object.
    """
    return dir(obj)
