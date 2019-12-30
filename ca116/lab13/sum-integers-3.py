#!/usr/bin/env python

# this code needs to loop through
# a list of number files and add all the numbers together
import sys
filenames = sys.argv[1:]

i = 0
total = 0
while i < len(filenames):

    with open(filenames[i]) as num:
        s = num.readline()
        while 0 < len(s):
            total += int(s)
            s = num.readline()

        i += 1

print total
