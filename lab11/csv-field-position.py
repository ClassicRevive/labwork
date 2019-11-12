#!/usr/bin/env python


import sys
arg = sys.argv[1]

s = raw_input()

index = 0
j = 0
k = 0
while index < 10:
    k = j
    while j < len(s) and s[j] != ",":
        j += 1

    j += 1

    if s[k:j - 1] == arg:
        print index

    index += 1
