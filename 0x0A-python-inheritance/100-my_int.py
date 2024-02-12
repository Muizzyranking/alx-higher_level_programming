#!/usr/bin/python3

"""Defines a class MyInt."""


class MyInt(int):
    """A rebel version of int."""

    def __eq__(self, other):
        """Override equality."""
        return False

    def __ne__(self, other):
        """Override inequality."""
        return True
