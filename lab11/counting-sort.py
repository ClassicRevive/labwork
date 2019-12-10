#!/usr/bin/env python


import sys

a = []

s = raw_input()
while s != "end":
    a.append(int(s))
    s = raw_input()


# i = 1 all the way to i = 1000 need to be tested against each element
# the list but without using a nested loop

i = 0
while i < 1000:
    count = a.count(i)

    if 0 < count:
        print (str(i) + "\n") * count,

    i += 1
