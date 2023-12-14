###############################################
#  Name:       Dylan Calvin
#  BlazerID:   dylcal13
#  Assignment: Lab 4 (Un-Graded)
#  Filename:   lab4_ungraded.py
###############################################

import random

def evenNumbers(x):
    i = 0
    num_list = []
    for i in range(0,x+1):
        if i%2 == 0:
            num_list.append(i)
        i += 1
    return str(num_list)

def factorial(f):
    fac = 1
    for i in range(1,f+1):
        fac = fac*i
    return fac

def replaceCharacter(s):
    letter_to_replace = s[0]
    list_string = list(s)
    for i in range(1,len(list_string)):
        if list_string[i]==letter_to_replace:
            list_string[i] = "$"
    s = ""
    for i in range(0,len(list_string)):
        s = s + list_string[i]
    return s

def printA():
    print(" ##### ")
    print("#     #")
    print("#     #")
    print("#     #")
    print("#######")
    print("#     #")
    print("#     #")
    print("#     #")
    print("#     #")
    print("#     #")

def isVowel(a):
    if a in ["a","e","i","o","u"]:
        return True
    else:
        return False

def randNumbers(r):
    list_rand = []
    sum = 0
    for i in range(0,r):
        random_number = random.randint(0,9)
        print(str(i+1)+". random number: "+str(random_number))
        list_rand.append(random_number)
    for i in range(0,len(list_rand)):
        sum += list_rand[i]
    print(" Average of numbers: " +str(sum/len(list_rand)))



print(evenNumbers(12))
print("-------------------------------")
print(factorial(7))
print("-------------------------------")
randNumbers(5)
print("-------------------------------")
print(replaceCharacter("restart"))
print("-------------------------------")
printA()
print("-------------------------------")
print(isVowel("a"))








