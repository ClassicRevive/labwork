#!/usr/bin/env python


sum_count = 0
while sum_count < 10:
    s = raw_input()

    i = 0
    while i < len(s) and s[i] != "+":
        i += 1

    first = int(s[:i])
    second = int(s[i + 1:])
    print first + second

    sum_count += 1
