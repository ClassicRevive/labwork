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

    index += 1

# function to check if any element of s is the target

s = raw_input()
while s != "end":
    l = 0
    m = 0
    place = 0
    while place < 10:
        l = m
        while m < len(s) and s[m] != ",":
            m += 1

        m += 1
        if s[l:m - 1] == target and place == pos:
            print s
        place += 1
    s = raw_input()
