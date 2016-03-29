'''
https://projecteuler.net/problem=500
'''

def F(num):
    pass


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
