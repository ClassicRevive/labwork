#!/usr/bin/env python


a = []
s = raw_input()
while s != "end":
    a.append(int(s))
    s = raw_input()

if len(a) != 0:
    i = 0
    stack = 1
    while i < len(a):
        count = 1
        j = i + 1

        b = a[i]
        while j < len(a):
            if a[j] - b < 1000:
                count += 1
            j += 1

        if stack < count:
            stack = count

        i += 1

    print stack
else:
    print 0
