''' reads a string on command line and prints consecutive pairs
    of characters of the string '''

import sys
word = sys.argv[1]

for i in range(len(word) - 1):
    print(word[i] + word[i + 1])
