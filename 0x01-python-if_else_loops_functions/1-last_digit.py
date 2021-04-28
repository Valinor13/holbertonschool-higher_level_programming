#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
print("Last digit of", number, "is", end=" ")
if number % 10 == 0:
    print(number % 10, "and is 0")
elif number < 0:
    number *= -1
    print("-{:d}".format(number % 10), "and is less than 6 and not 0")
elif number % 10 > 5:
    print(number % 10, "and is greater than 5")
else:
    print(number % 10, "and is less than 6 and not 0")
