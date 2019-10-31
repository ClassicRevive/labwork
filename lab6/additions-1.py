#!/usr/bin/env python


i = 0
while i < 10:
    s = raw_input()
    j = 0
    while j < len(s) and s[j] != "+":
        j += 1
    print s[j]  # test the addition locator



    i += 1
