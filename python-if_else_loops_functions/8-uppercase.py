#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if chr(97) <= i <= chr(122):
            i = chr(ord(i) - 32)
        print("{}".format(i), end="")
    print("")
