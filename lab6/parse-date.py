#!/usr/bin/env python


s = raw_input()


i = 0
while i < len(s) and s[i] != " ":
    i += 1

j = i + 1
while j < len(s) and s[j] != " ":
    j += 1

k = j + 1
while k < len(s) and s[k] != " ":
    k += 1

l = k + 1

print s[j + 1:k - 1] + s[i:j] + ", " + s[l:] + " " + "(" + s[:i] + ")"
