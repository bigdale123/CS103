import random

def find_index_max(list):
    imax = 0
    for i in range(len(list)):
        if list[i] > list[imax]:
            imax = i
    return imax

def find_index_min(list):
    imin = 0
    for i in range(len(list)):
        if list[i] < list[imin]:
            imin = i
    return imin


def listDetails(L):
    ret_tuple = ()
    ret_tuple += (len(L),)
    ret_tuple += (min(L),)
    ret_tuple += (find_index_min(L),)
    sum = 0
    for i in L:
        sum += i
    mean = sum/len(L)
    ret_tuple += ("{:.4}".format(mean),)
    ret_tuple += (max(L),)
    ret_tuple += (find_index_max(L),)
    return ret_tuple

def randomizedTest(numTests):
    ret_list = []
    for i in range(numTests):
        ret_list.append([random.randint(1,24),float("{:.4}".format(random.uniform(1,100))),float("{:.4}".format(random.uniform(1,100)))])
    return ret_list

def minSum(L2):
    ret_list = []
    ret_list.append(find_index_min(L2))
    L2.pop(ret_list[0])
    #print(L2)
    ret_list.append(find_index_min(L2)+1)

    return ret_list

print(listDetails([-8,-23, 18, 103, 0, 1,-4, 631, 3,-41, 5]))
print(randomizedTest(3))
print(minSum([1,2,3,4,5,6,7,8,9]))
