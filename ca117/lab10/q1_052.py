#!/usr/bin/env python3

''' rotate word from commandline by r steps clockwise '''

import sys


def main():
    word = sys.argv[1]
    r = int(sys.argv[2])

    if r < len(word):
        new_word = word[-r:] + word[:-r]  # swap last r chars wih first len - r chars
        print(new_word)
    else:
        new_r = r % len(word)
        new_word = word[-new_r:] + word[:-new_r]
        print(new_word)


if __name__ == '__main__':
    main()
