#!/usr/bin/env python

a = []

s = raw_input()
while s != "end":
    a.append(int(s))
    s = raw_input()

i = 0
while i < 10:
    print i, ("*" * a.count(i))
    i += 1
