#!/usr/bin/env python

import sys
arg = sys.argv[1]

s = raw_input()

index = 0
j = 0
k = 0
while index < int(arg) + 1:
    k = j
    while j < len(s) and s[j] != ",":
        j += 1

    j += 1
    index += 1

print s[k:j - 1]
