#!/usr/bin/env python


import sys
arg = sys.argv[1]

# function to find search grep

i = 0
while i < len(arg) and arg[i] != "=":
    i += 1

target = arg[i + 1:]

# funciton to find pos of header in first line

s = raw_input()


index = 0
j = 0
k = 0
while index < 10:
    k = j
    while j < len(s) and s[j] != ",":
        j += 1

    j += 1

    if s[k:j - 1] == arg[:i]:
        pos = index
    else:    
        index += 1

# function to check if any element of s is the target

s = raw_input()
while s != "end":
    if target in s:
        print s
    s = raw_input()
