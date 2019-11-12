#!/usr/bin/env python

a = []
b = []

s = raw_input()
while s != "end":
    a.append(int(s))
    s = raw_input()

t = raw_input()
while t != "end":
    b.append(int(t))
    t = raw_input()

c = a + b

i = 0
while i < len(c):
    p = i
    j = i + 1
    while j < len(c):
        if c[p] > c[j]:
            c[p], c[j] = c[j], c[p]
        j += 1
    i += 1

k = 0
while k < len(c):
    print c[k]
    k += 1
