#!/usr/bin/python3
"""
this function defines
if an object belongs
to a subclass
"""


def is_kind_of_class(obj, a_class):
    """
    function that compares an object with subclass
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
