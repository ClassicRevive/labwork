#!/usr/bin/env python3

''' rewrite text but only first occurence of each word '''

import sys
from string import punctuation

def main():
    seen = set()

    for line in sys.stdin:
        sentence = []
        line = line.rstrip().split()
        for word in line:
            if word.lower().strip(punctuation) not in seen:
                seen.add(word.lower().strip(punctuation))
                sentence.append(word)
            else:
                sentence.append(".")

        print(" ".join(sentence))


if __name__ == '__main__':
    main()
