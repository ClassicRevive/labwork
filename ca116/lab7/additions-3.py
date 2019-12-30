#!/usr/bin/env python

total = 0
while total != 1000:
    s = raw_input()

    i = 0
    while i < len(s) and s[i] != "+":
        i += 1

    total = int(s[:i]) + int(s[i + 1:])
    print total
