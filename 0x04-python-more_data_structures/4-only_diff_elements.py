#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    """
    Returns a set of all elements present in only one set.

    :param set_1: First set
    :param set_2: Second set
    :return: Set of elements in only one set
    """

    return set_1 ^ set_2
