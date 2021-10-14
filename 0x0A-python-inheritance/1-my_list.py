#!/usr/bin/python3
"""
This function
inherits a list
to a class
"""


class MyList(list):
    """
    this class prints a list in ascending order
    """

    def print_sorted(self):
        print(sorted(self))
# sorted  retun a list in ascending order
