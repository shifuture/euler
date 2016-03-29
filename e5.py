'''
https://projecteuler.net/problem=5
'''

import copy

def F(num):
    rs = 1
    ft = []
    for i in range(1,num+1):
        if isFactor(i, ft):
            ft.append(i)

    for i in list(ft):
        p = 2
        while True:
            if pow(i, p) < num:
                ft.append(i)
                p += 1
            else:
                break

    for i in ft:
        rs *= i

    return ft,rs

def isFactor(num, fs):
    if num < 2:
        return False
    divider = 2
    for n in fs:
        if num%n == 0:
            return False
        else:
            divider = n+1
    while True:
        if num%divider == 0 :
            if divider != num:
                return False
            else:
                return True
        else:
            divider += 1
