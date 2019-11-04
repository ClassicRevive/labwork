#!/usr/bin/env python


if __name__ == "__main__":
    a = ["dog", "mountjoy", "mounty", "extra-long", "mountain"]
    i = 1
    j = 2


tmp = a[i]
a[i] = a[j]
a[j] = tmp
