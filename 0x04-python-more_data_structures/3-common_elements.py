#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    diff_elements = set()

    for i in set_1:
        if i not in set_2:
            diff_elements.add(i)

    for i in set_2:
        if i not in set_1:
            diff_elements.add(i)

    return diff_elements
