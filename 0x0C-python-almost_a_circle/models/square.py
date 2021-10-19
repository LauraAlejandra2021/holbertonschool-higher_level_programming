#!/usr/bin/python3
"""
Create square
class that inherits
from rectangle class
"""


from models.rectangle import Rectangle
""" import class"""


class Square(Rectangle):
    """ new class"""
    
    def __init__(self, size, x=0, y=0, id=None):
        """constructor method square
        """
      