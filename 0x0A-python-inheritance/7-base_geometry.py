#!/usr/bin/python3
"""Defines a class BaseGeometry."""


class BaseGeometry:
    """Represensts a BaseGeometry"""

    def area(self):
        """Area of the geometry"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value.
        Args:
            name (str): name.
            value (int): value.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less or equal to 0.
        """
        if isinstance(value, int) is False:
            raise TypeError("{} must be an integer".format(name))
        if value < 0:
            raise ValueError("{} must be greater than 0".format(name))
