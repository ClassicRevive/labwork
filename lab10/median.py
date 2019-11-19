#!/usr/bin/env python


a = []

s = raw_input()
while s != "end":
    a.append(int(s))
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

<<<<<<< HEAD
=======
"""
if len(a) % 2 == 1:
    print a[(len(a) - 1) / 2]
elif len(a) % 2 == 0:
    if a[(len(a) - 1) / 2] < a[((len(a) - 1) / 2) + 1]:
        print a[((len(a) - 1) / 2) + 1]
    else:
        print a[(len(a) - 1) / 2]
"""
>>>>>>> master
print a[len(a) / 2]