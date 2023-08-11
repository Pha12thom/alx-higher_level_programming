#!/usr/bin/python3
if __name__ == "__main__":
    """import calculation modules"""
    from calculator_1 import add, sub, mul, div
    a = 10
    b = 5
    A = add(a, b)
    B = sub(a, b)
    C = mul(a, b)
    D = div(a, b)
    print("{} + {} = {}\n{} - {} = {}".format(a, b, A, a, b, B))
    print("{} * {} = {}\n{} / {} = {}".format(a, b, C, a, b, D))
