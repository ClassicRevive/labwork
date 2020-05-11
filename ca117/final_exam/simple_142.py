#!/usr/bin/env python3

import sys

# used for finding letter with min occurencies
def occurences(t):
    return t[1]

# used for compiling hash map of occurencies of each letter
def comp(word):
    seen = {}

    for letter in word:
        if letter not in seen:
            seen[letter] = 1
        else:
            seen[letter] += 1

    return seen

def main():

    for line in sys.stdin:
        word = line.rstrip()
        seen = comp(word)
        complexity = len(seen)

        moves = 0
        while complexity > 2:
            # keep reducing complexity based on the letter
            # with minimum occurencies until complexity is 2
            cand = min(seen.items(), key=occurences)
            word = word.replace(cand[0], "", 1)
            seen = comp(word)
            complexity = len(seen)

            # count the moves
            moves += 1

        print(moves)

if __name__ == '__main__':
    main()
