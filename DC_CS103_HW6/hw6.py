def isPrime(n):
    """
    isPrime(n): given an integer, n , the function finds out if n is a prime number.

    Parameters:
        n (int): given integer thats passed to Function

    Example: isPrime(3)
    Output:
        True
    """
    #Error Trapping
    if type(n) != int:
        print("ERROR in isPrime(): input must be integer type.")
        return None
    #function
    for i in range(2,n-1):
        if n/i == int(n/i):
            return False
    return True

def uabCs(n1):
    if n1 != 3 and n1 != 7 and isPrime(n1) == True:
        return "Go Blazers"
    elif n1%3 == 0 and n1%7 == 0:
        return "UAB CS 103"
    elif n1%3 == 0:
        return "CS"
    elif n1%7 == 0:
        return "UAB"
    else:
        return n1**3

def blazers(n2):
    retstring = ""
    powers = []
    for i in range(0,100):
        powers.append(2**i)
    for i in range(0,n2+1):
        if i in powers:
            retstring += "blazers"
        else:
            retstring += str(i)
    return retstring

def mostCommon(s):
    temp_dict = {}
    first_max = 0
    first_max_key = ""
    second_max = 0
    second_max_key = ""
    if len(s) < 4 or len(s) > 100:
        print("The string should be greater than 4 and less than 100.")
    else:
        for i in s:
            if i not in temp_dict.keys():
                temp_dict[i] = 1
            else:
                temp_dict[i] += 1
        for i in temp_dict.keys():
            if temp_dict[i] > first_max:
                # runs more code, saves on memory by not having to clone dictionaries
                first_max = temp_dict[i]
                first_max_key = i
        del temp_dict[first_max_key]
        for i in temp_dict.keys():
            if temp_dict[i] > second_max:
                # runs more code, saves on memory by not having to clone dictionaries
                second_max = temp_dict[i]
                second_max_key = i
        print(first_max_key,first_max)
        print(second_max_key,second_max)

def genPrime(n3):
    retlist = []
    for i in range(2,n3):
        if isPrime(i) == True:
            yield i

print(uabCs(3))
print(uabCs(70))
print(uabCs(4))
print(uabCs(17))

print(blazers(3))
print(blazers(7))
print(blazers(10))
print(blazers(1))

mostCommon("uabcsaaacc")
mostCommon("oblazersoooozzz")
mostCommon("uab")
mostCommon("hw6 isssssss funnn")

for i in genPrime(25):
    print(i)
