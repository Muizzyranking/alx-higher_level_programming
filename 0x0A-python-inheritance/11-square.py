#!/usr/bin/python3
"""Defines a square class."""

rectangle = __import__("9-rectangle").Rectangle


class Square(rectangle):
    """Represent a square."""

    def __init__(self, size):
        """Initialize a new square.
        Args:
            size (int): size of the new square.
        """
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """Return the printable representation of the square."""
        return "[Square] {}/{}".format(self.__size, self.__size)
