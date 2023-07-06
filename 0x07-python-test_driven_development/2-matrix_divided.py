#!/usr/bin/python3
"""
this module define a function that devide a matrix
"""


def matrix_divided(matrix, div):
    """
    function that divid a matrix by an int
    Args: matrix, div
    """

    if type(matrix) is not list or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    for row in matrix:
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for element in row:
            if type(element) not in [int, float]:
                raise TypeError("matrix must be a matrix (list of lists) of \
                integers/floats")
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(elem / div, 2)for elem in row] for row in matrix]

    


