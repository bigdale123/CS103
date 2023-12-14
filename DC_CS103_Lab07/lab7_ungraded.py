import math
def volCylinder(r,h):
    """
    volCylinder(r,h): Given two numerical inputs (meaning float or int), the function will calculate the
        volume of a cylinder using the given radius and height

    Parameters:
        r (int or float) = the given radius of the Cylinder
        f (int or float) = the given height of the Cylinder

    Example: volCylinder(2.5,14)
    Output:
        274.88
    """
    #Error Trapping
    if type(r) != float and type(r) != int:
        print("ERROR in volCylinder(): radius must be a float or integer.")
        return None
    if type(h) != float and type(h) != int:
        print("ERROR in volCylinder(): height must be a float or integer.")
        return None
    # Function
    return math.pi*(r**2)*h

def cCount(s):
    """
    cCount(S): Given a string, s, the function will determine how many letters, numbers, symbols and spaces exist in the string.

    Parameters:
        s (str) = the given string thats passed into the Function

    Example: cCount("hello CLASS! 123 *")
    Output:
        Number of Letters: 10
        Number of Numbers: 3
        Number of Symbols: 2
        Number of Spaces:  3
    """
    #Error Trapping
    if type(s) != str:
        print("ERROR in cCount(): Input must be a string.")
        return None
    # Function
    alpha = 0
    number = 0
    space = 0 #The final frontier
    symbol = 0
    for i in s:
        if i.isalpha() == True:
            alpha += 1
        elif i.isdigit() == True:
            number += 1
        elif i.isspace() == True:
            space += 1 #The frontier expands
        else:
            symbol += 1
    print("Number of Letters: "+str(alpha))
    print("Number of Numbers: "+str(number))
    print("Number of Symbols: "+str(symbol))
    print("Number of Spaces: "+str(space))


def isSorted(l):
    """
    isSorted(l): Given a list, l, the function will determine if the list is sorted, and if it is sorted determine how it is sorted.

    Parameters:
        l (list) = the list passed into the Function

    Example: isSorted([4,3,2,1])
    Output:
        Sorted Max to Min
    """
    #Error Trapping
    if type(l) != list:
        print("ERROR in isSorted(): Input must be a list.")
        return None
    #Function
    l1 = l[:]
    l2 = l[:]
    l1.sort()
    l2.sort()
    l2.reverse()
    if l1 == l:
        print("Sorted Min to Max")
    elif l2 == l:
        print("Sorted Max to Min")
    else:
        print("Unsorted")
    #print(l1)

def listCompare(l1,l2):
    missing = []
    extra = []
    for i in l2:
        #print(i)
        if (i in l1) == False:
            extra.append(i)
    for i in l1:
        #print(i)
        if (i in l2) == False:
            missing.append(i)
    print(str(missing))
    print(str(extra))

def bruh_moment(s):
    for c in range(len(s)):
        if s[c] == "x":
            first = c
            break
    s = s[::-1]
    for c in range(len(s)):
        if s[c] == "x":
            last = c
            break
    last = len(s)-last-1
    print(first+last)


#Function Calls
# print("--- Results of isSorted() ---")
# unsorted = [1,4,3,2]
# sorted_a = [1,2,3,4]
# sorted_d = [4,3,2,1]
#
# isSorted(unsorted)
# isSorted(sorted_a)
# isSorted(sorted_d)
#
# print("--- Results of volCylinder() ---")
# print(volCylinder(2.5,14))
# print(volCylinder(10,10))
#
# print("--- Results of cCount() ---")
# cCount("hello CLASS! 123 *")
listCompare(['a', 'b', 'c', 'd', 'e'],['b', 'd', 'e', 'f', 'g'])
bruh_moment("exit execution")
