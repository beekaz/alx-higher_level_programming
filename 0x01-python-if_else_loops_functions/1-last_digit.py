#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number == 0:
    last = 0
elif number > 0:
    last = int(str(number)[-1])
else:
    last = -1 * (int(str(number)[-1]))
if last > 5:
    print(f"Last digit of {number} is {last} and is greater than 5")
elif last == 0:
    print(f"Last digit of {+number} is {last} and is 0")
elif last < 6 and last != 0:
    print(f"Last digit of {number} is {last} and is less than 6 and not 0")
