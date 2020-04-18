#!/usr/bin/env python3

''' print words in symmetric order '''

import sys

def main():
    pairs = {}

    words = sys.stdin.readlines()

    for i in range(len(words)):
        words[i] = words[i].rstrip()  # remove \n characters

    # decides index to start the symmetric rotation
    if 1 < len(words):
        if len(words[-1]) == len(words[-2]):
            start = -3
        else:
            start = -2

        # symmetric rotation algo
        i = start
        while -len(words) < i:
            # swap words[i] and words[i + 1:]
            x = words.pop(i)
            words.append(x)
            i -= 2

        for word in words:
            print(word)
    else:
        print(words[0])
if __name__ == '__main__':
    main()
