#!/usr/bin/env python

import sys
size = sys.argv[1]

i = 1
while i < (int(size) / 2) + 1:
    print "*" * i
    i += 1

j = i 
while j > 0:
    print "*" * j
    j -= 1

