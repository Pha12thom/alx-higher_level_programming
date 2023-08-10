#!/usr/bin/python3
def uppercase(s):
    formatted_string = ""
    for c in s:
        formatted_string = "{}".format(chr(ord(c) - 32)) if 'a' <= c <= 'z' else c
        print("{}".format(formatted_string), end=" ")
