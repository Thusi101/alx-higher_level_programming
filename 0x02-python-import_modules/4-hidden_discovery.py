#!/usr/bin/python3
if __name__ == "__main__":
    # Importing all names from hidden_4 module
    from hidden_4 import *

    # Get names defined in the module
    names = dir()

    # Print sorted names that do not start with __
    for name in sorted(name for name in names if not name.startswith("__")):
        print("{}".format(name))
