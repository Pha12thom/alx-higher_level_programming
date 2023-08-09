#!/usr/bin/python3
def fizzbuzz(number):
    for number in range(101):
        if number % 3 == 0:
            print("Buzz", end=" ")
        if number % 3 ==0 and number % 5 == 0:
            print("FizzBuzz", end=" ")
