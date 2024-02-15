#!/usr/bin/python3
"""Defines the to_json_string function"""


def to_json_string(my_obj):
    """Returns the JSON representation of an object
    Args:
        my_obj: the object to represent
    Returns:
        the JSON representation of the object
    """
    import json

    return json.dumps(my_obj)
