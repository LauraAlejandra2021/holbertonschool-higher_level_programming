#!/usr/bin/python3
"""square area"""


class Square:
    """Class crate  a Square """
    @property
    def size(self):
        """ return a size"""
        return self.__size

    @size.setter
    def size(self, value):
        """get size"""
        self.__size = value

    def area(self):
        """return area square """
        return self.__size ** 2

    def __init__(self, size=0):
        """ private square constructor and error handling"""

        self.__size = size
        if type(size) != int:
            raise TypeError("size must be an integer ")

        elif size < 0:
            raise ValueError("size must be >= 0")