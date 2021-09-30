#!/usr/bin/python3
"""Class to Rectangle"""


class Rectangle:
    """Create a rectangle"""

    def __init__(self, width=0, height=0):
        """private rectangle constructor"""
        self.height = height
        self.width = width

    @property
    def width(self):
        """getter to retrieve the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter to get the width"""
        self.__width = value
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")

    @property
    def height(self):
        """crate  a Rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """ get height"""
        self.__height = value
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")

    def area(self):
        return self.height * self.width

    def perimeter(self):
        if self.__height == 0 or self.__width == 0:
            return 0
        return (self.__height + self.__width) * 2
