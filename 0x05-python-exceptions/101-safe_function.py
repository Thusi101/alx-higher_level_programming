#!/usr/bin/python3
import sys


def safe_function(fuct, *args):
    try:
        result = fuct(*args)
        return result
    except (ValueError, ZeroDivisionError, TypeError, IndexError):
        print("Exception: {}".format(sys.exec_info()[1]), file=sys.stderr)
        return None
