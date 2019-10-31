#!/usr/bin/env python

s = raw_input()  # eliminate heading


s = ""
while s != "end":
    s = raw_input()
    i = 0
    while i < len(s) and s[i] != ",":
        i += 1
    state_code = s[i + 1:i + 3]

    # snipe city names where state code = wisconson
    if state_code == "WI":
        print s[:i]
