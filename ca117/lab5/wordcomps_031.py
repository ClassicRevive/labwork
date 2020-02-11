#!/usr/bin/env python3

''' use list comprehensions to process
    the following lists from a parent list
'''
import sys

def contains(chars, word):
    matched = True
    for i in range(len(chars)):
            if chars[i].lower() in word.lower():
                word = word.replace(chars[i], "*")
            else:
                matched = False

    return matched

def shortest_vowel_word(a):
    shortest = 100
    short_word = ""
    for word in a:
        if len(word) < shortest and contains("aeiou", word):
            shortest = len(word)
            short_word = word

    return short_word


def main():
    a = []
    for s in sys.stdin:
        a.append(s.rstrip())

    iary_count = 0
    e_count = 0
    for i in a:
        if i[-4:] == "iary":
            iary_count += 1
        if e_count < i.count("e"):
            e_count = i.count("e")

    print("Words containing 17 letters: {}".format([x for x in a if len(x) == 17]))
    print("Words containing 18+ letters: {}".format([x for x in a if 17 < len(x)]))
    print("Shortest word containing all vowels: {}".format(shortest_vowel_word(a)))
    print("Words with 4 a's: {}".format([x for x in a if x.lower().count("a") >= 4]))
    print("Words with 2+ q's: {}".format([x for x in a if x.lower().count("q") >= 2]))
    print("Words containing cie: {}".format([x for x in a if "cie" in x.lower()]))
    print("Anagrams of angle: {}".format([x for x in a if len(x) == 5 and contains("angle", x.lower()) and x != "angle"]))
    print("Words ending in iary: {}".format(iary_count))
    print("Words with most e's: {}".format([x for x in a if x.count("e") == e_count]))


if __name__ == '__main__':
    main()
