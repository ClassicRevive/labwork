#!/usr/bin/env python3

''' for each password show number of character classes in it'''

import sys

def classify(s):
    if "a" <= s and s <= "z":
        return "lower_case"
    elif "A" <= s and s <= "Z":
        return "upper_case"
    elif "0" <= s and s <= "9":
        return "digit"
    else:
        return "special"


def main():
    passwords = sys.stdin.readlines()
    for password in passwords:
        password = password.strip()
        classes = []
        for char in password:
            char_type = classify(char)
            if char_type not in classes:
                classes.append(char_type)
        print(len(classes))


if __name__ == '__main__':
    main()
    # test calssify function
    # print(classify("3"), classify("a"), classify("A"), classify("/"))
