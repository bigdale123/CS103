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

def finalGrade(classList):
    """
    finalGrade(classList): Given a list containing sub-lists which contain numbers, classList, the function will return the class average for the
        attendance grade, the exam grade, and the homework grade. Each sublist represents a student in the class, and each sublist must contain only 3 values,
        where the 1st element is the student's attendance grade, the 2nd element contains the student's exam grade, and the third element contains the student's
        homework grade.

    Parameters:
        classList (list): A given list containing sublists that represent students in the class, like this:
            classList = [[student1 values],[student2 values],...]

    Example: finalGrade([[20,80,90],[10,60,40],[17, 77,56],[21,99,99]])
    Output:
        (17.0, 79.0, 71.25)
    """
    #Error Trapping
    if type(classList) != list:
        print("ERROR in finalGrade(): input must be list type.")
        return None
    for i in classList:
        if type(i) != list:
            print("ERROR in finalGrade(): class list can only contain elements of list type.")
            return None
        if len(i) > 3:
            print("ERROR in finalGrade(): a student list cannot be larger than 3 elements.")
        for j in i:
            if type(j) != float and type(j) != int:
                print("ERROR in finalGrade(): a student list cannot contain a non-numerical value")
    #Function
    attend_av = 0
    exam_av = 0
    hw_av = 0
    for i in classList:
        attend_av += i[0]
        exam_av += i[1]
        hw_av += i[2]
    attend_av = attend_av/len(classList)
    exam_av = exam_av/len(classList)
    hw_av = hw_av/len(classList)
    return (attend_av,exam_av,hw_av)

def gcDivisor(k,m):
    """
    gcDivisor(k,m): given two numbers, k and m, the function will find the createst common divisor of both numbers.

    Parameters:
        k (float or int): the first number passed into the function.
        m (float or int): the second number passed into the function.

    Example: gcDivisor(54,81)
    Output:
        27
    """
    #Error Trapping
    if type(k) != int and type(k) != float:
        print("ERROR in gcDivisor(): The first input must either be an integer or float value")
        return None
    if type(m) != int and type(m) != float:
        print("ERROR in gcDivisor(): The second input must either be an integer or float value")
        return None
    #function
    gc = 0
    if k > m:
        for i in range(2,m+1):
            if(k%i == 0 and m%i == 0):
                gc = i
    else:
        for i in range(2,k+1):
            if(m%i == 0 and k%i == 0):
                gc = i
    return gc

def isPrimeList(l):
    """
    isPrimeList(list): given a list, l, the function will iterate through the list and look for prime numbers. At the end the function returns a new
        sorted list containing all prime numbers from the original list.

    Parameters:
        l (list): the input passed to the function must be a list.

    Example: isPrimeList([11, 4, 8, 90, 87, 111, 17]])
    Output:
        [11,17]
    """
    #Error Trapping
    if type(l) != list:
        print("ERROR in is isPrimeList(): Input must be a list type.")
        return None
    for i in l:
        if type(i) != int:
            print("ERROR in isPrimeList(): Input List must contain only integers.")
    #function
    retlist = []
    for j in l:
        if isPrime(j) == True:
            retlist.append(j)
    retlist.sort()
    print(retlist)




#Function Calls
# print(isPrime(5))
# print(finalGrade([[20,80,90],[10,60,40],[17, 77,56],[21,99,99]]))
# print(gcDivisor(54,81))
# isPrimeList([11, 4, 8, 90, 87, 111, 17])
