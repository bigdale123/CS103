def dCube(n):
    ret_dict = {}
    for i in range(1,n+1):
        ret_dict[str(i)] = i**3
    return ret_dict

def dMerge(d1,d2):
    for i in d1:
        print(i)
        if i in d2:
            d2[i] = d2[i]+d1[i]
        else:
            d2[i] = d1[i]
    return d2

def nonRepeatings(s3):
    ret_list = []
    for i in s3:
        if (s3.count(i) == 1):
            ret_list.append(i)
    return ret_list

def dAnagram(s1,s2):
    if s1 != s2:
        if len(s2) == len(s1):
            for i in s1:
                if i not in s2:
                    return False
            return True
        else:
            return False
    else:
        return False



#Function Calls
print(dCube(5))
print(dMerge({'orange':500, 'apple':1100, 'carrot':600},{'orange':50, 'apple':10,'grapes':300}))
print(nonRepeatings("zzzdaaarttt"))
print(dAnagram("ordinate","rodentia"))
