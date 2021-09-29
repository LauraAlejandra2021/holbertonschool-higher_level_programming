#!/usr/bin/python3
'''Class to Rectangle'''


class Rectangle:
    '''This class is create a rectangle'''

    def __init__(self, width=0, height=0):
        '''Inicialization of width and height'''
        self.__height = height
        self.__width = width

    @property
    def width(self):
        '''getter to retrieve the width'''
        return self.__width

    @width.setter
    def width(self, value):
        '''setter to get the size'''
        self.__width = value
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")

    @property
    def height(self):
        '''getter to retrieve the height'''
        return self.__height

    @height.setter
    def height(self, value):
        '''setter to get the size'''
        self.__height = value
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
