#!/usr/bin/env python3


''' read numbers and print numbers which have previouslt occured in input '''

import sys

print("Enter numbers (-1 to end): ", end="")
numbers = set()
previous = []

num = int(input())
while num != -1:
    if num not in numbers:
        numbers.add(num)
    else:
        previous.append(num)

    num = int(input())


# for printing results: 

for num in previous:
    print(str(num) + " ", end="")

print()