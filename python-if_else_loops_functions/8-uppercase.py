#!/usr/bin/python3
def uppercase(str):
    up = ''
    for i in str:
        s = (ord(i)-32)
        if 97 <= ord(i) <= 122:
            up = up + chr(s)
        else:
            up = up + i
    print("{}".format(up))
