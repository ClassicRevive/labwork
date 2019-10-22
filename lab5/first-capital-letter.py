#!/usr/bin/env python


n = raw_input()

i = 0

char = n[i]
while char > "Z" or char < "A":
    i += 1
    char = n[i]

print i
