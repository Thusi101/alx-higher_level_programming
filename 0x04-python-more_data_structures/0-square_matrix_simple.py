#!/usr/bin/python3

def compute_square_matrix(matrix=[]):
    """
    Computes the square value of all integers in a matrix.

    :param matrix: 2-dimensional array
    :return: New matrix with squared values
    """
    result_matrix = []
    for row in matrix:
        squared_row = [element ** 2 for element in row]
        result_matrix.append(squared_row)
    return result_matrix
