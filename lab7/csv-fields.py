#!/usr/bin/env python


s = raw_input()
j = 0
i = 0
headers = 0

while headers < 10:
    while j < len(s) and s[j] != ",":  # find first comma
        j += 1

    print s[i:j]

    i = j + 1
    j += 1

    headers += 1
