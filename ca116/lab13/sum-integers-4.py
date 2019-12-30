#!/usr/bin/env python

# this code needs to loop through
# a list of number files and add all the numbers together
# in this case the numbers are seperated by space

import sys
filenames = sys.argv[1:]

i = 0
total = 0
while i < len(filenames):
    with open(filenames[i]) as num:
        s = num.read()
        s_split = s.split()
        j = 0
        while j < len(s_split):
            total += int(s_split[j])
            j += 1

    i += 1

print total
