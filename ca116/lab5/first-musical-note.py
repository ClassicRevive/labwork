#!/usr/bin/env python


# first test
n = raw_input()
i = 0

note = n[i]
while note > "g" or note < "a":
    i += 1
    note = n[i]

print note
