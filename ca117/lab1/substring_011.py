#!/usr/bin/env python


import sys

for line in sys.stdin:
    [left, right] = [line.rstrip().split()]

    print(left.lower() in right.lower())
