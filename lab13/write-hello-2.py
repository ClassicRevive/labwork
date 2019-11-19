#!/usr/bin/env python


if __name__ == "__main__":
    import sys
    filename = sys.argv[1]

message = "Hello world.\n"

with open(filename, "w") as fd:
    fd.write(message)
