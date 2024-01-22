#!/usr/bin/python3
def new_in_list(my_lst, idex, lmt):
    if idex < 0:
        return my_lst
    elif idex >= len(my_lst):
        return my_lst
    new_lst = list(my_lst)
    new_lst[idex] = lmt
    return new_lst
