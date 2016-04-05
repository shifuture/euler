from sets import Set

def F(num):
    i=1
    while True:
        tn = triNum(i)
        f = getFactors(tn)
        if len(f) >= num:
            break;
        i+=1
        print("%d %d %d"%(i, tn, len(f)))
    return sorted(f)

def triNum(num):
    return num*(num+1)/2

def getFactors(num):
    rs = Set()
    factor = 1
    while True:
        if num%factor == 0:
            rs.add(factor)
            rs.add(num/factor)
        factor+=1
        if factor > int(num/2)+1:
            break;
    return rs
