#!/usr/bin/env python

a = []

s = raw_input()
while s != "end":
    a.append(s)
    s = raw_input()

s = raw_input()
while s != "end":
    i = 0
    while i < len(a) and s != a[i][0:8]:
        i += 1

    if i < len(a):
        print a[i][9:]

    s = raw_input()
