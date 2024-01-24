#!/usr/bin/python3
"""
    Computes the square value of all integers in a matrix.

    :param matrix: 2-dimensional array
    :return: New matrix with squared values
    """
def square_matrix_simple(matrix=[]):
    return [[y ** 2 for y in x] for x in matrix]
