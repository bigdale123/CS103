import math
# Lab 2 GRADED exercises
# Return only this script file
def f(x,y):
    return int((x+y)**3/(x**2+y**2)**.5)
def fahr2celsius (f):
    return (f-32)*(5/9)
def volumeSphere (r):
    return (4/3)*math.pi*r**3
def areaTriangle (b,h):
    return (b*h)/2
########################################################
# Function Calls
# Do not Change/modify/touch.. any code below
########################################################
print ("\n**************************************")
x=3
y=4
print ("The result of function f ")
print(f (x,y))
print ("\n**************************************")
print ("\n**************************************")
b=10
h=2.5
print ("The result of Area of Triangle calculation")
print(areaTriangle (b,h))
print ("\n**************************************")
print ("\n**************************************")
f=74
print ("The result of Fahrenheit to Celsius calculation")
print(fahr2celsius (f))
print ("\n**************************************")
r=10
print ("The result of volumeSphere ")
print(volumeSphere (r))
print ("\n**************************************")