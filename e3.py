def F(num):
    fs = []
    rs = []
    divider = 2
    while True:
        if divider > num:
            break;
        if isFactor(divider, fs):
            fs.append(divider)
            if num%divider == 0:
                rs.append(divider)
                num = num/divider
        divider += 1
    return rs


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
