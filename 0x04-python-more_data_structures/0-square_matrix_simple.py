#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = [[]]
    for num in matrix:
        num = num**2
    new_matrix += num
    return new_matrix
