#!/usr/bin/python3
"""find peak"""


def find_peak(list_of_integers):
    """Finds a peak in a list of unsorted integers."""
    if not list_of_integers:
        return None

    if len(list_of_integers) == 1:
        return list_of_integers[0]

    mid = len(list_of_integers) // 2

    if list_of_integers[mid] >= list_of_integers[mid - 1] \
            and list_of_integers[mid] >= list_of_integers[mid + 1]:
        return list_of_integers[mid]

    # Check if peak is in the left half
    if mid > 0 and list_of_integers[mid - 1] > list_of_integers[mid]:
        return find_peak(list_of_integers[:mid])

    # Peak must be in the right half
    return find_peak(list_of_integers[mid + 1:])
