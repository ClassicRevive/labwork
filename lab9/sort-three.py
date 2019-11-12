#!/usr/bin/env python


a = input()
b = input()
c = input()

ls = [a, b, c]

i = 0
while i < len(ls):
    j = ls[0]
    if ls[i] < j:
        # ls[0], ls[i] = ls[i], ls[0]
        j = ls[i]
    i += 1

if ls[1] > ls[2]:
    ls[1], ls[2] = ls[2], ls[1]

p = 0
while p < len(ls):
    print ls[p]
    p += 1
