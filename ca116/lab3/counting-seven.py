#!/usr/bin/env python


n = input()
sevens = 0

i = 1
while sevens < n:
    if i % 7 == 0:
        print i
        sevens += 1
    i += 1
