#!/usr/bin/env python3

''' get average length of words and words that exceed it '''
import sys

def main():
    # read in words and strip newline chars
    words = sys.stdin.readlines()
    for i in range(len(words)):
        words[i] = words[i].rstrip()

    total = 0
    for word in words:
        total += len(word)

    avg = total / len(words)
    print("Average: {:.2f}".format(avg))

    for word in words:
        if avg < len(word):
            print(word)


if __name__ == '__main__':
    main()
