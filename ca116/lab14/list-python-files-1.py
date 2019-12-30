#!/usr/bin/env python

import os
import sys
files = os.listdir(".")

i = 0
while i < len(files):
    if files[i][-3:] == ".py":
        print files[i]

    i += 1
