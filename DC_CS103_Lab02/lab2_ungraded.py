import math
# Lab 2 UNGRADED exercises
# These exercises are for practice only
# We will be creating a  Calculator

#our first function should add two numbers
def addTwoNumbers (f1,f2):
    return f1+f2

# create a multiplication function
def multTwoNumbers (f3,f4):
    return f3*f4

#uncomment the following function definition
def divTwoNumbers (f5,f6):
    return f5/f6

def nMultiplier (n):
    return (n+n*11+n*111)

#define the function subTwoNumbers below
def subTwoNumbers (f7,f8):
    return f7-f8

def averageOfThree (a,b,c):
    return (a+b+c)/3

def radToDegree (rad):
    return rad*180/math.pi

########################################################
# Function Calls
########################################################
# Firstly, we will create our variables
f1 = 25.2
f2 = 7.3
# create the rest of the needed variables, f3,f4...etc
# now we will call functions with the corresponding variables
print ("The result of addTwoNumbers")
print(addTwoNumbers(f1,f2))
# I can call the same function with any values
print(addTwoNumbers(75,45.5))
# I can put the result into another variable
sumOfTwo = addTwoNumbers (45.22, 65.66)
# now the result is inside the sumOfTwo variable
# Let's print it
print(sumOfTwo)
#Now, it is your job to "call" other functions
print(subTwoNumbers(6.66,4.11))
print(multTwoNumbers(5.2,2.0))
print(divTwoNumbers(12.6,3.0))
print(nMultiplier(5))
print(averageOfThree(11,33,76))
print(radToDegree(52))


