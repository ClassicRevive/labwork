#!/usr/bin/env python

secret_number = 543

def guess(n):
    if n == secret_number:
        return "correct"
    elif n < secret_number:
        return "too-low"
    else:
        return "too-high"


