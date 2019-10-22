#!/usr/bin/env python


line1 = raw_input()
line2 = raw_input()
line3 = raw_input()

if len(line1) > len(line2) and len(line1) > len(line3):
    print line1
elif len(line2) > len(line1) and len(line2) > len(line3):
    print line2
else:
    print line3
