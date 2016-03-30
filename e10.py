def F(num):
    fs = []
    rs = 0
    divider = 2
    while True:
        if divider > num:
            break
        if isFactor(divider, fs):
            fs.append(divider)
            rs += divider
        divider += 1
    return fs, rs


def isFactor(num, fs):
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
