#!/usr/bin/python3
def uppercase(str):
    toUpper = ""
    for char in str:
        if 97 <= ord(char) <= 122:
            toUpper += chr(ord(char) - 32)
        else:
            toUpper += char
    print("{:s}".format(toUpper))
