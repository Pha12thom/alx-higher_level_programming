#!/usr/bin/python3
def safe_print_integer(value):
    try:
        if True:
            print("{:d}".format(value))
        else:
            return false
    except Exception as e:
        print(f"{e}")
        exit()
