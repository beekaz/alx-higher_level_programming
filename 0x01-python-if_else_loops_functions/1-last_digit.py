#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
number = str(number)
last_digit = int(number[-1])
number = int(number)
if number > 5:
    print(f" last dight of {number} is {last_digit} and is greater than 5")
elif number == 0:
    print(f"last dight of {number} is {last_digit} is 0 and is zero")
elif number  < 6 != 0:
    print(f"last digit of {number} is {last_digit} and is less than 6 and not 0")
