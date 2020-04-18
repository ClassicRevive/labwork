#!/usr/bin/env python

'''
    Revert from camel case back to regular case
    RULES:
    1. keep first word of each line as is
    2. for each capital after that, treat as a new word
'''

import sys

def rcamel(s):
    cap_ind = []
    sentence = []

    # gather indices for capital letters
    for i in range(len(s)):
        if s[i].isupper():
            cap_ind.append(i)

    i = 0
    while (i < len(cap_ind) - 1):
        start, end = cap_ind[i], cap_ind[i + 1]

        # first case doesn't decapitalize
        if i == 0:
            sentence.append(s[start:end])
        else:
            sentence.append(s[start:end].lower())

        i += 1
    if 1 < len(cap_ind):
        sentence.append(s[cap_ind[i]:].lower())  # get last case
    else:
        sentence.append(s[cap_ind[i]:])

    return " ".join(sentence)

def main():
    for line in sys.stdin:
        line = line.rstrip()
        print(rcamel(line))

if __name__ == '__main__':
    main()
