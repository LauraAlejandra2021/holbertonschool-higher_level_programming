#!/usr/bin/python3
"""
Generates an
undefined area
error
"""


class BaseGeometry:
    """
    Generates an undefined area error
    """
    def area(self):
        raise Exception("area() is not implemented")
