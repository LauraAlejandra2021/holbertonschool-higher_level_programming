#!/usr/bin/python3
def uppercase(str):
    for i in str:
        cam = ord(i)
        if cam >= 97 and cam <= 122:
            i = chr(cam - 32)
        print("{}".format(i), end='')
    print("")
