#!/usr/bin/env python


prev = input()

i = 0
while i < 5:
    curr = input()
    if prev < curr:
        print "higher"
    elif prev > curr:
        print "lower"
    else:
        print "equal"

    prev = curr
    i += 1
