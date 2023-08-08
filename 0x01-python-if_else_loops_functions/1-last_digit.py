#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)

# Extract the last digit of the number
last_digit = abs(number) % 10

# Determine the condition based on the last digit
if last_digit > 5:
    condition = "and is greater than 5"
elif last_digit == 0:
    condition = "and is 0"
else:
    condition = f"and is less than 6 and not 0"
    print(f"The string Last digit of, {number} is, {last_digit}, {condition}")
