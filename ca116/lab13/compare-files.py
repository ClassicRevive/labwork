#!/usr/bin/env python

import sys
first_file = sys.argv[1]
second_file = sys.argv[2]

# open both files and read each
# read as a whole, parse through
# count the newline chaacters as a line no system
# count position as distance from newline character
# when an anomaly is found, print the newline count and position

f = open(first_file)
s = open(second_file)
newline_count = 0
position = 0
fr = f.read()
sr = s.read()

i = 0
while i < len(fr) and i < len(sr) and sr[i] == fr[i]:
    if sr[i] == "\n" and fr[i] == "\n":
        newline_count += 1
        position = 0
    else:
        position += 1

    i += 1

if i < len(fr) or i < len(sr):
    print newline_count, position

f.close()
s.close()
