#!/usr/bin/python3
"""Module that defines the write_file function"""


def write_file(filename="", text=""):
    """Writes a string to a text file (UTF8)

    Returns:
        the number of characters written
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
