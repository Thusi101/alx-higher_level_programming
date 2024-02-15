#!/usr/bin/python3
"""
This is the matrix_divided module.

This module supplies one function, matrix_divided().
"""


def matrix_divided(matrix, div):
    """
    Return a new matrix where each element has been divided by div.

    Args:
        matrix (list): List of lists of integers or floats.
        div (int, float): The divider, must be >= 0.
    """
    matrix_type_error = 'Matrix must be a matrix of integers/floats'
    matrix_length_error = 'Each row of the matrix must have the same size'
    div_type_error = 'Divider must be a number'
    div_zero_error = 'Division by zero is not allowed'

    if not isinstance(matrix, list)
    or not all(isinstance(row, list) for row in matrix):
        raise TypeError(matrix_type_error)

    if not all(isinstance(num, (int, float)) for row in matrix for num in row):
        raise TypeError(matrix_type_error)

    if any(len(row) != len(matrix[0]) for row in matrix):
        raise TypeError(matrix_length_error)

    if not isinstance(div, (int, float)):
        raise TypeError(div_type_error)

    if div == 0:
        raise ZeroDivisionError(div_zero_error)

    return [[round(num / div, 2) for num in row] for row in matrix]
