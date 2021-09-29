#!/usr/bin/python3
"""square area"""


class Square:
    """Class crate  a Square """
    @property
    def size(self):
        """ return a size"""
        return self.__size

    def my_print(self):
        i = 0
        j = 0
        self.new_method()

    def new_method(self):
        self.p = self.__size
        if self.p is 0:
            print('\n', end='')
        else:
            for i in range(0, self.p + 1):
                for j in range(0, self.p + 1):
                    print('#', end="")
                print('\n', end="")

    @size.setter
    def size(self, value):
        """get size"""
        self.__size = value

    def area(self):
        """Method that returns the area """
        return self.__size ** 2

    def __init__(self, size=0):
        """ private square constructor and error handling"""

        self.__size = size
        if type(size) != int:
            raise TypeError("size must be an integer ")

        elif size < 0:
            raise ValueError("size must be >= 0")
