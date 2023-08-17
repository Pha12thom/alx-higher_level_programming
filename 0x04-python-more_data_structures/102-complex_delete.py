#!/usr/bin/python3
def complex_delete(my_dict, value):
    to_del = []
    for key in my_dict:
        if my_dict[key] == value:
            to_del.append(key)
    for key in to_del:
        del my_dict[key]
    return my_dict
