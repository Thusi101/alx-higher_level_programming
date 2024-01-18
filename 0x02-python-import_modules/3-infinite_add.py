#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    sumint = 0
    if len(argv) < 2:
        print("0")
    else:
        equate = sum(int(arg) for arg in argv[1:])
        print(equate)
