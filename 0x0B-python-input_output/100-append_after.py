#!/usr/bin/python3

"""This module cotains the function that inserts a line
of text to a file, after each line containing a specific string."""


def append_after(filename="", search_string="", new_string=""):
    """This function inserts a line of text to a file,
    after each line containing a specific string.
    Args:
        filename (str): The file to be read from and written to.
        search_string (str): The string to be searched for in the file.
        new_string (str): The string to be inserted after each line
        containing the search string.
    """
    with open(filename, mode="r+", encoding="utf-8") as f:
        new_text = ""
        for line in f:
            new_text += line
            if search_string in line:
                new_text += new_string
        f.seek(0)
        f.write(new_text)
