#!/usr/bin/env python


if __name__ == "__main__":
    a = ["dog", "mountjoy", "mounty", "extra-long", "mountain"]


tmp = a[0]
a[0] = a[-1]
a[-1] = tmp
