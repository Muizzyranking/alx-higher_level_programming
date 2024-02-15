#!/usr/bin/python3
"""Defines from_json_string function"""


def from_json_string(my_str):
    """Returns an object
    Args:
        my_str: string
    Returns:
        an object
    """
    import json

    return json.loads(my_str)
