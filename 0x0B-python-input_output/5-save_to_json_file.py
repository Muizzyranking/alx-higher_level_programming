#!/usr/bin/python3
"""Defienes the save_to_json_file function"""


def save_to_json_file(my_obj, filename):
    """Writes an object to a text file, using JSON representation"""
    import json

    with open(filename, "w") as f:
        json.dump(my_obj, f)
