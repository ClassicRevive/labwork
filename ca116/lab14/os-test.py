#!/usr/bin/env python

import os
files = os.listdir("..")  # .. is back one dir (Line A.)

i = 0
while i < len(files):
   if files[i][0] != ".":  # don't include hidden files (Line B.)
      print files[i]
   i = i + 1

