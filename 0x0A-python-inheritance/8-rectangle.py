#!/usr/bin/python3
"""
function that inherits
a class to use
its method
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
       a new class
    """

    def __init__(self, width, height):
        """
            verifying with the method integer validator
        """
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)
