#!/usr/bin/env python

curr = 0
prev = input()
if prev != 0:
    curr = input()

while curr != 0:
    if prev < curr:
        print "higher"
    elif prev > curr:
        print "lower"
    else:
        print "equal"

    prev = curr
    curr = input()
