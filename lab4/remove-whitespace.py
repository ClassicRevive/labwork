#!/usr/bin/env python


s = raw_input()
t = ""

i = 0
while i < len(s):
    # do something
    if s[i] != " ":
        t += s[i]

    i += 1

print t
