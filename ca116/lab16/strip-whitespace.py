#!/usr/bin/env python

import sys

fd = sys.argv[1]

with open(fd) as f:
    f_read = f.readline()
    while 0 < len(f_read):
        f_strip = f_read.strip()
        # print f_strip
        with open(fd + ".stripped", "a") as new:
            new.write(f_strip + "\n")

        f_read = f.readline()
