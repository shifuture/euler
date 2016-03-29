'''
https://projecteuler.net/problem=4
'''
import math

def F(dig):
    rs = []
    minNum = pow(pow(10,dig-1), 2)
    maxNum = pow(pow(10,dig)-1,2)
    i = minNum
    while True:
        if isPdNum(i) and divide(i, dig) > 0:
            rs.append(i)
        if i > maxNum:
            break
        else:
            i += 1
    return rs,rs[len(rs)-1]

def isPdNum(num):
    strNum = str(num)
    strRev = ''.join([strNum[x] for x in range(len(strNum)-1, -1, -1)])
    if strNum == strRev:
        return True
    else:
        return False

def divide(num, dig):
    for i in range(pow(10,dig-1), pow(10,dig)):
        if num%i == 0 and len(str(num/i)) == dig:
            return i
    return 0
