#!/usr/bin/python3


"""Defiens the load_from_json_file function"""


def load_from_json_file(filename):
    """Function that creates an Object from a “JSON file”"""
    with open(filename, "r") as file:
        import json

        return json.load(file)
