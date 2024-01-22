#!/usr/bin/python3
def no_c(my_str):
    new_str = ""
    for lmts in my_str:
        if lmts != "c" and lmts != "C":
            new_str += lmts
    return new_str
