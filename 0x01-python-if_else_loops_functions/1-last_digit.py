#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)
last_digit = number % 10 if number >= 0 else -(-number % 10)

message = "Last digit of {} is {} and is".format(number, last_digit)

if last_digit > 5:
    print("{} greater than 5".format(message))
elif last_digit == 0:
    print("{} 0".format(message))
else:
    print("{} less than 6 and not 0".format(message))
