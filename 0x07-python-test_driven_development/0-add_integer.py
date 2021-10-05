#!/usr/bin/python3
"""
this function adds
two numbers of type
int or float
"""


def add_integer(a, b=98):
    """
  pass parameters of another type to int or float
    """
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    if type(a) is not int:
        raise TypeError("a must be an integer")
    if type(b) is not int:
        raise TypeError("a must be an integer")
    return a+b
