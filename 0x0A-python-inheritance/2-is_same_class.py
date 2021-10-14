#!/usr/bin/python3
""""
function that tells me
if an objero is an
instance of a class

"""


def is_same_class(obj, a_class):
    """
    compare an object of a class
    """
    if type(obj) == a_class:
        return True
    else:
        return False
