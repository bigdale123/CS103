import numpy as np

def fileExtension(s):
    for i in range(len(s)):
        if s[i] == ".":
            return s[i+1:]

def twoIntCompare(n1,n2):
    if n1 == n2:
        return True
    elif (abs(n1-n2) == 12) or (n1+n2 == 12):
        return True
    else:
        return False

def basicStats(npArray):
    return [np.mean(npArray),np.std(npArray),np.var(npArray)]


print(fileExtension("lab13_103sp19.pdf"))
print(twoIntCompare(7,5))
print(twoIntCompare(17,5))
print(twoIntCompare(17,15))
a = [0,1,2,3,4,5]
print(basicStats(a))
