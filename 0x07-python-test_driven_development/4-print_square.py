#!/usr/bin/python3
"""Module containing a function that prints a square"""


def print_square(size):
    """adds integers
    Arguments:
        @size: size of the square
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size == 0:
        return
    for _ in range(size):
        for _ in range(size):
            print("#", end="")
        print()
