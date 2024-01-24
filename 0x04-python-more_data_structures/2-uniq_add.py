#!/usr/bin/python3

def uniq_add(my_list=[]):
    """
    Adds all unique integers in a list (only once for each integer).

    :param my_list: List of integers
    :return: Sum of unique integers
    """
    return sum(set(my_list))
