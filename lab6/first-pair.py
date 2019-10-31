#!/usr/bin/env python


s = raw_input()


i = 1
while i < len(s) and s[i - 1] != s[i]:
    i += 1

if i < len(s):
    # found one!
    print s[i] * 2
