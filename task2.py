"""
Multiplies the given input arguments and prints the result
"""
from __future__ import print_function


def multiplication(a, b, c):
    total = a * b * c
    return total


# takes arguments from the command line
a = int(input("Please input value a: "))
b = int(input("Please input value b: "))
c = int(input("Please input value c: "))

result = multiplication(a, a, c)
print('multiplication of given inputs is {}'.format(result))
