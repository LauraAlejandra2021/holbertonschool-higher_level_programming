#!/usr/bin/python3
"""
this function divides
by a number int or float the
numbers of a matrix.
"""


def matrix_divided(matrix, div):
    """
    an int or a float divides the elements of a matrix
    """
    new_list = []
    len1 = len(matrix[0])

    for t in range(len(matrix)):
        for n in range(len(matrix[t])):
            if len(matrix[t]) != len1:
                raise TypeError("Each row of the matrix "
                                        "must have the same size")
    if isinstance(div, (int, float)) is False:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    for i in range(len(matrix)):
        new_list.append([])
        for j in range(len(matrix[i])):
            # isinstance compares parameters and returns a boolean
            a = isinstance(matrix[i][j], (int, float))
            if a is False:
                raise TypeError("matrix must be a matrix (list of lists) "
                                        "of integers/floats")
            # round removes decimal places
            new_list[i].append(round(matrix[i][j]/div, 2))
    return new_list
