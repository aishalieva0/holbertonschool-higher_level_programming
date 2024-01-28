#!/usr/bin/python3
for s in range(ord('a'), ord('z') + 1):
    if "{:c}".format(s) == 'q' or "{:c}".format(s) == 'e':
        continue
    print("{:c}".format(s), end="")
