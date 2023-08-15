#!/usr/bin/python3
def max_integer(my_list=[]):
    for num in my_list:
        if my_list is None:
            return None
        largest = my_list[0]
        if num > largest:
            return num
