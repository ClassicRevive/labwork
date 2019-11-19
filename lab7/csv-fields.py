#!/usr/bin/env python


s = raw_input()

j = 0
i = 0

while i < len(s):
    while j < len(s) and s[j] != ",":  # find comma
        j += 1

    print s[i:j]

    i = j + 1  # assign new index for linear search
    j += 1
