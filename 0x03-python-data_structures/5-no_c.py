#!/usr/bin/python3
def no_c(my_string):
    c_no = ""
    for char in my_string:
        if char != "c" and char != "C":
            c_no += char
    return c_no
