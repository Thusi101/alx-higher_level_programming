#!/usr/bin/python3

def common_elements(set_1, set_2):
    """
    Returns a set of common elements in two sets.

    :param set_1: First set
    :param set_2: Second set
    :return: Set of common elements
    """
    return set_1 & set_2

# Example usage:
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
common_elements_set = common_elements(set_a, set_b)
print(common_elements_set)

