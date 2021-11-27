import random
import string


def count(string):
    # your code here
    d = {}
    keep = len(string) - 1
    for i in range(0, keep):
        lul = 1
        if string[i] in d:
            lul = lul + 1
            d[string[i]] = lul
        else:
            d[string[i]] = lul
    return d

count("lol")