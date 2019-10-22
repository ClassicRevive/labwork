#!/usr/bin/env python


n = input()
odds = 0

i = 0
while odds < n:
    if i % 2 == 1:
        print i
        odds += 1
    i += 1
