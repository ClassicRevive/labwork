#!/usr/bin/env python3

from stack import Stack

def check_brackets(line):
    s = Stack()

    for char in line:
        if char == "(":
            s.push(char)
        elif char == ")":
            x = s.pop()

            if x is None:
                return False

    return s.is_empty()
