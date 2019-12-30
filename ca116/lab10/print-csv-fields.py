#!/usr/bin/env python


a = []

s = raw_input()
while s != "end":
    a.append(s)
    s = raw_input()

t = input()
i = 0
while i < len(a):
    index = 0  # comma count
    j = 0

    # Linear search commas until index = t
    while index < t + 1:
        k = j
        while j < len(a[i]) and a[i][j] != ",":
            j += 1
        index += 1
        j += 1

    print a[i][k:j - 1]

    i += 1
