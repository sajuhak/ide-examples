"""
Code to demonstrate debugging behavior of PyCharm
It takes nth number and
1) calculates the sum of 1 to n digits, i.e., 1+2+3+ ...+n
2) multiplies from 1 to n digits, i.e., 1*2*3* ...*n

If input is given as 4, then
1) sum = 10 (1+2+3+4)
2) multiplication = 24 (1 * 2 * 3 * 4)

"""
from __future__ import print_function

def demo(n):
    sum = 0
    multiplication = 0

    for i in range(n):
        sum = sum + i

    print('sum is {}'.format(sum))

    for x in range(n):
        multiplication = multiplication * n

    print('multiplication is {}'.format(multiplication))


input_number = int(input('enter nth number: '))
print(input_number)
demo(input_number)