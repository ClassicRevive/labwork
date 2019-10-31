#!/usr/bin/env python

s = raw_input()  # eliminate heading


s = ""
while s != "end":
    s = raw_input()
    i = 0
    while i < len(s) and s[i:i + 4] != "City":
        i += 1

    if i < len(s):
        city_name = s[:i + 4]
        print city_name
