from __future__ import print_function
import sys


def multiplication(a, b, c):
    total = a * b * c
    return total


# takes arguments from the command line
a = int(input("a "))
b = int(input("b "))
c = int(input("c "))

result = multiplication(a, a, c)
print(result)