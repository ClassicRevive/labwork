#!/usr/bin/env python

import os
import sys

files = os.listdir(".")  # powerful!

i = 0
while i < len(files):
    isfile = os.path.isfile(files[i])

    if files[i][-4:] == ".bak" and isfile:
        os.unlink(files[i])

    i += 1
