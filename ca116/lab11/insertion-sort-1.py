#!/usr/bin/env python


a = []

s = raw_input()
while s != "end":
    a.append(int(s))
    s = raw_input()

v = input()

i = len(a) - 1
while i > 0 and v < a[i]:
    a[i - 1] = a[i]

    i -= 1

print i
