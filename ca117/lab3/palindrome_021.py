#!/usr/bin/env python3

'''return boolean for whether input is a palindrome'''

import sys
import string

# join whole line into string with no space and no caps
# check if s[:len(s)/2].reverse() = s[len(s)/2:]

def palindrome(s):
    reverse = ""
    for i in range(len(s)):
        reverse += s[-1 - i]
    return reverse == s


def main():
    for line in sys.stdin:
        s = line.split()

        # split and strip each word and lower individually
        for i in range(len(s)):
            s[i] = s[i].lower().rstrip(string.punctuation)

        pal = "".join(s)
        print(palindrome(pal))


if __name__ == '__main__':
    main()
