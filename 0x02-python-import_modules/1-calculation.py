#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div

    a, b = 10, 5
    operations = {'add': add, 'sub': sub, 'mul': mul, 'div': div}

    for op, func in operations.items():
        result = func(a, b)
        print(f"{a} {op} {b} = {result}")
