#!/usr/bin/env python

"""
this code will take an input and slice off the last number
if the last number = 1, print "st"
if it = 2, "nd"
if it = 3, "rd"

"""
n = input()

if n == 11 or n == 12 or n == 13:
    print "th"
elif n % 10 == 1:
    print "st"
elif n % 10 == 2:
    print "nd"
elif n % 10 == 3:
    print "rd"
else:
    print "th"
