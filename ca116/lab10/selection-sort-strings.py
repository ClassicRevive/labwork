#!/usr/bin/env python


a = []

s = raw_input()
while s != "end":
    a.append(s)
    s = raw_input()

i = 0
while i < len(a):
    p = i
    j = i + 1
    while j < len(a):
        if a[j] < a[p]:
            a[j], a[p] = a[p], a[j]

        j += 1
    i += 1


j = 0
while j < len(a):
    print a[j]
    j += 1