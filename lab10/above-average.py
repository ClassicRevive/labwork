#!/usr/bin/env python

a = []

s = raw_input()
while s != "end":
    a.append(int(s))
    s = raw_input()

total = 0
i = 0
while i < len(a):
    total += a[i]
    i += 1

if len(a) != 0:
    average = float(total) / len(a)
# print average

j = 0
while j < len(a):
    if a[j] > average:
        print a[j]
    j += 1
