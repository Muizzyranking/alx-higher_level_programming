#!/usr/bin/python3
"""Module theat defines the function read_file"""


def read_file(filename=""):
    """Reads a text file (UTF8) and prints it to stdout

    Args:
        filename: text file name

    Prints:
        the content of the file
    """

    with open(filename, "r", encoding="utf-8") as file:
        print(file.read(), end="")
