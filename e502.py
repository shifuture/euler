''' 
    https://projecteuler.net/problem=502
'''
import copy

def F(w, h):
    rs = []
    base = [[[w for i in range(0,w)]]]
    bs = build(base, h)
    # filter block
    for b in bs:
        if not (getWholeBlockNum(b)%2) :
            rs.append(b)
    return rs
    

def getWholeBlockNum(s):
    rs = 0 
    for f in s:
        rs += getFloorBlockNum(f)
    return rs

def getFloorBlockNum(s):
    return len(getFloorBlock(s))

def getFloorBlock(s):
    rs = []
    e = 0
    for m in s:
        if m and e!=m:
            rs.append(m)
        e = m
    return rs

def build(fbs, h):
    if h <= 1:
        return fbs 
    rs = []
    for fb in fbs:
        fs = fb[len(fb)-1]
        rsTemp = []
        i = 0
        while True:
            if i >= len(fs):
                break
            if not fs[i]:
                rsTemp.append([[0]])
                i += 1
            else:
                rsTemp.append(floor(fs[i]))
                i += fs[i]
        rsTemp = mergeFloor(rsTemp)
        for rsTmp in rsTemp:
            fbtmp = copy.copy(fb)
            fbtmp.append(rsTmp)
            rs.append(fbtmp)
    h -= 1
    return build(rs, h)

def mergeFloor(bs):
    rs = []
    iRange = len(bs)
    i = [0 for x in range(0, len(bs))]
    ib = 0
    b = []
    while True:
        b  += copy.copy(bs[ib])[i[ib]]
        if ib == len(bs) - 1:
            ib = 0
            rs.append(b)
            b=[]
            toAdd = 1
            for j in range(len(bs)-1, -1, -1):
                i[j] += toAdd
                if i[j] >= len(bs[j]) and j!=0:
                    i[j] = 0
                    toAdd = 1
                else:
                    toAdd = 0
        else:
            ib += 1
        if i[0] >= len(bs[0]):
            break
    return rs

def floor(w):
    rs = []
    if w > 0:
        for i in range(0,w+1):
            bl = [i for x in range(0, i)]
            if len(bl)<w :
                bl.append(0)
            brs = floor(w-i-1)
            if len(brs):
                for br in brs:
                    tmpbl = copy.copy(bl)
                    for e in br:
                        tmpbl.append(e)
                    rs.append(tmpbl)
            else:
                rs.append(bl)
    return rs

def clean(s):
    rs = []
    for r in s:
        if len(r)>1:
            for e in r:
                if e != 0:
                    rs.append(r)
                    break
        else:
            rs.append(r)
    return rs
