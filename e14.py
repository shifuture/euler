def F():
    i=1
    sh=dict()
    maxSeq=0
    maxNum=0
    while i<=1000000:
        seq,num=sequence(i,sh)
        if seq > maxSeq:
            maxSeq=seq
            maxNum=num
            print("%d %d"%(maxSeq, maxNum))
        i+=1
    return maxSeq,maxNum


def sequence(num, sh):
    h = process(num)
    if sh.has_key(h):
        sh[num] = sh[h]+1
    else:
        sl=[num]
        n=num
        while n!=1:
            h=process(n)
            sl.append(h)
            n=h
        sh[num]=len(sl)
    return sh[num],num

def process(num):
    if num%2 :
        h=3*num+1
    else:
        h=num/2
    return h
