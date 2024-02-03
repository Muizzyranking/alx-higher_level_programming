#!/usr/bin/python3
"""Defines a class MagicClass"""
import math


class MagicClass:
    """Represents a circle"""

    def __init__(self, radius=0):
        self.__radius = 0
        if isinstance(radius, int) or isinstance(radius, float):
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        return (self.__radius**2) * math.pi

    def circumference(self):
        return 2 * math.pi * self.__radius
