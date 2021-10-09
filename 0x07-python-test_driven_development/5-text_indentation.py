#!/usr/bin/python3
"""
this function tokenizes
a text according to
requirements
"""


def text_indentation(text):
    """tokenize a text"""
    if isinstance(text, str) is False:
        raise TypeError("text must be a string")

    for i in range(len(text)):
        if text[i] == ".":
            print(".\n")
        elif text[i] == "?":
            print('?\n')
        elif text[i] == ":":
            print(":\n")
        else:
            if (text[i] == " " and (text[i - 1]
                                    in ".?:" or text[i - 1] == " ")):
                continue
            print("{}".format(text[i]), end="")
