#!/usr/bin/env python

s = raw_input()  # eliminate heading

wis_count = 0
s = ""
while s != "end":
    s = raw_input()
    i = 0
    while i < len(s) and s[i] != ",":
        i += 1
    state_code = s[i + 1:i + 3]

    if state_code == "WI":
        wis_count += 1

print wis_count
