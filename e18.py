import copy

def F():
    nums='''
    75
    95 64
    17 47 82
    18 35 87 10
    20 04 82 47 65
    19 01 23 75 03 34
    88 02 77 73 07 63 67
    99 65 04 28 06 16 70 92
    41 41 26 56 83 40 80 70 33
    41 48 72 33 47 32 37 16 94 29
    53 71 44 65 25 43 91 52 97 51 14
    70 11 33 28 77 73 17 78 39 68 17 57
    91 71 52 38 17 14 91 43 58 50 27 29 48
    63 66 04 68 89 53 67 30 73 16 69 87 40 31
    04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
    '''
    nums=parse(nums)
    paths=route(len(nums))
    maxSum=0
    maxPath=None
    for path in paths:
        sumPath=0
        for p in path:
            print("%d,%d"%(p[0],p[1]))
            sumPath += int(nums[p[0]][p[1]])
        if sumPath > maxSum:
            maxSum = sumPath
            maxPath = path
    return maxPath,maxSum

def route(n):
    paths=[[(0,0)]]
    while not isAllArrived(paths, n):
        pathsTmp=[]
        for path in paths:
            now = path[len(path)-1]
            pathTmp=copy.deepcopy(path)
            path.append((now[0]+1, now[1]+1))
            pathTmp.append((now[0]+1, now[1]))
            pathsTmp.append(path)
            pathsTmp.append(pathTmp)
        paths=pathsTmp
    return paths

def isAllArrived(paths, n):
    for path in paths:
        if len(path)<n:
            return False
    return True

def parse(numStr):
    rs=[]
    for r in numStr.split("\n"):
        r=r.strip(" ")
        if len(r)>0:
            r=r.split(' ')
            rs.append(r)
    return rs
