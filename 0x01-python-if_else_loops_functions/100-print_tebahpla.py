#!/usr/bin/python3
for c in range(ord('a'), ord('z') - 1, -1):
    print("{:c}".format(c - 32) if c % 2 == 0 else "{:c}".format(c), end='')

