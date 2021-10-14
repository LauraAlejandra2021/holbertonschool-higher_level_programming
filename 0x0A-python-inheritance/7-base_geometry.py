#!/usr/bin/python3
"""
in this function we are
validating if value
is an integer

"""


class BaseGeometry:
    """
    verifications
    """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        self.name = name
        self.value = value
        if type(self.value) != int:
            raise TypeError("{} must be an integer".format(self.name))
        if self.value <= 0:
            raise ValueError("{} must be greater than 0".format(self.name))
