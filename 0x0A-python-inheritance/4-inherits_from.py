#!/usr/bin/python3
"""Defines inherited class checking funtion"""


def inherits_from(obj, a_class):
    """checks if an objects is an inherited instance of a class
    Args:
        obj: Object to check
        a_class: the class to check against

    Returns:
        True: if the object is an inherited instance of the class
        False: otherwise
    """
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    return False
