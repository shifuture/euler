def F(num):
    res="1"
    rs=0
    for i in range(0,num):
        res = multi(res,"2")
    for i in range(0,len(res)):
        rs+=int(res[i])
    return rs,res

def multi(x,y):
    res="0"
    rsTmp=[]
    for i in range(len(y)-1,-1,-1):
        jw=0
        rs=""
        for j in range(len(x)-1, -1,-1):
            n=int(x[j])*int(y[i])+jw
            jw=n/10
            n=n%10
            rs=str(n)+rs
        if jw >0:
            rs=str(jw)+rs
        for i in range(0,len(y)-1-i):
            rs+='0'
        rsTmp.append(rs)
    for rs in rsTmp:
        res=add(res,rs)
    return res


def add(x,y):
    rs=""
    num=max(len(x),len(y))
    j=0
    n=0
    for i in range(0, num+1):
        if len(x)-1-i >=0 and len(y)-1-i >= 0:
            n=int(x[len(x)-1-i])+int(y[len(y)-1-i])+j
            j=n/10
            n=n%10
        elif len(x)-1-i >=0:
            n=int(x[len(x)-1-i])+j
            j=n/10
            n=n%10
        elif len(y)-1-i >= 0:
            n=int(y[len(y)-1-i])+j
            j=n/10
            n=n%10
        else:
            n=j
        rs = str(n) + rs
    return rs.lstrip('0')
