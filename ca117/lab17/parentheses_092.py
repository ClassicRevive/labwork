#!/usr/bin/env python3

from stack_092 import Stack


def matcher(line):
    s = Stack()
    par = {"(": ")",
           "[": "]",
           "{": "}"}
    # keys ~ lefties, values~ righties

    for char in line:
        if char in par.keys():
            s.push(char)
        elif char in par.values():  # use this format to prevent excessive and's
            # fail if there is no lefty to match
            if s.is_empty():
                return False
            # fail if the lefty and righty don't match
            elif par[s.top()] != char:
                return False

            s.pop()

    return s.is_empty()
