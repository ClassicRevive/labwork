#!/usr/bin/env python3

''' use list comprehensions to process 
    the following lists from a parent list
'''
import sys


def shortest_vowel_word(a):
    shortest = 100
    short_word = ""
    for word in a:
        if len(word) < shortest and "a" in word:
            shortest = len(word)
            short_word = word

    return 


def main():
    a = []
    for s in sys.stdin:
        a.append(s.rstrip().lower())
    print(shortest_vowel_word(a))
    # print("Words containing 17 letters: {}".format(x for x in a if len(x) == 17))
    # print("Words containing 18+ letters: {}".format(x for x in a if 17 < len(x)))
    # print("Shortest word containing all vowels: {}".format(shortest_vowel_word(a)))



if __name__ == '__main__':
    main()