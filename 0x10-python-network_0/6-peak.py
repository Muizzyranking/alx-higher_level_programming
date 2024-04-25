#!/usr/bin/python3
"""find peak"""


def find_peak(list_of_integers):
    """find peak"""
    if not list_of_integers:
        return None
    if len(list_of_integers) == 1:
        return list_of_integers[0]
    if len(list_of_integers) == 2:
        return max(list_of_integers)

    return max(list_of_integers)
