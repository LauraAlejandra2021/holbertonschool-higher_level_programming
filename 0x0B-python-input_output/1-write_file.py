#!/usr/bin/python3
"""
function that
reads aUTF8 file,
returns the number of characters
"""


def write_file(filename="", text=""):
    """
    function that reads a UTF8 f
    returns the number of characters
    """

    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
