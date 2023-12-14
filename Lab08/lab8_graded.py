######################################
#   Name: Dylan Calvin
#   BlazerID: dylcal13
#   Assignment: lab 8 (ungraded)
######################################


def argmin(l):
    """
    argmin(list): argmin takes a list and returns the index of the miniumum value in the list.

    Parameters:
        list (list): The list that is given to the Function

    Example: argmin([2,5,4,6,7,8,9,3,1])
    Output:
        8
    """
    #Error trapping
    if type(l) != list:
        print("ERROR in argmin(): input must be a list.")
        return None
    #Function
    imin = 0
    for i in range(len(l)):
        if l[i] < l[imin]:
            imin = i
    return imin

def sumOfEven(n):
    """
    sumofEven(n): Given an integer, n, the function calculates the sum of all the even numbers that precede n.
        NOTE: if n is even, n will not be included in the sum.

    Parameters:
        n (int)

    Returns value of the summ of even numbers that precede n.

    Example: sumOfEven(11)
    Output:
        30
    """
    #Error trapping
    if type(n) != int:
        print("ERROR in sumOfEven(): input must be an integer.")
        return None
    #function
    if n <= 1: # Base condition
        return n
    else:
        if n%2 == 0:
            return n + sumOfEven(n-2)
        else:
            n -= 1
            return n + sumOfEven(n-2)

def triangleChecker():
    """
    triangleChecker(): using the input file, triangle.txt, the function determines if the 3 values in the File
        represent a triangle, and then classify what triangle it is.

    Example: triangle.txt contains 3 lines: 5,4,6
    Output:
        The triangle is valid. the triangle is a Scalene triangle.
    """
    #function
    f=open("triangle.txt","r")
    line1,line2,line3=f.readline(),f.readline(),f.readline()
    line1,line2,line3=line1[:-1],line2[:-1],line3[:-1]
    f.close()
    if(line1.isdigit() == True and line2.isdigit() == True and line3.isdigit() == True):
        if line1==line2==line3:
            print("The Triangle is valid. it is an Equilateral.")
        elif (line1==line2) or (line1==line3) or (line2==line3):
            print("The Triangle is valid. it is an Isosceles.")
        else:
            print("The triangle is valid. it is a Scalene.")
    else:
        print("The triangle is not valid.")

def ssnChecker(s):
    """
    ssnChecker(s): Given a string, s, the function determines wether or not the sting follows
        the social security number format.

    Parameters:
        s (str): string given to the Function

    Function returns bool values

    Example: ssnChecker("999-99-9999")
    Output:
        True
    """
    #Error trapping
    if type(s) != str:
            print("ERROR in ssnChecker(): the input should be a string.")
            return None
    #Function
    if (len(s)==11) and (s[3] == "-" and s[6] == "-") and (s[0:3].isdigit() and s[4:6].isdigit() and s[7:].isdigit() == True):
        return True
    else:
        return False

print(argmin([2,5,4,6,7,8,9,3,1]))
print(sumOfEven(11))
triangleChecker()
print(ssnChecker("999-99-9999"))
