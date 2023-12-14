########################################
#  Name: Dylan Calvin
#  BlazerID: dylcal13
#  Assignment: Lab 6 (ungraded)
########################################

def mOfThree(n):
    """ 
    mOfThree(n): given an integer input,n, this function finds every number between 1 and n that are
        multiples of three.

    Parameters:
        n (int): integer number that acts as upper limit, i.e no number printed goes above n

    Example: mOfThree(14)
    Output:
        3
        6
        9
        12
    """
    #Error Trapping
    if type(n) != int:
        print("ERROR in mOfThree(): recieved non-int value for input.")
        return
    # function
    i=1
    while i <= n:
        if i%3 == 0:
            print(i)
        i += 1

def tupleCheck(t):
    """
    tupleCheck(t): given a tuple, t, the function checks for how many even and odd numbers are in the tuple.

    Parameters:
        t (tuple): the tuple that is given in the function call, used for determining number of evens and odds.

    Example: tupleCheck((1,2,3,4,5,6,7,8,9))
    Output:
        Number of even numbers: 4
        Number of odd numbers: 5
    """
    #Error Trapping
    if type(t) != tuple:
        print("ERROR in tupleCheck(): recieved non-tuple value for input.")
        return
    #Function
    num_odd = 0
    num_even = 0
    for i in t:
        if i%2 == 0:
            num_even += 1
        else:
            num_odd += 1
    print("   Number of even numbers: "+str(num_even))
    print("   Number of odd numbers: "+str(num_odd))

def caseCheck(s):
    """
    caseChecks(s): given a string input, s, the function will determine how many upper case and lower case
        letters exist in the string.

    Parameters:
        s (str): a string that is given in the function call and is used to determine the number of upper and
            lower case letters.

    Example: caseChecks("The quick Brown Fox")
    Output:
        Number of Upper Case letters: 3
        Number of Lower Case letters: 13 
    """
    #Error Trapping
    if type(s) != str:
        print("ERROR in caseCheck(): recieved a non-string value for input.")
        return
    #Function
    num_upper = 0
    num_lower = 0
    for i in range(len(s)):
        if s[i].isalpha() == True:
            if s[i].isupper() == True:
                num_upper += 1
            else:
                num_lower += 1
    print("   Number of Upper Case letters: "+str(num_upper))
    print("   Number of Lower Case letters: "+str(num_lower))

# EXtra Excersises
def nextDate():
    """
    nextDate(): The function asks the user for the current date, and then returns the next day's date.
        The function accounts for leap years, end-of-month changes, and end-of-year changes.
    
    Example: nextDate()
    Output:
        Please enter the year: 2020
        Please enter the month: 2
        Please enter the day: 28
        Next Date = 2-29-2020
    """
    y = int(input("Please enter the year: "))
    m = int(input("Please enter the month: "))
    d = int(input("Please enter the day: "))
    if d+1 > 32:
        if m in [1,3,5,7,8,10,12]:
            if m == 12:
                m = 1
                d = 1
                y += 1
            else:
                m += 1
                d = 1
    elif d+1 > 31:
        if m in [9,4,6,11]:
            m += 1
            d = 1
    elif d+1 > 29:  
        if m == 2:
            if y%4 != 0:
                m += 1
                d = 1
            else:
                d += 1
    else:
        d += 1
    print("Next Date = "+str(m)+"-"+str(d)+"-"+str(y))

def mTable(n):
    """
    mTable(n): given an integer, n, the function generates a table showing the mutliplication of n time 1 to 10.

    Parameters:
        n (int): the input value used to generate the table.

    Example: mTable(6)
    Output:
        6x1 = 6
        6x2 = 12
        6x3 = 18
        6x4 = 24
        6x5 = 30
        6x6 = 36
        6x7 = 42
        6x8 = 48
        6x9 = 54
    """
    #Error Trapping
    if type(n) != int:
        print("ERROR in mTable(): Recieved a non-integer value for input.")
        return
    #function
    for i in range(1,10):
        print(" "+str(n)+"x"+str(i)+" = "+str(n*i))


# Big Ol' Function calling.
print("****** Results of mOfThree() ******")
print("Result 1: mOfThree(15)")
mOfThree(15)
print("Result 2: mOfThree(25)")
mOfThree(25)
print("Result 3: mOfThree(78)")
mOfThree(78)
print()
print("****** Results of tupleCheck() ******")
print("Result 1: tupleCheck((1,2,3,4,5,6,7,8,9))")
tupleCheck((1,2,3,4,5,6,7,8,9))
print("Result 2: tupleCheck((-43,56,79,23,2,8,5,23,132,46,67,8))")
tupleCheck((-43,56,79,23,2,8,5,23,132,46,67,8))
print("Result 3: tupleCheck((1234,123,5,2304987,6,758,6,23,134,134,54,54,65,43,134,2,6,5,34,13,234,6,6,56,34,134,2,54,56,586,342,1342))")
tupleCheck((1234,123,5,2304987,6,758,6,23,134,134,54,54,65,43,134,2,6,5,34,13,234,6,6,56,34,134,2,54,56,586,342,1342))
print()
print("****** Results of caseCheck() ******")
print("Result 1: caseCheck('The quick Brown Fox')")
caseCheck("The quick Brown Fox")
print("Result 2: caseCheck('Long Live Linux')")
caseCheck("Long Live Linux")
print("Result 3: caseCheck('According to all known laws of aviation, there is no way that a bee should be able to fly. Its wings are too small to get its fat little body off the ground. The bee, of course, flies anyways. Because bees don't care what humans think is impossible.')")
caseCheck("According to all known laws of aviation, there is no way that a bee should be able to fly. Its wings are too small to get its fat little body off the ground. The bee, of course, flies anyways. Because bees don't care what humans think is impossible.")
print()
print("-- Begin Extra Excersises --")
print()
print("****** Results of nextDate() ******")
nextDate() 
print()
print("****** Results of mTable() ******")
print("Result 1: mTable(6)")
mTable(6)
print("Result 1: mTable(6)")
mTable(87)
print("Result 1: mTable(6)")
mTable(25)