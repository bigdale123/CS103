######################################
#   Name: Dylan Calvin
#   BlazerID: dylcal13
#   Assignment: lab 8 (ungraded)
######################################


#########
# It was mentioned during grading that my error trapping should be assertions, but
#    we were told earlier in the semester that assertions break the auto grader.
#    That's why im not using assertions for error trapping.
#########
def listCheck(l):
    """
    listCheck(l): given an input, l, the function prints all the even numbers contained in the list.

    Parameters:
        l (list): the list given to the function.

    Example: listCheck([2,3,6,77,33,14,62,18,99,123,1])
    Output:
        2 6 14 18
    """
    #Error Trapping
    if type(l) != list:
        print("ERROR in listCheck(): The input should be a list.")
        return None
    #Function
    for i in l:
        if i%2 == 0:
            if i < 20:
                print(i, end = " ")
    print()

def sumOfN(n):
    """
    sumOfN(n): given a integer, n, the function returns the sum of all numbers that precede n, including n.

    Parameters:
        n (int): the number given to the function.

    Returns the value of the sum of all the numbers that preced n including n.

    Example: sumOfN(5)
    Output:
        15
    """
    #Error Trapping
    if type(n) != int:
        print("ERROR in sumOfN(): input must be an integer.")
        return None
    #Error Trapping
    if n <= 1:
        return n
    else:
        return n+sumOfN(n-1)

def fChecker():
    """
    fChecker(): using a file, inputFile.txt, the function reads the first name, last name, and age of the person, then prints
        a greeting and how old that person will be in 5 years.

    Example: fChecker, where inputFile.txt contains dylan, calvin, and 18
    Output:
        Hello Dylan Calvin. You will be 23 years old in 5 years.
    """
    #No Error Trapping required
    f = open("inputFile.txt","r")
    f_name,l_name,age = f.readline(),f.readline(),f.readline()
    f_name, l_name, age = f_name[:-1],l_name[:-1],age[:-1]
    print("Hello "+f_name+" "+l_name+". You will be "+str(int(age)+5)+" years old in 5 years.")
    f.close()

listCheck([2,3,6,77,33,14,62,18,99,123,1])
print(sumOfN(5))
fChecker()
