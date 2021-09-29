#!/usr/bin/python3
"""square area"""


class Square:
    """Square area"""
    def area(self):
        """Method that returns the area """
        return self.__size **2

    def __init__(self, size=0):
        """ private square constructor and error handling"""

        self.__size = size 
        if type(size) != int:
            raise TypeError("size must be an integer ")

        elif size < 0:
            raise ValueError("size must be >= 0")
