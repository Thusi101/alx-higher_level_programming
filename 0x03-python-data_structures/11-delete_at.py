#!/usr/bin/python3
def delete_at(my_lst=[], idex=0):
    if idex < 0:
        return my_lst
    elif idex >= len(my_lst):
        return my_lst
    del my_lst[idex]
    return my_lst
