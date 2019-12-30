#!/usr/bin/env python


s = raw_input()

i = 0
integer = ""
factor = ""
while i < len(s) and (s[i] != "."):
    integer = integer + s[i]
    i += 1

j = i
while j < len(s):
    factor = factor + s[j]
    j += 1

print integer
print factor[1:]
