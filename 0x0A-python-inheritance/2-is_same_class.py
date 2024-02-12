#!/usr/bin/python3

"""Module that checks if the object is exactly an instance of a class"""


def is_same_class(obj, a_class):
    """Function that checks if obj is exactly an instance of a_class"""
    return type(obj) == a_class
