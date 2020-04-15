#!/usr/bin/env python3

def fibonacci(n):
    # base case
    if n <= 1:
        return 1
    # recursive case
    return fibonacci(n - 2) + fibonacci(n - 1)
