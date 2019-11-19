#!/usr/bin/env python

s = raw_input()
while s != "end":

    slash_count = 0
    i = 0
    j = len(s)
    while slash_count < 3:

        while i < len(s) and s[i] != "/":
            i += 1

        i += 1
        slash_count += 1

    if s[j - 2:j] == "py":
        print s[i:j]
    s = raw_input()
