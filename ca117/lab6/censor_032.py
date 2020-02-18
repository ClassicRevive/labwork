#!/usr/bin/env python3

''' return text from stdin but censor words which are in censor list'''

import sys

def censor_word(word, censor):
    return word.replace(censor, "@" * len(censor))


def main():
    # load censor words into dictionary
    censor_file = sys.argv[1]
    censor_words = {}

    with open(censor_file, "r") as fin:

        for word in fin:
            word = word.rstrip()
            censor_words[word] = True

    for line in sys.stdin:
        curr_line = []

        words = line.rstrip().split()
        for word in words:
            for censor in censor_words:
                if censor in word:
                    word = censor_word(word, censor)
            curr_line.append(word)

        print(" ".join(curr_line))


if __name__ == '__main__':
    main()
