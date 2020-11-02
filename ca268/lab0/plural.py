#!/usr/bin/env python3

import sys

def get_plural(word):
    es = ["ch", "sh", "x", "s", "z", "o"]
    ies = "y"
    consonants = "bcdfghjklmnpqrstvwxyz"

    if word[-1] in es or word[-2:] in es:
        return word + "es"
    elif word[-2] in consonants and word[-1] == "y":
        return word[:-1] + "ies"
    elif word[-1] == "f":
        return word[:-1] + "ves"
    elif word[-2:] == "fe":
        return word[:-2] + "ves"
    elif word[-1] == "o":
        return word + "es"
    else:
        return word + "s"
