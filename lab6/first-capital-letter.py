#!/usr/bin/env python


n = raw_input()

i = 0

char = n[i]
while char < "A" or "Z" < char:
    i += 1
    char = n[i]

print i
