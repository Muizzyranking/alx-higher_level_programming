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

    mid = len(list_of_integers) // 2
    peak = list_of_integers[mid]

    if peak > list_of_integers[mid - 1] and peak > list_of_integers[mid + 1]:
        return peak
    elif peak < list_of_integers[mid - 1] and peak > list_of_integers[mid + 1]:
        return find_peak(list_of_integers[:mid])
    else:
        return find_peak(list_of_integers[mid:])
