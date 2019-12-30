#!/usr/bin/env python

from math import sqrt

x1 = input()
y1 = input()
r1 = input()

x2 = input()
y2 = input()
r2 = input()

if sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2) - (r1 + r2) >= 0:
    print "no"
else:
    print "yes"
