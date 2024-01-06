#!/usr/bin/python3
def no_c(my_string):
    """Removes all the characters c and C from a string"""
    new_str = ""
    for char in my_string:
        if char not in ["c", "C"]:
            new_str += char
    return new_str
