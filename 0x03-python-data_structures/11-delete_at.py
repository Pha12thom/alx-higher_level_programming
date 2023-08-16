#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    new_list = ""
    for num in my_list:
        if idx < 0 or len(my_list):
            return my_list
        return my_list[:idx] + my_list[idx+1:]
