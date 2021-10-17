#!/usr/bin/python3
"""
function that
reads a
UTF8 file
"""


def read_file(filename=""):
    """
    function that reads a UTF8 file
    """


    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
        
