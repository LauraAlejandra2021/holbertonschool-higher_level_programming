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

    mat1 = len(matrix[0])
    mat2 = len(matrix[1])
    new_list = []

    if mat1 != mat2:
        raise TypeError("Each row of the matrix must have the same size")

    if type(div) is not int and float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    for i in range(len(matrix)):
        new_list.append([])
        for j in range(len(matrix[i])):
            a = isinstance(matrix[i][j], (int, float)) #isinstance compares parameters and returns a boolean
            if a is False:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            new_list[i].append(round(matrix[i][j]/div, 2)) #round removes decimal places
    return new_list
