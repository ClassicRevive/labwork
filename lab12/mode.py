#!/usr/bin/env python


a = []

s = raw_input()
while s != "end":
    a.append(int(s))
    s = raw_input()

# print a

i = 1
while i < len(a):
    v = a[i]
    p = i
    while 0 < p and v < a[p - 1]:
        a[p] = a[p - 1]

        p -= 1

    a[p] = v

    i += 1

# print a

max_count = 1
mode = 0

j = 0
while j < len(a) - 1:
    count = 1
    # print j
    while j < len(a) - 1 and a[j] == a[j + 1]:
        count += 1
        j += 1

    if max_count < count:
        max_count = count
        mode = a[j]

    j += 1

print mode, max_count
