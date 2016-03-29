def F(num):
    fs = []
    divider = 2
    while len(fs) < num:
        if isFactor(divider,fs):
            fs.append(divider)
        divider += 1
    return fs,len(fs),fs[len(fs)-1]

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

