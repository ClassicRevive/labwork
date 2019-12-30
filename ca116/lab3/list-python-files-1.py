#!/usr/bin/env python

import os
import sys
files = os.listdir(".")

i = 0
while i < len(files):
    print files[i][-3:]
    if files[i][-3:] == ".py":
        sys.stdout.write(files[i])

    i += 1

