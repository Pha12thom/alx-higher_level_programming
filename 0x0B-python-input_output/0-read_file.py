#!/usr/bin/python3
"""File reader"""
def read_file(filename=""):
    with open(filename, "r", encoding="UTF-8") as f:
        print(f, end="")
