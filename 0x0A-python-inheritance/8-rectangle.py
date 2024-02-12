#!/usr/bin/python3

"""Defines a rectngle class."""

base_geometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(base_geometry):
    """Represent a rectangle."""

    def __init__(self, width, height):
        """Initialize a new rectangle.
        Args:
            width (int): width of the new rectangle.
            height (int): height of the new rectangle.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
