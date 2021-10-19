#!/usr/bin/python3
"""
create and inherit
classes, attribute definition
and attribute validation.
"""


from models.base import Base
""" import class"""


class Rectangle(Base):
    """ new class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """constructor method rectangle
        """

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """getter of width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter of width"""
        self.__width = value

        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

    @property
    def height(self):
        """getter of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter of height"""
        self.__height = value

        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")

    @property
    def x(self):
        """getter x"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter x"""
        self.__x = value

        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")

    @property
    def y(self):
        """getter y"""
        return self.__y

    @y.setter
    def y(self, value):
        """setter y"""
        self.__y = value

        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")

    def area(self):
        """new method, return area"""
        return(self.width * self.height)

    def display(self):
        """print rectangle"""

        for i in range (self.height):
            print("", end="")
            for j in range (self.width):
                print("#", end="")
            print(" ")
