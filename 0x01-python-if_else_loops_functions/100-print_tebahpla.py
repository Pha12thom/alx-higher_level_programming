#!/usr/bin/python3
for c in range(ord('Z'), ord('A') - 1, -1):
    print("{:c}".format(c+32) if c % 2 == 0 else "{:c}".format(c), end='')
