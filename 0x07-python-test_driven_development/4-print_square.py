#!/usr/bin/python3
"""
this function prints
a square, taking
only whole numbers
"""


def print_square(size):

    """
    this function prints a square
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) is not int and size < 0:
        raise TypeError("size must be an integer")
    for i in range(size):
        for j in range(size):
            print("#", end='')
        print("")
