import math

def F(num):
    return nsp(num) - nps(num)

def nps(num):
    res = 0
    for i in range(1, num+1):
        res+=int(math.pow(i, 2))
    return res

def nsp(num):
    return int(math.pow(sum(range(1,num+1)), 2))
