def listToDict(l1,l2):
    ret_dict = {}
    if len(l1) == len(l2):
        for i in range(len(l1)):
            ret_dict[l1[i]] = l2[i]
    return ret_dict

def dMax(d):
    max = 0
    for i in d:
        if d[i] > max:
            max = d[i]
    return max

def dString(s):
    ret_dict = {}
    for i in s:
        if i != " ":
            if i in ret_dict:
                ret_dict[i] += 1
            else:
                ret_dict[i] = 1
    return ret_dict

print(listToDict([1,2,3],["First","second","Third"]))
print(dMax({'a':2500, 'b':61874, 'c': 60,'d':1560}))
print(dString("UAB CS BS"))
