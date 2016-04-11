import copy

def F(m,n):
    return walk2(0,0,m,n)

def walk2(srcX, srcY, dstX, dstY):
    paths=[[0,0,1]]
    while not isAllArrived2(paths, dstX, dstY):
        pathsTmp=[]
        for path in paths:
            if path[0]<dstX:
                isIn,num = isInPaths2(pathsTmp, path[0]+1, path[1])
                if isIn:
                    removePath2(pathsTmp, path[0]+1, path[1])
                pathsTmp.append([path[0]+1,path[1], path[2]+num])
            if path[1]<dstY:
                isIn,num = isInPaths2(pathsTmp, path[0], path[1]+1)
                if isIn:
                    removePath2(pathsTmp, path[0], path[1]+1)
                pathsTmp.append([path[0],path[1]+1, path[2]+num])
        paths=pathsTmp
    return paths

def isInPaths2(paths, pointX, pointY):
    for path in paths:
        if path[0] == pointX and path[1] == pointY:
            return True,path[2]
    return False,0

def removePath2(paths, pointX, pointY):
    for i in range(0, len(paths)):
        if paths[i][0] == pointX and paths[i][1] == pointY:
            paths.pop(i)
            return


def isAllArrived2(paths, dstX, dstY):
    for path in paths:
        if path[0] != dstX or path[1] != dstY:
            return False
    return True

def walk(srcX, srcY, dstX, dstY):
    paths=[[(srcX, srcY)]]
    while not isAllArrived(paths, dstX, dstY):
        pathsTmp=[]
        for path in paths:
            now = path[len(path)-1]
            if now[0]<dstX:
                pathTmp=copy.deepcopy(path)
                pathTmp.append((now[0]+1,now[1]))
                pathsTmp.append(pathTmp)
            if now[1]<dstY:
                pathTmp=copy.deepcopy(path)
                pathTmp.append((now[0],now[1]+1))
                pathsTmp.append(pathTmp)
        paths=pathsTmp
    return paths


def isAllArrived(paths, dstX, dstY):
    for path in paths:
        point = path[len(path)-1]
        if point[0] != dstX or point[1] != dstY:
            return False
    return True
