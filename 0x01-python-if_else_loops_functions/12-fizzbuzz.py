#!/usr/bin/python3
def fizzbuzz():
    for number in range(1, 101):
        result = (
            "Fizz" * (number % 3 == 0) +
            "Buzz" * (number % 5 == 0) or
            str(number)
        )
        print(f"{result} ", end="")
