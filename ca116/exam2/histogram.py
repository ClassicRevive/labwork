#!/usr/bin/env python

import random

a = []

s = raw_input()
while s != "end":
    a.append(int(s))
    s = raw_input()

i = 0
maximum = 0
while i < len(a):
    if maximum < a[i]:
        maximum = a[i]

    i += 1


j = 0
while j < maximum:
    # build each row based on spaces or "***"
    # algorithm is as follows

    row = ""
    k = 0
    while k < len(a):
        if j + a[k] < maximum:
            row = row + "   "
        else:
            row = row + "***"

        k += 1

    print "|" + row

    j += 1

# print " " * len(a)
# print " " * len(a)
print "|" + ("-" * (len(a) * 3))
