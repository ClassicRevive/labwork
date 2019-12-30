#!/usr/bin/env python


a = []

s = raw_input()
while s != "end":
    a.append(int(s))
    s = raw_input()

number = input()
a.append(number)

i = 1
while i < len(a):
    p = i
    v = a[i]
    while p > 0 and v < a[p - 1]:
        a[p] = a[p - 1]
        p -= 1

    a[p] = v

    i += 1

print a
