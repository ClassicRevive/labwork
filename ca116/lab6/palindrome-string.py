#!/usr/bin/env python


s = raw_input()

i = 0
while (i < (len(s) / 2) + 1) and (s[i] == s[-i - 1]):
    i += 1

if i == (len(s) / 2) + 1:
    print "palindrome"
