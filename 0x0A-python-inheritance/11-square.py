#!/usr/bin/python3
"""
class that inherits the class rectanglesquare2
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
       a new class
    """
    def __init__(self, size):
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)
