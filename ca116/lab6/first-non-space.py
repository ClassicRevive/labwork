#!/usr/bin/env python


s = raw_input()

i = 0
while i < len(s) and (s[i] == " "):
    i += 1

if i < len(s) and i > 0:
    print i
else:
    print -1
