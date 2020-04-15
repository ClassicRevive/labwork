#!/usr/bin/env python3

import sys

word = sys.argv[1]
# if rotation is above length of word, reset rotation
rotation = int(sys.argv[2]) % len(word)

# swap characters before and after rotation index number
s = word[rotation:] + word[:rotation]
print(s)
