#!/usr/bin/env python


a = []

s = raw_input()
while s != "end":
    a.append(int(s))
    s = raw_input()

i = 1
while i < len(a):
    v = a[i]
    p = i

    # print "v =", v, 0 < p, v < [p - 1]
    while 0 < p and v < a[p - 1]:
        # print a[p - 1], a[p]
        a[p] = a[p - 1]
        # print a
        p -= 1

    # print "p =", p
    a[p] = v

    i += 1

j = 0
while j < len(a):
    print a[j]
    j += 1
