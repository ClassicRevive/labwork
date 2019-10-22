#!/usr/bin/env python


s = raw_input()

i = 0
while i < len(s) and (s[i] < "A" or "Z" < s[i]):
    i += 1

if i < len(s):
    print s[i], i
