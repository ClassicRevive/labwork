#!/usr/bin/env python


a = []

s = raw_input()
while s != "end":
    a.append(int(s))
    s = raw_input()

number = input()

if len(a) != 0:
    i = len(a) - 1
    while i != 0 and number < a[i - 1]:
        i -= 1

    if i == len(a) - 1:
        print len(a)
    else:
        print i
else:
    print 0
