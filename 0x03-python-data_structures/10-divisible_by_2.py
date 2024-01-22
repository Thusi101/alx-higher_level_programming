#!/usr/bin/python3
def divisible_by_2(my_lst=[]):
    new_lst = []
    if my_lst:
        for num in my_lst:
            new_lst.append(False if num % 2 else True)
        return new_lst
