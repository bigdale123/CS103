###############################################
#  Name:       Dylan Calvin
#  BlazerID:   dylcal13
#  Assignment: Lab 4 (Graded)
#  Filename:   lab4_graded.py
###############################################


def letterCount(s1,s2):
    for i in s2:
        print(str(i)+" "+str(s1.count(i)))

def fibonacci(n):
    f1,f2 = 0,1
    for i in range(n):
        print(f1, end=" ")
        sum = f1+f2
        f1 = f2
        f2 = sum
    print("\n")

def oddChecker(t):
    for i in range(0,len(t)):
        #print(i)
        if t[i]%2 != 0:
            print(t[i])

def listSum(l):
    if len(l) < 7:
        print("ERROR: List must be at least 7 elements long.")
    else:
        numsum = 0
        for i in range(1,7):
            numsum += l[i]
        return numsum

letterCount("do you want to go to the movies tonight","qwerty")
print("--------------------")
fibonacci(5)
print("--------------------")
t=(1,2,3,5,8,22,35,92,123)
oddChecker(t)
print("--------------------")
l = [12,20,30,40,10,1,2,4,21,35,36,28,66]
print(listSum(l))