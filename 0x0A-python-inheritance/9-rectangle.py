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
            constructor method
        """
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return ("[{}] {}/{}".format(self.__class__.__name__,self.__width, self.__height))
