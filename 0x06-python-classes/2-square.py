#!/usr/bin/python3
"""square constructor and error handling"""


class Square:
    """square constructor"""

    def __init__(self, size=0):
        """ private square constructor and error handling """
        self.__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer ")
        if size < 0:
            raise ValueError("size must be >= 0")
