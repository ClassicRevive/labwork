#!/usr/bin/env python


s = raw_input()
t = ""

i = 0
while i < len(s):
    # do something
    t = t + s[len(s) - i - 1]
    i += 1
print t
