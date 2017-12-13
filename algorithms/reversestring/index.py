#!/usr/bin/env python
# -*- coding: utf-8 -*-

def reverseString(word):
    reversed = ""
    for ch in list(word):
        reversed = "{0}{1}".format(ch, reversed)
    return reversed


# Solution 1
# return word[::-1]

# Solution 2
# reversed = ""
# for ch in list(word):
#   reversed = "{0}{1}".format(ch, reversed)
# return reversed

if __name__ == "__main__":
    reverseString("abcd")