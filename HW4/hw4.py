#Mandatory functions
def myName():
    """
    myName(): upon calling, the function returns my name.

    No parameters needed.

    Example: print(myName())
    Output:
        Dylan Calvin
    """
    return "Dylan Calvin"
def myBlazerID():
    """
    myBlazerID(): upon calling, the function returns my BlazerID.

    No parameters needed.

    Example: print(myBlazerID())
    Output:
        dylcal13
    """
    return "dylcal13"

#These functions are being used for other functions in the HW.
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


#Begin HW functions
def tCount(s):
    """
    tCount(s): given a string, s, the function counts the number of occurences of the letter t (upper or lowercase) in the string and returns it.

    Parameters:
        s (str): the string given to the functions

    Example: tCount("There are 9 't' letters in this sentence")
    Output:
        6
    """
    #Error trapping
    if type(s) != str:
        print("ERROR in tCount(): the input must be a string.")
        return None
    sum = 0
    for i in s:
        if i == "T" or i == "t":
            sum += 1
    return int(sum)

def consonantCount(s2):
    """
    consonantCount(s2): given a string, s2, the function counts the number of consonants in the string.
        NOTE: the letter y is not counted as a consonant

    Parameters:
        s2 (str): the string given to the function.

    Example: consonantCount('how many consonants?')
    Output:
        11
    """
    #Error trapping
    if type(s2) != str:
        print("ERROR in consonantCount(): input must be string.")
        return None
    sum = 0
    for i in s2:
        if (i not in "aeiouAEIOUyY") and i.isalpha() == True:
            sum += 1
    return sum

def grList(l1):
    """
    grList(l1): given a list, l1, the function determines if your grocery list contains items that your friend is allergic to (peanuts or carrots).
        If the list does contain allergy items, we replace that item in the friends list with an orange and print both lists.

    Parameters:
        l1 (list): your grocery list given to the function.

    Example: grList(["water","chips","watermelon","peanut","napkins"])
    Output:
        My friend needs ['water', 'chips', 'watermelon', 'orange', 'napkins']
        I need ['water', 'chips', 'watermelon', 'peanut', 'napkins']
    """
    #Error trapping
    if type(l1) != list:
        print("ERROR in grList(): input must be a list.")
        return None
    for i in l1:
        if type(i) != str:
            print("ERROR in grList(): elements in list must be strings.")
            return None
    #functions
    friend_list = []
    for i in l1:
        if i in ["peanut","carrot"]:
            friend_list.append("orange")
        else:
            friend_list.append(i)
    print("My friend needs "+str(friend_list))
    print("I need "+str(l1))

def argMin(l2):
    """
    argMin(l2): argmin takes a list and returns the index of the miniumum value in the list.

    Parameters:
        list (list): The list that is given to the Function

    Example: argMin([2,5,4,6,7,8,9,3,1])
    Output:
        8
    """
    #Error trapping
    if type(l2) != list:
        print("ERROR in argMin(): input must be a list.")
        return None
    for i in l2:
        if type(i) != float and type(i) != int:
            print("ERROR in argMin(): elements must be a number.")
            return None
    #Function
    imin = 0
    for i in range(len(l2)):
        if l2[i] < l2[imin]:
            imin = i
    return imin

def notPrimes(t):
    """
    notPrimes(t): given a tuple, t, the function determines what elements are not prime USING isPrime(), and returns a
        list containing those values.

    Parameters:
        t (tuple): the tuple given to the function.

    Example: notPrimes((3,4,5))
    Output:
        [4]
    """
    #Error trapping
    if type(t) != tuple:
        print("ERROR in notPrimes(): input must be a tuple.")
        return None
    for i in t:
        if type(i) != float and type(i) != int:
            print("ERROR in notPrimes(): elements must be a number.")
            return None
    retlist = []
    for i in t:
        if isPrime(i) == False:
            retlist.append(i)
    return retlist

#Function Calls
# print("My Name is =",myName(), " and my BlazerID is =",myBlazerID())
# print()
# print("****** Results of tCount() ******")
# print(" tCount(\"There are 9 't' letters in this sentence\") =", tCount("There are 9 't' letters in this sentence"))
# print(" tCount(\"abra cadabra\") = ", tCount("abra cadabra"))
# print(" tCount(\"Tattooist has capital T letters\") =", tCount("Tattooist has capital T letters"))
# print("****** Results of consonantCount() ******")
# print(" consonantCount('abra cadabra') =",consonantCount('abra cadabra'))
# print(" consonantCount('how many consonants?') =",consonantCount('how many consonants?'))
# print(" consonantCount('This is Hw4, folks') =",consonantCount('This is Hw4, folks'))
# print("****** Results of grList() ******")
# grList(["water", "chips", "watermelon", "peanut", "napkins"])
# grList(["candy","lemonade","ginger","bread","water"])
# grList(["candy","peanut","carrot","bread","water"])
# print("****** Results of argMin() ******")
# print(" argMin([3,4,5]) =",argMin([3,4,5]))
# print(" argMin([3,4,5,0,-7]) =",argMin([3,4,5,0,-7]))
# print(" argMin([0,0,5,9,3,-21,45,1022]) =",argMin([0,0,5,9,3,-21,45,1022]))
# print("****** Results of notPrimes() ******")
# print(" notPrimes((3,4,5)) =",notPrimes((3,4,5)))
# print(" notPrimes((3,4,5,6,12,14,21)) =",notPrimes((3,4,5,6,12,14,21)))
# print(" notPrimes((12,17,11,22,24)) =",notPrimes((12,17,11,22,24)))
