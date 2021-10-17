#!/usr/bin/python3
"""
function that
append a UTF8 file,
and modify it
"""


def append_write(filename="", text=""):
    """
    append file and modify it
    """

    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
