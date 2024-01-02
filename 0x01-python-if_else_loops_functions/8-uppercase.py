#!/usr/bin/python3


def uppercase(str):
    newstring = ""
    for c in str:
        if ord(c) >= 97 and ord(c) <= 122:
            newstring += chr(ord(c) - 32)
        else:
            newstring += c
    print("{}".format(newstring))
