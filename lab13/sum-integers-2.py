#!/usr/bin/env python


import sys
filename = sys.argv[1]

with open(filename) as num:
    total = 0

    s = num.readline()
    while 0 < len(s):
        total += int(s)
        s = num.readline()

    print total
