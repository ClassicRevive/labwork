#!/usr/bin/env python


s = raw_input()

i = 0
while i < len(s) and (s[i] < "A" or "Z" < s[i]):
    i += 1

if i < len(s):
    # found one!
    j = i
    while j < len(s) and ("A" <= s[j] and s[j] <= "Z"):
        j += 1

    print s[i:j], i
