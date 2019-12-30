#!/usr/bin/env python

from time import sleep

i = 0
n = 1

while i < 100:
    if n % 2 == 0:
        n = n / 2
        print n
        sleep(0.2)
    else:
        n = (n * 3) + 1
        print n
        sleep(0.2)

    n += 1
    i += 1

#print n
